from dataclasses import dataclass
from app.frontend import api_client

_ANGLE_NAMES = {"ASC", "DSC", "MC", "IC"}

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
    house_system: str = "placidus"


@dataclass
class Transit:
    transit_planet: str
    natal_planet: str
    aspect: str
    orb: float
    transit_position: PlanetPosition
    natal_position: PlanetPosition
    score: float = 0.0
    peak_score: float = 0.0
    category: str = "background"
    is_applying: bool = True
    days_to_exact: float | None = None
    speed: float | None = None


@dataclass
class TransitWindow:
    start: str  # "YYYY-MM-DD"
    end: str    # "YYYY-MM-DD"


@dataclass
class SkyWindowResult:
    planet1: str
    planet2: str
    aspect: str
    windows: list[TransitWindow]


@dataclass
class TransitWindowResult:
    transit_planet: str
    natal_planet: str
    aspect: str
    windows: list[TransitWindow]


@dataclass
class Aspect:
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
            transit_position=PlanetPosition(**{
                k: v for k, v in t["transit_position"].items()
                if k in ("longitude", "sign", "degree", "retrograde")
            }),
            natal_position=PlanetPosition(**{
                k: v for k, v in t["natal_position"].items()
                if k in ("longitude", "sign", "degree", "retrograde")
            }),
            score=t.get("score", 0.0),
            peak_score=t.get("peak_score", 0.0),
            category=t.get("category", "background"),
            is_applying=t.get("is_applying", True),
            days_to_exact=t.get("days_to_exact"),
            speed=t.get("speed"),
        )
        for t in raw["transits"]
    ]
    return TransitData(date=raw["date"], transits=transits)


def format_transit_dates(windows: list[TransitWindow]) -> str:
    """Format transit windows as e.g. 'Apr 28–May 15' or 'Apr 1–15,  May 3–20' (retrograde loop)."""
    from datetime import datetime as _dt
    parts = []
    for w in windows:
        s = _dt.strptime(w.start, "%Y-%m-%d")
        e = _dt.strptime(w.end, "%Y-%m-%d")
        if s.year != e.year:
            parts.append(f"{s.strftime('%b %-d %Y')}–{e.strftime('%b %-d %Y')}")
        elif s.month == e.month:
            parts.append(f"{s.strftime('%b %-d')}–{e.strftime('%-d')}")
        else:
            parts.append(f"{s.strftime('%b %-d')}–{e.strftime('%b %-d')}")
    return ",  ".join(parts)


def load_sky_windows(user_id: str, date: str | None = None) -> list[SkyWindowResult]:
    raw = api_client.get_sky_windows(user_id, date=date)
    if not raw:
        return []
    return [
        SkyWindowResult(
            planet1=r["planet1"],
            planet2=r["planet2"],
            aspect=r["aspect"],
            windows=[TransitWindow(**w) for w in r["windows"]],
        )
        for r in raw["windows"]
    ]


def load_transit_windows(user_id: str, date: str | None = None) -> list[TransitWindowResult]:
    raw = api_client.get_transit_windows(user_id, date=date)
    if not raw:
        return []
    return [
        TransitWindowResult(
            transit_planet=r["transit_planet"],
            natal_planet=r["natal_planet"],
            aspect=r["aspect"],
            windows=[TransitWindow(**w) for w in r["windows"]],
        )
        for r in raw["windows"]
    ]


def load_sky_aspects(user_id: str, date: str | None = None) -> list[Aspect]:
    raw = api_client.get_sky_aspects(user_id, date=date)
    if not raw:
        return []
    return sorted(
        [Aspect(planet1=a["planet1"], planet2=a["planet2"], aspect=a["aspect"], orb=a["orb"])
         for a in raw["aspects"]],
        key=lambda a: a.orb,
    )


def load_transit_positions(user_id: str) -> ChartData | None:
    raw = api_client.get_transit_positions(user_id)
    if not raw:
        return None
    return ChartData(
        user_id=raw["user_id"],
        zodiac_system=raw["zodiac_system"],
        positions={
            name: PlanetPosition(**{k: v for k, v in pos.items() if k in _PLANET_POSITION_KEYS})
            for name, pos in raw["positions"].items()
        },
        computed_at=raw["date"],
    )


def get_zodiac_system(user_id: str) -> str:
    raw = api_client.get_user_settings(user_id)
    return raw["zodiac_system"] if raw else "sidereal"


def set_zodiac_system(user_id: str, zodiac_system: str) -> None:
    api_client.update_user_settings(user_id, zodiac_system=zodiac_system)


def get_house_system(user_id: str) -> str:
    raw = api_client.get_user_settings(user_id)
    return raw.get("house_system", "placidus") if raw else "placidus"


def set_house_system(user_id: str, house_system: str) -> None:
    api_client.update_user_settings(user_id, house_system=house_system)


def compute_natal_aspects(chart: ChartData) -> list[Aspect]:
    """Detect aspects between natal planets from their longitudes alone — no API call."""
    planets = list(chart.positions.items())
    results = []
    for i, (name1, pos1) in enumerate(planets):
        for name2, pos2 in planets[i + 1:]:
            if name1 in _ANGLE_NAMES and name2 in _ANGLE_NAMES:
                continue
            diff = abs(pos1.longitude - pos2.longitude) % 360
            if diff > 180:
                diff = 360 - diff
            for aspect_name, (angle, orb) in _ASPECT_ANGLES.items():
                if abs(diff - angle) <= orb:
                    results.append(Aspect(
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


_PLANET_POSITION_KEYS = {"longitude", "sign", "degree", "retrograde"}


def _parse_chart(raw: dict) -> ChartData:
    return ChartData(
        user_id=raw["user_id"],
        zodiac_system=raw["zodiac_system"],
        positions={
            name: PlanetPosition(**{k: v for k, v in pos.items() if k in _PLANET_POSITION_KEYS})
            for name, pos in raw["positions"].items()
        },
        computed_at=raw["computed_at"],
        house_cusps=raw.get("house_cusps"),
        house_system=raw.get("house_system", "placidus"),
    )
