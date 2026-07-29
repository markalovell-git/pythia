from dataclasses import dataclass
from app.frontend import api_client


@dataclass
class Location:
    location_id: str
    name: str
    latitude: float | None = None
    longitude: float | None = None
    timezone: str | None = None


def search_locations(q: str = "") -> list[Location]:
    return [Location(**r) for r in api_client.get_locations(q)]


def create_location(
    name: str,
    latitude: float | None = None,
    longitude: float | None = None,
    timezone: str | None = None,
) -> Location:
    raw = api_client.create_location({
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
    })
    return Location(**raw)
