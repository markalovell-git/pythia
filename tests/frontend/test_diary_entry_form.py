import pytest
from PyQt6.QtCore import QDate, QTime

from app.frontend.models.diary_model import DiaryEntry
from app.frontend.widgets.diary_entry_form import DiaryEntryForm


def _entry(entry_time=None) -> DiaryEntry:
    return DiaryEntry(
        entry_id="e1",
        user_id="u1",
        entry_date="2026-07-19",
        content="content",
        created_at="2026-01-01T00:00:00",
        updated_at="2026-01-01T00:00:00",
        title="A title",
        entry_time=entry_time,
    )


@pytest.fixture
def form(qtbot, mock_api):
    mock_api["get_locations"].return_value = []
    f = DiaryEntryForm()
    qtbot.addWidget(f)
    f.set_user("u1")
    return f


class TestTimePicker:
    def test_timed_entry_roundtrips(self, form):
        form.set_entry(_entry("08:30"), QDate(2026, 7, 19))
        assert form.time_edit.time() == QTime(8, 30)
        assert form._time_value() == "08:30"

    def test_missing_time_defaults_to_1201pm(self, form):
        form.set_entry(_entry(None), QDate(2026, 7, 19))
        assert form.time_edit.time() == QTime(12, 1)
        assert form._time_value() == "12:01"

    def test_midnight_saves_as_a_real_time_not_null(self, form):
        form.set_entry(_entry("00:00"), QDate(2026, 7, 19))
        assert form.time_edit.time() == QTime(0, 0)
        assert form._time_value() == "00:00"

    def test_unpadded_time_is_normalised(self, form):
        form.set_entry(_entry("9:05"), QDate(2026, 7, 19))
        assert form._time_value() == "09:05"

    def test_legacy_freetext_time_discarded_for_default(self, form):
        # Imported diary.xml has values like "2h" that QTimeEdit can't show;
        # they are dropped in favour of the 12:01pm default.
        form.set_entry(_entry("2h"), QDate(2026, 7, 19))
        assert form.time_edit.time() == QTime(12, 1)
        assert form._time_value() == "12:01"

    def test_create_mode_starts_at_default_time(self, form):
        form.set_entry(None, QDate(2026, 7, 19))
        assert form._time_value() == "12:01"
        assert form.save_btn.text() == "Create"

    def test_time_change_marks_form_dirty(self, form):
        form.set_entry(_entry("08:30"), QDate(2026, 7, 19))
        assert not form.is_dirty()
        form.time_edit.setTime(QTime(9, 0))
        assert form.is_dirty()


class TestCategoryChips:
    def test_one_chip_per_known_category(self, form):
        from app.common.constants import DIARY_CATEGORIES
        form.set_entry(None, QDate(2026, 7, 19))
        assert set(form._chips) == {slug for slug, _ in DIARY_CATEGORIES}
        assert all(chip.isCheckable() for chip in form._chips.values())

    def test_entry_categories_start_lit(self, form):
        entry = _entry()
        entry.categories = ["family", "outing"]
        form.set_entry(entry, QDate(2026, 7, 19))
        assert form._chips["family"].isChecked()
        assert form._chips["outing"].isChecked()
        assert not form._chips["world"].isChecked()

    def test_clicking_toggles_selection(self, form):
        form.set_entry(None, QDate(2026, 7, 19))
        form._chips["family"].click()
        assert form._checked_categories() == ["family"]
        form._chips["family"].click()
        assert form._checked_categories() == []

    def test_multiple_categories_can_be_lit_at_once(self, form):
        form.set_entry(None, QDate(2026, 7, 19))
        for slug in ("family", "outing", "world"):
            form._chips[slug].click()
        assert sorted(form._checked_categories()) == ["family", "outing", "world"]

    def test_toggling_marks_form_dirty(self, form):
        entry = _entry()
        entry.categories = ["family"]
        form.set_entry(entry, QDate(2026, 7, 19))
        assert not form.is_dirty()
        form._chips["world"].click()
        assert form.is_dirty()

    def test_unknown_legacy_slug_gets_a_lit_chip(self, form):
        entry = _entry()
        entry.categories = ["travel"]  # legacy diary.xml slug
        form.set_entry(entry, QDate(2026, 7, 19))
        assert "travel" in form._chips
        assert form._chips["travel"].isChecked()
        assert form._chips["travel"].text() == "Travel"
        assert "travel" in form._checked_categories()

    def _row_counts(self, form):
        counts = []
        for row in form._chip_rows:
            counts.append(
                sum(1 for j in range(row.count()) if row.itemAt(j).widget() is not None)
            )
        return counts

    def test_chips_split_evenly_across_two_rows(self, form):
        form.set_entry(None, QDate(2026, 7, 19))
        assert len(form._chip_rows) == 2
        # 11 categories -> 6 then 5, the extra going to the first row.
        assert self._row_counts(form) == [6, 5]

    def test_rows_rebalance_when_a_legacy_chip_appears(self, form):
        entry = _entry()
        entry.categories = ["travel"]
        form.set_entry(entry, QDate(2026, 7, 19))
        assert self._row_counts(form) == [6, 6]

    def test_stale_legacy_chip_removed_on_next_entry(self, form):
        legacy = _entry()
        legacy.categories = ["travel"]
        form.set_entry(legacy, QDate(2026, 7, 19))
        assert "travel" in form._chips

        plain = _entry()
        plain.categories = ["family"]
        form.set_entry(plain, QDate(2026, 7, 19))
        assert "travel" not in form._chips
        assert form._checked_categories() == ["family"]


class TestFormLayout:
    def test_button_order_is_new_update_delete(self, form):
        # The button row is the last item in the form's outer layout.
        labels = []
        outer = form.layout()
        btn_row = outer.itemAt(outer.count() - 1).layout()
        for i in range(btn_row.count()):
            w = btn_row.itemAt(i).widget()
            if w is not None:
                labels.append(w.text())
        assert labels == ["New", "Create", "Delete"]

    def test_required_markers_removed_from_date_location_description(self, form):
        from PyQt6.QtWidgets import QFormLayout
        inner = form.findChild(QFormLayout)
        labels = []
        for i in range(inner.rowCount()):
            item = inner.itemAt(i, QFormLayout.ItemRole.LabelRole)
            if item is not None and item.widget() is not None:
                labels.append(item.widget().text())
        assert "Date:" in labels
        assert "Location:" in labels
        assert "Description:" in labels
        assert "Category:" in labels
        # No required-field markers remain anywhere on the form.
        assert not any("(*)" in lbl for lbl in labels)

    def test_date_and_time_stay_narrow(self, form):
        from app.frontend.widgets.diary_entry_form import _FIELD_WIDTH
        assert form.date_edit.maximumWidth() == _FIELD_WIDTH
        assert form.time_edit.maximumWidth() == _FIELD_WIDTH

    def test_location_fields_are_much_wider_than_date_and_time(self, form):
        from app.frontend.widgets.diary_entry_form import _FIELD_WIDTH, _WIDE_FIELD_WIDTH
        assert _WIDE_FIELD_WIDTH > _FIELD_WIDTH * 3
        assert form.location_picker.combo.maximumWidth() == _WIDE_FIELD_WIDTH
        assert form.destination_picker.combo.maximumWidth() == _WIDE_FIELD_WIDTH
