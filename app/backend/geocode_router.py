from fastapi import APIRouter, HTTPException
import httpx

from app.astrology.geocode import geocode_location

geocode_router = APIRouter()


@geocode_router.get("/geocode")
async def geocode(q: str):
    if not q.strip():
        raise HTTPException(status_code=422, detail="Query string cannot be empty")
    try:
        result = geocode_location(q)
    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="Geocoding service unavailable")
    if result is None:
        raise HTTPException(status_code=404, detail=f"No location found for {q!r}")
    return result
