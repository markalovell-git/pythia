import pytest
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox

from app.frontend.widgets.diary_view import DiaryView

# Same six entries as scripts/seed_diary.py, already in final chronological
# order (order_entries would sort them identically).
_ENTRIES = [
    dict(entry_id="e1", user_id="u1", entry_date="2026-05-04", content="c1",
         created_at="2026-01-01T00:00:00", updated_at="2026-01-01T00:00:00",
         title="Early start", entry_time="08:30"),
    dict(entry_id="e2", user_id="u1", entry_date="2026-06-12", content="c2",
         created_at="2026-01-01T00:01:00", updated_at="2026-01-01T00:01:00",
         title="A day without hours", entry_time=None),
    dict(entry_id="e3", user_id="u1", entry_date="2026-07-02", content="c3",
         created_at="2026-01-01T00:02:00", updated_at="2026-01-01T00:02:00",
         title="Late thoughts", entry_time="21:15"),
    dict(entry_id="e4", user_id="u1", entry_date="2026-07-19", content="c4",
         created_at="2026-01-01T00:03:00", updated_at="2026-01-01T00:03:00",
         title="Woke unplaced", entry_time=None),
    dict(entry_id="e5", user_id="u1", entry_date="2026-07-19", content="c5",
         created_at="2026-01-01T00:04:00", updated_at="2026-01-01T00:04:00",
         title="Morning walk", entry_time="07:45"),
    dict(entry_id="e6", user_id="u1", entry_date="2026-07-19", content="c6",
         created_at="2026-01-01T00:05:00", updated_at="2026-01-01T00:05:00",
         title="Evening, three of three", entry_time="19:30"),
]


@pytest.fixture
def diary_view(qtbot, mock_api):
    mock_api["get_diary_entries"].return_value = list(_ENTRIES)
    mock_api["get_diary_dates"].return_value = ["2026-05-04", "2026-06-12", "2026-07-02", "2026-07-19"]
    mock_api["get_locations"].return_value = []

    view = DiaryView()
    qtbot.addWidget(view)
    view.load("u1")
    qtbot.waitUntil(lambda: len(view._entries) == 6, timeout=2000)
    # Anchor on the first entry's date so navigation tests start from a known
    # index=0, regardless of what "today" happens to be when tests run.
    view.calendar.setSelectedDate(QDate(2026, 5, 4))
    assert view._index == 0
    return view


def _titles(view):
    return [e.title for e in view._entries]


class TestDiaryViewNavigation:
    def test_no_entry_list_widget(self, diary_view):
        assert not hasattr(diary_view, "entry_list")

    def test_arrow_steps_forward_one_entry_at_a_time(self, diary_view, qtbot):
        assert _titles(diary_view) == [
            "Early start", "A day without hours", "Late thoughts",
            "Woke unplaced", "Morning walk", "Evening, three of three",
        ]
        diary_view.next_btn.click()
        assert diary_view._index == 1
        diary_view.next_btn.click()
        assert diary_view._index == 2

    def test_stepping_within_multiday_keeps_same_date_updates_counter(self, diary_view):
        for _ in range(3):
            diary_view.next_btn.click()
        assert diary_view._index == 3
        assert diary_view._entries[diary_view._index].entry_date == "2026-07-19"
        assert "1 of 3" in diary_view.position_label.text()

        diary_view.next_btn.click()
        assert diary_view._index == 4
        assert diary_view._entries[diary_view._index].entry_date == "2026-07-19"
        assert "2 of 3" in diary_view.position_label.text()

        diary_view.next_btn.click()
        assert diary_view._index == 5
        assert "3 of 3" in diary_view.position_label.text()

    def test_prev_disabled_at_first_next_disabled_at_last(self, diary_view):
        assert diary_view._index == 0
        assert not diary_view.prev_btn.isEnabled()
        assert diary_view.next_btn.isEnabled()

        for _ in range(5):
            diary_view.next_btn.click()
        assert diary_view._index == 5
        assert not diary_view.next_btn.isEnabled()
        assert diary_view.prev_btn.isEnabled()

    def test_prev_arrow_steps_backward(self, diary_view):
        for _ in range(5):
            diary_view.next_btn.click()
        diary_view.prev_btn.click()
        assert diary_view._index == 4

    def test_calendar_click_jumps_to_first_entry_of_day(self, diary_view):
        diary_view.calendar.setSelectedDate(QDate(2026, 7, 19))
        assert diary_view._index == 3
        assert diary_view._entries[diary_view._index].title == "Woke unplaced"

    def test_calendar_click_on_empty_date_shows_blank_form_with_live_arrows(self, diary_view):
        diary_view.calendar.setSelectedDate(QDate(2026, 6, 1))  # between e1 and e2, no entry
        assert diary_view._index == -1
        assert not diary_view.form._entry
        assert diary_view.prev_btn.isEnabled()  # e1 (2026-05-04) is before
        assert diary_view.next_btn.isEnabled()  # e2 (2026-06-12) is after

        diary_view.next_btn.click()
        assert diary_view._entries[diary_view._index].title == "A day without hours"


class TestDiaryViewImport:
    @pytest.fixture
    def picked_file(self, tmp_path, monkeypatch):
        path = tmp_path / "diary.xml"
        path.write_text("<xml/>", encoding="utf-8")
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QFileDialog.getOpenFileName",
            lambda *a, **k: (str(path), ""),
        )
        return path

    def _answer(self, monkeypatch, button):
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QMessageBox.warning",
            lambda *a, **k: button,
        )

    def test_cancelling_confirmation_makes_no_api_call(self, diary_view, mock_api, picked_file, monkeypatch):
        self._answer(monkeypatch, QMessageBox.StandardButton.Cancel)
        diary_view.import_btn.click()
        mock_api["import_diary"].assert_not_called()

    def test_cancelling_file_dialog_makes_no_api_call(self, diary_view, mock_api, monkeypatch):
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QFileDialog.getOpenFileName",
            lambda *a, **k: ("", ""),
        )
        diary_view.import_btn.click()
        mock_api["import_diary"].assert_not_called()

    def test_confirming_imports_and_reloads(self, diary_view, mock_api, picked_file, monkeypatch, qtbot):
        self._answer(monkeypatch, QMessageBox.StandardButton.Yes)
        shown = []
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QMessageBox.information",
            lambda _parent, _title, text: shown.append(text),
        )
        mock_api["import_diary"].return_value = {"deleted": 6, "imported": 1, "month_only_dates": 1}
        mock_api["get_diary_entries"].return_value = [_ENTRIES[0]]
        diary_view.import_btn.click()
        qtbot.waitUntil(lambda: len(diary_view._entries) == 1, timeout=2000)
        mock_api["import_diary"].assert_called_once_with("u1", "<xml/>")
        assert "Imported 1 entries, replacing 6" in shown[0]
        assert "1 entries gave only a month" in shown[0]
        assert diary_view.import_btn.isEnabled()

    def test_failure_shows_error_dialog(self, diary_view, mock_api, picked_file, monkeypatch, qtbot):
        self._answer(monkeypatch, QMessageBox.StandardButton.Yes)
        errors = []
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QMessageBox.critical",
            lambda _parent, _title, text: errors.append(text),
        )
        mock_api["import_diary"].side_effect = ValueError("Entry 2: unrecognised date 'x'")
        diary_view.import_btn.click()
        qtbot.waitUntil(lambda: bool(errors), timeout=2000)
        assert "Entry 2" in errors[0]
        assert diary_view.import_btn.isEnabled()


class TestDiaryViewExport:
    _RESULT = {"xml": "<vt:diary_event>é</vt:diary_event>\n", "exported": 1, "username": "mark lovell"}

    def _save_to(self, monkeypatch, path):
        names = []

        def fake_dialog(_parent, _title, default, _filter):
            names.append(default)
            return (str(path), "")

        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.QFileDialog.getSaveFileName", fake_dialog
        )
        return names

    def _capture(self, monkeypatch, kind):
        shown = []
        monkeypatch.setattr(
            f"app.frontend.widgets.diary_view.QMessageBox.{kind}",
            lambda _parent, _title, text: shown.append(text),
        )
        return shown

    def test_writes_file_with_suggested_name(self, diary_view, mock_api, tmp_path, monkeypatch, qtbot):
        target = tmp_path / "backup"
        names = self._save_to(monkeypatch, target)
        shown = self._capture(monkeypatch, "information")
        mock_api["export_diary"].return_value = self._RESULT
        diary_view.export_btn.click()
        qtbot.waitUntil(lambda: bool(shown), timeout=2000)
        today = QDate.currentDate().toString("yyyy-MM-dd")
        assert names[0].endswith(f"diary_mark_lovell_{today}.xml")
        written = tmp_path / "backup.xml"  # .xml added when no suffix was typed
        assert written.read_text(encoding="utf-8") == self._RESULT["xml"]
        assert not (tmp_path / "backup.xml.tmp").exists()
        assert diary_view.export_btn.isEnabled()

    def test_cancelling_save_dialog_writes_nothing(self, diary_view, mock_api, tmp_path, monkeypatch, qtbot):
        names = self._save_to(monkeypatch, "")
        mock_api["export_diary"].return_value = self._RESULT
        diary_view.export_btn.click()
        qtbot.waitUntil(lambda: bool(names), timeout=2000)
        assert list(tmp_path.iterdir()) == []

    def test_empty_diary_skips_save_dialog(self, diary_view, mock_api, tmp_path, monkeypatch, qtbot):
        names = self._save_to(monkeypatch, tmp_path / "x.xml")
        shown = self._capture(monkeypatch, "information")
        mock_api["export_diary"].return_value = {"xml": "", "exported": 0, "username": "u"}
        diary_view.export_btn.click()
        qtbot.waitUntil(lambda: bool(shown), timeout=2000)
        assert names == []

    def test_write_failure_keeps_existing_backup(self, diary_view, mock_api, tmp_path, monkeypatch, qtbot):
        target = tmp_path / "old.xml"
        target.write_text("old backup", encoding="utf-8")
        self._save_to(monkeypatch, target)
        errors = self._capture(monkeypatch, "critical")
        monkeypatch.setattr(
            "app.frontend.widgets.diary_view.os.replace",
            lambda *a: (_ for _ in ()).throw(OSError("disk full")),
        )
        mock_api["export_diary"].return_value = self._RESULT
        diary_view.export_btn.click()
        qtbot.waitUntil(lambda: bool(errors), timeout=2000)
        assert "disk full" in errors[0]
        assert target.read_text(encoding="utf-8") == "old backup"
        assert not (tmp_path / "old.xml.tmp").exists()

    def test_api_failure_shows_error(self, diary_view, mock_api, monkeypatch, qtbot):
        errors = self._capture(monkeypatch, "critical")
        mock_api["export_diary"].side_effect = RuntimeError("backend down")
        diary_view.export_btn.click()
        qtbot.waitUntil(lambda: bool(errors), timeout=2000)
        assert "backend down" in errors[0]
        assert diary_view.export_btn.isEnabled()


class TestDiaryViewNew:
    def test_new_starts_blank_entry_dated_today(self, diary_view):
        diary_view.next_btn.click()  # sitting on a past entry
        assert diary_view._index == 1
        diary_view.form.new_btn.click()
        today = QDate.currentDate()
        assert diary_view.form._entry is None
        assert diary_view.form.date_edit.date() == today
        assert diary_view.calendar.selectedDate() == today
        assert diary_view._index == -1
