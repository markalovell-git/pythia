import httpx

_NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
_USER_AGENT = "AstrologyApp/0.1"


def geocode_location(query: str) -> dict | None:
    response = httpx.get(
        _NOMINATIM_URL,
        params={"q": query, "format": "json", "limit": 1},
        headers={"User-Agent": _USER_AGENT},
        timeout=10.0,
    )
    response.raise_for_status()
    results = response.json()
    if not results:
        return None
    result = results[0]
    try:
        return {
            "display_name": result["display_name"],
            "lat": float(result["lat"]),
            "lon": float(result["lon"]),
        }
    except (KeyError, ValueError):
        return None
