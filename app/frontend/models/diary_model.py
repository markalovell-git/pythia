from dataclasses import dataclass
from app.frontend import api_client


@dataclass
class DiaryEntry:
    entry_id: str
    user_id: str
    entry_date: str
    content: str
    created_at: str
    updated_at: str


def get_entries(user_id: str, date: str | None = None) -> list[DiaryEntry]:
    rows = api_client.get_diary_entries(user_id, date=date)
    return [DiaryEntry(**r) for r in rows]


def create_entry(user_id: str, entry_date: str, content: str) -> DiaryEntry:
    raw = api_client.create_diary_entry(user_id, entry_date, content)
    return DiaryEntry(**raw)


def update_entry(entry_id: str, content: str) -> DiaryEntry:
    raw = api_client.update_diary_entry(entry_id, content)
    return DiaryEntry(**raw)


def delete_entry(entry_id: str) -> None:
    api_client.delete_diary_entry(entry_id)


def dates_with_entries(user_id: str) -> set[str]:
    """Returns ISO date strings (YYYY-MM-DD) that have at least one entry."""
    entries = get_entries(user_id)
    return {e.entry_date for e in entries}
