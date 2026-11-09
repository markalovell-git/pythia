"""Parser for the legacy diary.xml format.

The file is not well-formed XML: it has no root element, an undeclared ``vt:``
prefix and bare ``&`` characters, so it is repaired in memory before parsing.
Its dates were typed by hand and come in many shapes.
"""
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime

_NS = "{urn:vt}"
_DEFAULT_TIME = "12:01"  # matches the diary form's default

_BARE_AMP_RE = re.compile(r"&(?!amp;|lt;|gt;|quot;|apos;|#)")
_SEPT_RE = re.compile(r"\bSept\b", re.IGNORECASE)
_TIME_24H_RE = re.compile(r"^(\d{1,2}):(\d{2})$")
_TIME_12H_RE = re.compile(r"^(\d{1,2}):(\d{2})\s*([ap])m$", re.IGNORECASE)

_FULL_DATE_FORMATS = (
    "%d %b %Y", "%d %B %Y", "%d %b, %Y", "%d %B, %Y",
    "%b %d %Y", "%b %d, %Y", "%B %d %Y", "%B %d, %Y",
)
_MONTH_ONLY_FORMATS = ("%b %Y", "%B %Y")


@dataclass
class ParsedEntry:
    entry_date: date
    month_only: bool  # source gave no day, so entry_date is the 1st of the month
    entry_time: str
    content: str
    title: str | None = None
    visual_cues: str | None = None
    categories: str = "|unsorted|"
    location: str | None = None
    destination: str | None = None
    segment_start: bool = False
    segment_color: str | None = None


def _parse_date(raw: str) -> tuple[date, bool] | None:
    """Returns (date, month_only), or None if `raw` matches no known format."""
    value = _SEPT_RE.sub("Sep", raw)
    for fmt in _FULL_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date(), False
        except ValueError:
            pass
    for fmt in _MONTH_ONLY_FORMATS:
        try:
            return datetime.strptime(value, fmt).date(), True
        except ValueError:
            pass
    return None


def _parse_time(raw: str | None) -> str:
    """Normalise to "HH:MM"; missing or unparseable values get the default."""
    value = (raw or "").strip()
    match = _TIME_24H_RE.match(value)
    if match:
        hour, minute = int(match.group(1)), int(match.group(2))
    else:
        match = _TIME_12H_RE.match(value)
        if not match:
            return _DEFAULT_TIME
        hour, minute = int(match.group(1)), int(match.group(2))
        if not 1 <= hour <= 12:
            return _DEFAULT_TIME
        hour = hour % 12 + (12 if match.group(3).lower() == "p" else 0)
    if hour > 23 or minute > 59:
        return _DEFAULT_TIME
    return f"{hour:02d}:{minute:02d}"


def _text(event: ET.Element, tag: str) -> str | None:
    value = (event.findtext(_NS + tag) or "").strip()
    return value or None


def parse_diary_xml(text: str) -> list[ParsedEntry]:
    """Parse the whole file, raising ValueError on any problem.

    All-or-nothing, so a caller replacing existing entries can parse first and
    never lose data to a bad file.
    """
    repaired = _BARE_AMP_RE.sub("&amp;", text)
    try:
        root = ET.fromstring(f'<root xmlns:vt="urn:vt">{repaired}</root>')
    except ET.ParseError as e:
        raise ValueError(f"Not a valid diary XML file: {e}") from e

    events = root.findall(_NS + "diary_event")
    if not events:
        raise ValueError("No diary entries found in this file")

    entries = []
    for number, event in enumerate(events, start=1):
        raw_date = _text(event, "date")
        parsed = _parse_date(raw_date) if raw_date else None
        if parsed is None:
            raise ValueError(f"Entry {number}: unrecognised date {raw_date!r}")
        entry_date, month_only = parsed

        segment = event.find(_NS + "segment_start")
        entries.append(ParsedEntry(
            entry_date=entry_date,
            month_only=month_only,
            entry_time=_parse_time(event.findtext(_NS + "time")),
            content=_text(event, "description") or "",
            title=_text(event, "title"),
            visual_cues=_text(event, "visuals"),
            categories=_text(event, "category") or "|unsorted|",
            location=_text(event, "location"),
            destination=_text(event, "destination"),
            segment_start=segment is not None,
            segment_color=_text(segment, "color") if segment is not None else None,
        ))
    return entries
