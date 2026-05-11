from dataclasses import dataclass
from app.frontend import api_client

_ASPECT_ANGLES = {
    "conjunction": (0,   8),
    "sextile":     (60,  6),
    "square":      (90,  8),
    "trine":       (120, 8),
    "opposition":  (180, 8),
}


@dataclass
class PlanetPosition:
    longitude: float
    sign: str
    degree: float
    retrograde: bool = False


@dataclass
class ChartData:
    user_id: str
    zodiac_system: str
    positions: dict[str, PlanetPosition]
    computed_at: str
    house_cusps: list[float] | None = None


@dataclass
class Transit:
    transit_planet: str
    natal_planet: str
    aspect: str
    orb: float
    transit_position: PlanetPosition
    natal_position: PlanetPosition


@dataclass
class NatalAspect:
    planet1: str
    planet2: str
    aspect: str
    orb: float


@dataclass
class TransitData:
    date: str
    transits: list[Transit]


def load_chart(user_id: str) -> ChartData | None:
    raw = api_client.get_natal_chart(user_id)
    if not raw:
        return None
    return _parse_chart(raw)


def calculate_chart(user_id: str) -> ChartData:
    api_client.calculate_natal_chart(user_id)
    raw = api_client.get_natal_chart(user_id)
    return _parse_chart(raw)


def load_transits(user_id: str, date: str | None = None) -> TransitData:
    raw = api_client.calculate_transits(user_id, date=date)
    transits = [
        Transit(
            transit_planet=t["transit_planet"],
            natal_planet=t["natal_planet"],
            aspect=t["aspect"],
            orb=t["orb"],
            transit_position=PlanetPosition(**t["transit_position"]),
            natal_position=PlanetPosition(**t["natal_position"]),
        )
        for t in raw["transits"]
    ]
    transits.sort(key=lambda t: t.orb)
    return TransitData(date=raw["date"], transits=transits)


def load_transit_positions(user_id: str) -> ChartData | None:
    raw = api_client.get_transit_positions(user_id)
    if not raw:
        return None
    return ChartData(
        user_id=raw["user_id"],
        zodiac_system=raw["zodiac_system"],
        positions={name: PlanetPosition(**pos) for name, pos in raw["positions"].items()},
        computed_at=raw["date"],
    )


def get_zodiac_system(user_id: str) -> str:
    raw = api_client.get_user_settings(user_id)
    return raw["zodiac_system"] if raw else "sidereal"


def set_zodiac_system(user_id: str, zodiac_system: str) -> None:
    api_client.update_user_settings(user_id, zodiac_system)


def compute_natal_aspects(chart: ChartData) -> list[NatalAspect]:
    """Detect aspects between natal planets from their longitudes alone — no API call."""
    planets = list(chart.positions.items())
    results = []
    for i, (name1, pos1) in enumerate(planets):
        for name2, pos2 in planets[i + 1:]:
            diff = abs(pos1.longitude - pos2.longitude) % 360
            if diff > 180:
                diff = 360 - diff
            for aspect_name, (angle, orb) in _ASPECT_ANGLES.items():
                if abs(diff - angle) <= orb:
                    results.append(NatalAspect(
                        planet1=name1, planet2=name2,
                        aspect=aspect_name,
                        orb=round(abs(diff - angle), 2),
                    ))
                    break
    return sorted(results, key=lambda a: a.orb)


def get_house_number(longitude: float, cusps: list[float]) -> int | None:
    """Return 1-based Whole Sign house number for a longitude, or None."""
    if not cusps or len(cusps) != 12:
        return None
    for i in range(12):
        start = cusps[i]
        end   = cusps[(i + 1) % 12]
        if end > start:
            if start <= longitude < end:
                return i + 1
        else:
            if longitude >= start or longitude < end:
                return i + 1
    return 1


def _parse_chart(raw: dict) -> ChartData:
    return ChartData(
        user_id=raw["user_id"],
        zodiac_system=raw["zodiac_system"],
        positions={
            name: PlanetPosition(**pos) for name, pos in raw["positions"].items()
        },
        computed_at=raw["computed_at"],
        house_cusps=raw.get("house_cusps"),
    )
