import re
from dataclasses import dataclass, field
from app.frontend import api_client

_TIME_RE = re.compile(r"^(\d{1,2}):(\d{2})$")


@dataclass
class DiaryEntry:
    entry_id: str
    user_id: str
    entry_date: str
    content: str
    created_at: str
    updated_at: str
    title: str | None = None
    visual_cues: str | None = None
    categories: list[str] = field(default_factory=lambda: ["unsorted"])
    entry_time: str | None = None
    location_id: str | None = None
    destination_id: str | None = None
    location_name: str | None = None
    destination_name: str | None = None
    segment_start: bool = False
    segment_color: str | None = None


def get_entries(user_id: str, date: str | None = None) -> list[DiaryEntry]:
    rows = api_client.get_diary_entries(user_id, date=date)
    return [DiaryEntry(**r) for r in rows]


def create_entry(user_id: str, payload: dict) -> DiaryEntry:
    raw = api_client.create_diary_entry(user_id, payload)
    return DiaryEntry(**raw)


def update_entry(entry_id: str, payload: dict) -> DiaryEntry:
    raw = api_client.update_diary_entry(entry_id, payload)
    return DiaryEntry(**raw)


def delete_entry(entry_id: str) -> None:
    api_client.delete_diary_entry(entry_id)


def dates_with_entries(user_id: str) -> set[str]:
    """Returns ISO date strings (YYYY-MM-DD) that have at least one entry."""
    return set(api_client.get_diary_dates(user_id))


def _time_rank(entry_time: str | None) -> tuple[int, str]:
    """Sort key fixing the backend's lexicographic TEXT ordering of entry_time.

    Untimed entries lead the day (rank 0). Parseable "H:MM"/"HH:MM" values sort
    numerically via a zero-padded key (rank 1), so "9:00" precedes "21:00".
    Unparseable legacy values (e.g. "2h") fall back to raw text (rank 2), kept
    out of the numeric range so they never scramble real times.
    """
    if not entry_time:
        return (0, "")
    m = _TIME_RE.match(entry_time.strip())
    if m:
        hour, minute = m.groups()
        return (1, f"{int(hour):02d}:{minute}")
    return (2, entry_time)


def order_entries(entries: list[DiaryEntry]) -> list[DiaryEntry]:
    """Stable chronological order: date, then time-of-day, then entry order.

    Entries without a parseable time come first on their date (matching how
    the backend's NULL-first ordering already behaves), then real times in
    numeric order, then legacy free-text values last. Ties (including two
    untimed entries on the same day) keep their `created_at` order, i.e. the
    order they were entered in.
    """
    return sorted(
        entries,
        key=lambda e: (e.entry_date, _time_rank(e.entry_time), e.created_at),
    )
