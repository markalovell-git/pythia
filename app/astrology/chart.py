from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from functools import lru_cache

from skyfield.api import Loader
from skyfield.framelib import ecliptic_frame

_DATA_DIR = Path(__file__).parent.parent.parent / "data"
_DATA_DIR.mkdir(exist_ok=True)
_loader = Loader(str(_DATA_DIR))

PLANETS = [
    ("Sun", "sun"),
    ("Moon", "moon"),
    ("Mercury", "mercury"),
    ("Venus", "venus"),
    ("Mars", "mars"),
    ("Jupiter", "jupiter barycenter"),
    ("Saturn", "saturn barycenter"),
    ("Uranus", "uranus barycenter"),
    ("Neptune", "neptune barycenter"),
    ("Pluto", "pluto barycenter"),
]

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]

ASPECTS = [
    ("conjunction", 0, 8),
    ("sextile", 60, 6),
    ("square", 90, 8),
    ("trine", 120, 8),
    ("opposition", 180, 8),
]

EPHEMERIS_MIN_YEAR = 1900
EPHEMERIS_MAX_YEAR = 2053

# Lahiri ayanamsa at J2000.0 and its annual rate (degrees)
_LAHIRI_J2000 = 23.853105
_LAHIRI_RATE = 0.013969


@lru_cache(maxsize=1)
def _load_ephemeris():
    return _loader("de421.bsp"), _loader.timescale(builtin=True)


def _lahiri_ayanamsa(tt: float) -> float:
    years_from_j2000 = (tt - 2451545.0) / 365.25
    return _LAHIRI_J2000 + _LAHIRI_RATE * years_from_j2000


def _longitude_to_sign(lon: float) -> tuple[str, float]:
    sign = SIGNS[int(lon / 30) % 12]
    degree = lon % 30
    return sign, round(degree, 4)


def _angular_difference(lon1: float, lon2: float) -> float:
    diff = abs(lon1 - lon2) % 360
    return diff if diff <= 180 else 360 - diff


def compute_planet_positions(dt_utc: datetime, zodiac_system: str) -> dict:
    """Return ecliptic positions for all tracked planets at a given UTC datetime."""
    if dt_utc.tzinfo is None:
        dt_utc = dt_utc.replace(tzinfo=timezone.utc)

    if not (EPHEMERIS_MIN_YEAR <= dt_utc.year <= EPHEMERIS_MAX_YEAR):
        raise ValueError(
            f"Date {dt_utc.date()} is outside the supported range "
            f"({EPHEMERIS_MIN_YEAR}–{EPHEMERIS_MAX_YEAR}). "
            f"A larger ephemeris (de441.bsp) would be required for dates outside this range."
        )

    planets, ts = _load_ephemeris()
    earth = planets["earth"]
    t = ts.from_datetime(dt_utc)
    positions = {}

    for name, body in PLANETS:
        astrometric = earth.at(t).observe(planets[body])
        _, lon, _ = astrometric.frame_latlon(ecliptic_frame)
        tropical_lon = lon.degrees % 360

        if zodiac_system == "sidereal":
            final_lon = (tropical_lon - _lahiri_ayanamsa(t.tt)) % 360
        else:
            final_lon = tropical_lon

        sign, degree = _longitude_to_sign(final_lon)
        positions[name] = {
            "longitude": round(final_lon, 4),
            "sign": sign,
            "degree": round(degree, 4),
        }

    # Mean North Node via standard formula (accurate to ~0.1°)
    T = (t.tt - 2451545.0) / 36525.0
    north_node_lon = (125.04452 - 1934.136261 * T) % 360
    if zodiac_system == "sidereal":
        north_node_lon = (north_node_lon - _lahiri_ayanamsa(t.tt)) % 360
    south_node_lon = (north_node_lon + 180.0) % 360

    for node_name, node_lon in [("North Node", north_node_lon), ("South Node", south_node_lon)]:
        sign, degree = _longitude_to_sign(node_lon)
        positions[node_name] = {
            "longitude": round(node_lon, 4),
            "sign": sign,
            "degree": round(degree, 4),
        }

    return positions


def compute_natal_chart(
    birth_datetime: datetime, birth_timezone: str, zodiac_system: str
) -> dict:
    """Compute natal planet positions from local birth time and timezone."""
    try:
        tz = ZoneInfo(birth_timezone)
    except ZoneInfoNotFoundError:
        raise ValueError(f"Unknown timezone in stored data: {birth_timezone!r}")
    dt_local = birth_datetime.replace(tzinfo=tz) if birth_datetime.tzinfo is None else birth_datetime.astimezone(tz)
    dt_utc = dt_local.astimezone(timezone.utc)
    return compute_planet_positions(dt_utc, zodiac_system)


def compute_transits(natal_positions: dict, zodiac_system: str, dt: datetime | None = None) -> list:
    """Compare sky positions at dt (defaults to now) against natal positions and return active aspects."""
    current_positions = compute_planet_positions(dt or datetime.now(timezone.utc), zodiac_system)

    transits = []
    for transit_planet, transit_data in current_positions.items():
        for natal_planet, natal_data in natal_positions.items():
            diff = _angular_difference(transit_data["longitude"], natal_data["longitude"])
            for aspect_name, angle, orb in ASPECTS:
                if abs(diff - angle) <= orb:
                    transits.append({
                        "transit_planet": transit_planet,
                        "natal_planet": natal_planet,
                        "aspect": aspect_name,
                        "orb": round(abs(diff - angle), 2),
                        "transit_position": transit_data,
                        "natal_position": natal_data,
                    })

    return sorted(transits, key=lambda x: x["orb"])
