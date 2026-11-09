import uuid
from datetime import datetime, date, timedelta

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.backend.diary_export import build_diary_xml
from app.backend.diary_import import parse_diary_xml
from app.common.database import get_db, UserData, DiaryEntry, Location

diary_router = APIRouter()


class DiaryEntryCreate(BaseModel):
    entry_date: date
    content: str
    title: str | None = None
    visual_cues: str | None = None
    categories: list[str] = ["unsorted"]
    entry_time: str | None = None
    location_id: str | None = None
    destination_id: str | None = None
    segment_start: bool = False
    segment_color: str | None = None


class DiaryEntryUpdate(BaseModel):
    entry_date: date | None = None
    content: str | None = None
    title: str | None = None
    visual_cues: str | None = None
    categories: list[str] | None = None
    entry_time: str | None = None
    location_id: str | None = None
    destination_id: str | None = None
    segment_start: bool | None = None
    segment_color: str | None = None


class DiaryImport(BaseModel):
    xml: str


def _categories_to_str(slugs: list[str]) -> str:
    slugs = [s for s in slugs if s]
    if not slugs:
        slugs = ["unsorted"]
    return "|" + "|".join(slugs) + "|"


def _categories_from_str(value: str | None) -> list[str]:
    slugs = [s for s in (value or "").split("|") if s]
    return slugs or ["unsorted"]


def _entry_response(entry: DiaryEntry, db: Session) -> dict:
    def _loc_name(location_id: str | None) -> str | None:
        if not location_id:
            return None
        loc = db.query(Location).filter(Location.location_id == location_id).first()
        return loc.name if loc else None

    return {
        "entry_id": entry.entry_id,
        "user_id": entry.user_id,
        "entry_date": str(entry.entry_date),
        "content": entry.content,
        "created_at": entry.created_at.isoformat(),
        "updated_at": entry.updated_at.isoformat(),
        "title": entry.title,
        "visual_cues": entry.visual_cues,
        "categories": _categories_from_str(entry.categories),
        "entry_time": entry.entry_time,
        "location_id": entry.location_id,
        "destination_id": entry.destination_id,
        "location_name": _loc_name(entry.location_id),
        "destination_name": _loc_name(entry.destination_id),
        "segment_start": bool(entry.segment_start),
        "segment_color": entry.segment_color,
    }


@diary_router.get("/get_diary_entries/{user_id}")
async def get_diary_entries(
    user_id: str, date: date | None = None, db: Session = Depends(get_db)
):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    q = db.query(DiaryEntry).filter(DiaryEntry.user_id == user_id)
    if date:
        q = q.filter(DiaryEntry.entry_date == date)
    q = q.order_by(DiaryEntry.entry_date, DiaryEntry.entry_time, DiaryEntry.created_at)
    return [_entry_response(e, db) for e in q.all()]


@diary_router.get("/diary_dates/{user_id}")
async def get_diary_dates(user_id: str, db: Session = Depends(get_db)):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    rows = (
        db.query(DiaryEntry.entry_date)
        .filter(DiaryEntry.user_id == user_id)
        .distinct()
        .all()
    )
    return [str(r[0]) for r in rows]


@diary_router.post("/create_diary_entry/{user_id}")
async def create_diary_entry(
    user_id: str, body: DiaryEntryCreate, db: Session = Depends(get_db)
):
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    now = datetime.utcnow()
    entry = DiaryEntry(
        entry_id=str(uuid.uuid4()),
        user_id=user_id,
        entry_date=body.entry_date,
        content=body.content,
        created_at=now,
        updated_at=now,
        title=body.title,
        visual_cues=body.visual_cues,
        categories=_categories_to_str(body.categories),
        entry_time=body.entry_time,
        location_id=body.location_id,
        destination_id=body.destination_id,
        segment_start=int(body.segment_start),
        segment_color=body.segment_color,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return _entry_response(entry, db)


@diary_router.put("/update_diary_entry/{entry_id}")
async def update_diary_entry(
    entry_id: str, body: DiaryEntryUpdate, db: Session = Depends(get_db)
):
    entry = db.query(DiaryEntry).filter(DiaryEntry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    data = body.model_dump(exclude_unset=True)
    if "categories" in data and data["categories"] is not None:
        data["categories"] = _categories_to_str(data["categories"])
    if "segment_start" in data and data["segment_start"] is not None:
        data["segment_start"] = int(data["segment_start"])
    for field, value in data.items():
        setattr(entry, field, value)
    entry.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(entry)
    return _entry_response(entry, db)


@diary_router.delete("/delete_diary_entry/{entry_id}")
async def delete_diary_entry(entry_id: str, db: Session = Depends(get_db)):
    entry = db.query(DiaryEntry).filter(DiaryEntry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"entry_id": entry_id, "deleted": True}


@diary_router.get("/export_diary/{user_id}")
async def export_diary(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserData).filter(UserData.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    entries = (
        db.query(DiaryEntry)
        .filter(DiaryEntry.user_id == user_id)
        .order_by(DiaryEntry.entry_date, DiaryEntry.entry_time, DiaryEntry.created_at)
        .all()
    )
    location_names = {loc.location_id: loc.name for loc in db.query(Location).all()}
    return {
        "xml": build_diary_xml(entries, location_names),
        "exported": len(entries),
        "username": user.username,
    }


@diary_router.post("/import_diary/{user_id}")
async def import_diary(user_id: str, body: DiaryImport, db: Session = Depends(get_db)):
    """Replace ALL of this user's diary entries with those in the XML file."""
    if not db.query(UserData).filter(UserData.user_id == user_id).first():
        raise HTTPException(status_code=404, detail="User not found")
    # Parse before touching the DB, so a bad file leaves existing entries intact.
    try:
        parsed = parse_diary_xml(body.xml)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # Name-only locations: bulk geocoding is impractical (Nominatim ~1 req/s).
    locations = {loc.name.lower(): loc.location_id for loc in db.query(Location).all()}

    def _location_id(name: str | None) -> str | None:
        if not name:
            return None
        key = name.lower()
        if key not in locations:
            locations[key] = str(uuid.uuid4())
            db.add(Location(location_id=locations[key], name=name))
        return locations[key]

    try:
        deleted = db.query(DiaryEntry).filter(DiaryEntry.user_id == user_id).delete()
        now = datetime.utcnow()
        for i, item in enumerate(parsed):
            db.add(DiaryEntry(
                entry_id=str(uuid.uuid4()),
                user_id=user_id,
                entry_date=item.entry_date,
                content=item.content,
                # Ordering falls back to created_at, so this keeps same-day
                # entries in file order.
                created_at=now + timedelta(microseconds=i),
                updated_at=now,
                title=item.title,
                visual_cues=item.visual_cues,
                categories=item.categories,
                entry_time=item.entry_time,
                location_id=_location_id(item.location),
                destination_id=_location_id(item.destination),
                segment_start=int(item.segment_start),
                segment_color=item.segment_color,
            ))
        db.commit()
    except Exception:
        db.rollback()
        raise
    return {
        "deleted": deleted,
        "imported": len(parsed),
        "month_only_dates": sum(1 for item in parsed if item.month_only),
    }
