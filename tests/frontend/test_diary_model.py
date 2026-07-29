from app.frontend.models.diary_model import DiaryEntry, order_entries


def _entry(entry_id, entry_date, entry_time=None, created_at="2026-01-01T00:00:00") -> DiaryEntry:
    return DiaryEntry(
        entry_id=entry_id,
        user_id="u1",
        entry_date=entry_date,
        content="content",
        created_at=created_at,
        updated_at=created_at,
        entry_time=entry_time,
    )


class TestOrderEntries:
    def test_orders_by_date_first(self):
        e1 = _entry("e1", "2026-07-19")
        e2 = _entry("e2", "2026-05-04")
        e3 = _entry("e3", "2026-06-12")
        assert [e.entry_id for e in order_entries([e1, e2, e3])] == ["e2", "e3", "e1"]

    def test_untimed_entries_lead_the_day(self):
        timed = _entry("timed", "2026-07-19", entry_time="09:00", created_at="2026-01-01T00:00:01")
        untimed = _entry("untimed", "2026-07-19", entry_time=None, created_at="2026-01-01T00:00:00")
        result = order_entries([timed, untimed])
        assert [e.entry_id for e in result] == ["untimed", "timed"]

    def test_numeric_time_ordering_not_lexicographic(self):
        # "9:00" would sort after "21:00" as plain text; must sort before it.
        early = _entry("early", "2026-07-19", entry_time="9:00")
        late = _entry("late", "2026-07-19", entry_time="21:00")
        result = order_entries([late, early])
        assert [e.entry_id for e in result] == ["early", "late"]

    def test_normal_time_ordering_within_day(self):
        a = _entry("a", "2026-07-19", entry_time="07:45")
        b = _entry("b", "2026-07-19", entry_time="19:30")
        result = order_entries([b, a])
        assert [e.entry_id for e in result] == ["a", "b"]

    def test_untimed_entries_on_same_day_keep_created_at_order(self):
        first = _entry("first", "2026-07-19", created_at="2026-01-01T00:00:00")
        second = _entry("second", "2026-07-19", created_at="2026-01-01T00:00:01")
        result = order_entries([second, first])
        assert [e.entry_id for e in result] == ["first", "second"]

    def test_legacy_unparseable_time_does_not_raise(self):
        legacy = _entry("legacy", "2026-07-19", entry_time="2h")
        timed = _entry("timed", "2026-07-19", entry_time="09:00")
        result = order_entries([legacy, timed])
        # Doesn't crash; legacy free-text values sort after real times.
        assert [e.entry_id for e in result] == ["timed", "legacy"]

    def test_three_entries_one_day_matches_seed_shape(self):
        untimed = _entry("untimed", "2026-07-19", created_at="2026-01-01T00:00:00")
        morning = _entry("morning", "2026-07-19", entry_time="07:45", created_at="2026-01-01T00:00:01")
        evening = _entry("evening", "2026-07-19", entry_time="19:30", created_at="2026-01-01T00:00:02")
        result = order_entries([evening, untimed, morning])
        assert [e.entry_id for e in result] == ["untimed", "morning", "evening"]

    def test_input_list_not_mutated(self):
        original = [_entry("b", "2026-07-19"), _entry("a", "2026-05-04")]
        snapshot = list(original)
        order_entries(original)
        assert original == snapshot
