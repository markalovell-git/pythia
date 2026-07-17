from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.common.database import get_db, UserData, UserSettings, NatalChart
from app.common.astro_utils import house_number as _house_number
from app.astrology.chart import compute_natal_chart, compute_transits, compute_planet_positions, compute_sky_aspects, compute_transit_windows, compute_sky_windows
from app.astrology.scoring import score_transit, categorize, get_timescale, DEFAULT_CONFIG

chart_router = APIRouter()

_ASC_SIGN_RULERS = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury",
    "Cancer": "Moon", "Leo": "Sun", "Virgo": "Mercury",
    "Libra": "Venus", "Scorpio": "Pluto", "Sagittarius": "Jupiter",
    "Capricorn": "Saturn", "Aquarius": "Uranus", "Pisces": "Neptune",
}


def _chart_ruler(asc_sign: str | None) -> str | None:
    return _ASC_SIGN_RULERS.get(asc_sign) if asc_sign else None


def _parse_date_param(date: str | None) -> datetime | None:
    """Parse an optional ISO date query param to an aware UTC datetime.

    Naive inputs are assumed to be UTC; offset-aware inputs are converted.
    """
    if not date:
        return None
    try:
        dt = datetime.fromisoformat(date)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid date format: {date!r}. Use ISO format e.g. 1997-04-15T12:00:00",
        )
    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt.astimezone(timezone.utc)


def _get_settings_or_404(user_id: str, db: Session) -> UserSettings:
    settings = db.query(UserSettings).filter(UserSettings.user_id == user_id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="User not found")
    return settings



@chart_router.post("/calculate_natal_chart/{user_id}")
async def calculate_natal_chart(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserData).filter(UserData.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    settings = _get_settings_or_404(user_id, db)
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
    settings = _get_settings_or_404(user_id, db)
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
    dt = _parse_date_param(date)
    settings = _get_settings_or_404(user_id, db)
    try:
        transits = compute_transits(chart.positions, settings.zodiac_system, dt)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    asc_data = chart.positions.get("ASC") or {}
    ruler = _chart_ruler(asc_data.get("sign"))
    for t in transits:
        natal_house = _house_number(t["transit_position"]["longitude"], chart.house_cusps)
        result = score_transit(
            t["transit_planet"], t["natal_planet"], t["aspect"], t["orb"],
            t.get("is_applying", True), t.get("speed"),
            natal_house, ruler, DEFAULT_CONFIG,
        )
        if result is not None:
            t["score"], t["peak_score"] = result
        else:
            t["score"] = t["peak_score"] = 0.0
        t["category"] = categorize(t["score"], DEFAULT_CONFIG)
        t["timescale"] = get_timescale(t["transit_planet"], DEFAULT_CONFIG)

    transits.sort(key=lambda x: x["peak_score"], reverse=True)

    return {
        "user_id": user_id,
        "zodiac_system": settings.zodiac_system,
        "date": (dt or datetime.now(timezone.utc)).isoformat(),
        "transits": transits,
    }


@chart_router.get("/transit_windows/{user_id}")
async def get_transit_windows(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime to center the 12-month scan on, e.g. 2026-05-17T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    chart = db.query(NatalChart).filter(NatalChart.user_id == user_id).first()
    if not chart:
        raise HTTPException(status_code=404, detail="Natal chart not found — call /calculate_natal_chart first")
    dt = _parse_date_param(date)
    settings = _get_settings_or_404(user_id, db)
    try:
        windows = compute_transit_windows(chart.positions, settings.zodiac_system, dt)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "user_id": user_id,
        "date": (dt or datetime.now(timezone.utc)).isoformat(),
        "windows": windows,
    }


@chart_router.get("/sky_aspects/{user_id}")
async def get_sky_aspects(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime, e.g. 2026-05-11T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    settings = _get_settings_or_404(user_id, db)
    dt = _parse_date_param(date) or datetime.now(timezone.utc)
    try:
        aspects = compute_sky_aspects(settings.zodiac_system, dt)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "user_id": user_id,
        "date": dt.isoformat(),
        "aspects": aspects,
    }


@chart_router.get("/sky_windows/{user_id}")
async def get_sky_windows(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime to center the 12-month scan on, e.g. 2026-05-17T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    settings = _get_settings_or_404(user_id, db)
    dt = _parse_date_param(date)
    try:
        windows = compute_sky_windows(settings.zodiac_system, dt)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return {
        "user_id": user_id,
        "date": (dt or datetime.now(timezone.utc)).isoformat(),
        "windows": windows,
    }


@chart_router.get("/transit_positions/{user_id}")
async def get_transit_positions(
    user_id: str,
    date: str | None = Query(None, description="ISO datetime to compute positions for, e.g. 2026-05-10T12:00:00. Defaults to now."),
    db: Session = Depends(get_db),
):
    settings = _get_settings_or_404(user_id, db)
    dt = _parse_date_param(date) or datetime.now(timezone.utc)
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
