"""Writer for the legacy diary.xml format; the counterpart of diary_import.

Output keeps that format's shape (no root element or XML declaration, undeclared
``vt:`` prefix), so parse_diary_xml can load it back.
"""
import re
from xml.sax.saxutils import escape

from app.common.database import DiaryEntry

_MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Characters XML 1.0 can't represent, which would make the backup unimportable.
_INVALID_XML_RE = re.compile("[^\t\n\r -퟿-�\U00010000-\U0010ffff]")


def _element(tag: str, value: str | None) -> str:
    if not value:
        return ""
    return f"<vt:{tag}>{escape(_INVALID_XML_RE.sub('', value))}</vt:{tag}>\n"


def _event(entry: DiaryEntry, location_names: dict[str, str]) -> str:
    d = entry.entry_date
    segment = ""
    if entry.segment_start:
        color = _element("color", entry.segment_color)
        segment = f"<vt:segment_start>\n{color}</vt:segment_start>\n"
    return (
        "<vt:diary_event>\n"
        + _element("category", entry.categories)
        + _element("date", f"{d.day} {_MONTHS[d.month - 1]} {d.year}")
        + _element("time", entry.entry_time)
        + _element("location", location_names.get(entry.location_id))
        + _element("destination", location_names.get(entry.destination_id))
        + _element("title", entry.title)
        # Always present, even when empty, as every entry in the format has one.
        + (_element("description", entry.content) or "<vt:description></vt:description>\n")
        + _element("visuals", entry.visual_cues)
        + segment
        + "</vt:diary_event>\n\n"
    )


def build_diary_xml(entries: list[DiaryEntry], location_names: dict[str, str]) -> str:
    """Serialise `entries`, resolving location ids through `location_names`."""
    return "".join(_event(entry, location_names) for entry in entries)
