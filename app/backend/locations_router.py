import uuid

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.common.database import get_db, Location

locations_router = APIRouter()


class LocationCreate(BaseModel):
    name: str
    latitude: float | None = None
    longitude: float | None = None
    timezone: str | None = None


class LocationUpdate(BaseModel):
    latitude: float | None = None
    longitude: float | None = None
    timezone: str | None = None


def _location_response(loc: Location) -> dict:
    return {
        "location_id": loc.location_id,
        "name": loc.name,
        "latitude": loc.latitude,
        "longitude": loc.longitude,
        "timezone": loc.timezone,
    }


@locations_router.get("/locations")
async def get_locations(q: str = "", db: Session = Depends(get_db)):
    query = db.query(Location)
    if q:
        query = query.filter(Location.name.ilike(f"%{q}%"))
    return [_location_response(l) for l in query.order_by(Location.name).all()]


@locations_router.post("/locations")
async def create_location(body: LocationCreate, db: Session = Depends(get_db)):
    name = body.name.strip()
    if not name:
        raise HTTPException(status_code=422, detail="Location name is required")
    existing = db.query(Location).filter(Location.name.ilike(name)).first()
    if existing:
        # Backfill coordinates a name-only row was missing.
        changed = False
        if existing.latitude is None and body.latitude is not None:
            existing.latitude = body.latitude
            existing.longitude = body.longitude
            changed = True
        if existing.timezone is None and body.timezone is not None:
            existing.timezone = body.timezone
            changed = True
        if changed:
            db.commit()
            db.refresh(existing)
        return _location_response(existing)
    loc = Location(
        location_id=str(uuid.uuid4()),
        name=name,
        latitude=body.latitude,
        longitude=body.longitude,
        timezone=body.timezone,
    )
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return _location_response(loc)


@locations_router.put("/locations/{location_id}")
async def update_location(
    location_id: str, body: LocationUpdate, db: Session = Depends(get_db)
):
    loc = db.query(Location).filter(Location.location_id == location_id).first()
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    data = body.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(loc, field, value)
    db.commit()
    db.refresh(loc)
    return _location_response(loc)
