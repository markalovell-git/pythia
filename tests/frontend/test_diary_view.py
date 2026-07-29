import pytest
from PyQt6.QtCore import QDate

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
