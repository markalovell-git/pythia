from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.common.database import get_db, UserData, UserSettings, NatalChart
from app.astrology.chart import compute_natal_chart, compute_transits, compute_planet_positions

chart_router = APIRouter()


@chart_router.post("/calculate_natal_chart/{user_id}")
async def calculate_natal_chart(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserData).filter(UserData.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    try:
        positions, cusps = compute_natal_chart(
            user.birth_datetime, user.birth_timezone, settings.zodiac_system,
            user.birth_lat, user.birth_lon, settings.house_system,
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if chart:
        chart.positions   = positions
        chart.house_cusps = cusps
        chart.computed_at = datetime.now(timezone.utc)
    else:
        db.add(NatalChart(
            user_id=user_id,
            computed_at=datetime.now(timezone.utc),
            positions=positions,
            house_cusps=cusps,
        ))
    db.commit()

    return {
        "user_id":       user_id,
        "zodiac_system": settings.zodiac_system,
        "house_system":  settings.house_system,
        "positions":     positions,
        "house_cusps":   cusps,
    }


@chart_router.get("/get_natal_chart/{user_id}")
async def get_natal_chart(user_id: str, db: Session = Depends(get_db)):
    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if not chart:
        raise HTTPException(
            status_code=404,
            detail="Natal chart not found — call /calculate_natal_chart first",
        )
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    return {
        "user_id":       user_id,
        "zodiac_system": settings.zodiac_system,
        "house_system":  settings.house_system,
        "computed_at":   chart.computed_at,
        "positions":     chart.positions,
        "house_cusps":   chart.house_cusps,
    }


@chart_router.get("/calculate_transits/{user_id}")
async def calculate_transits(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime to calculate transits for, e.g. 1997-04-15T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if not chart:
        raise HTTPException(
            status_code=404,
            detail="Natal chart not found — call /calculate_natal_chart first",
        )
    dt = None
    if date:
        try:
            dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid date format: {date!r}. Use ISO format e.g. 1997-04-15T12:00:00")
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    try:
        transits = compute_transits(chart.positions, settings.zodiac_system, dt)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "user_id": user_id,
        "zodiac_system": settings.zodiac_system,
        "date": (dt or datetime.now(timezone.utc)).isoformat(),
        "transits": transits,
    }


@chart_router.get("/transit_positions/{user_id}")
async def get_transit_positions(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime to compute positions for, e.g. 2026-05-10T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="User not found")
    dt = None
    if date:
        try:
            dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid date format: {date!r}. Use ISO format e.g. 2026-05-10T12:00:00")
    dt = dt or datetime.now(timezone.utc)
    try:
        positions = compute_planet_positions(dt, settings.zodiac_system)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "user_id": user_id,
        "zodiac_system": settings.zodiac_system,
        "date": dt.isoformat(),
        "positions": positions,
    }
