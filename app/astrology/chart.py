import math
from pathlib import Path
from datetime import datetime, timezone, timedelta
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

ANGLE_NAMES = {"ASC", "DSC", "MC", "IC"}

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


def compute_angles_and_cusps(
    t, birth_lat: float, birth_lon: float, zodiac_system: str
) -> tuple[dict, list[float]]:
    """Return (angle_positions_dict, whole_sign_cusps) for the given birth location."""
    gast  = t.gast
    lst   = (gast + birth_lon / 15.0) % 24
    ramc  = (lst * 15.0) % 360
    T     = (t.tt - 2451545.0) / 36525.0
    obliquity = 23.439291111 - 0.013004167 * T
    eps    = math.radians(obliquity)
    phi    = math.radians(birth_lat)
    ramc_r = math.radians(ramc)

    mc_trop  = math.degrees(math.atan2(math.sin(ramc_r), math.cos(ramc_r) * math.cos(eps))) % 360
    asc_trop = math.degrees(math.atan2(
        -math.cos(ramc_r),
        math.sin(ramc_r) * math.cos(eps) + math.tan(phi) * math.sin(eps)
    )) % 360

    if zodiac_system == "sidereal":
        ayanamsa = _lahiri_ayanamsa(t.tt)
        asc = (asc_trop - ayanamsa) % 360
        mc  = (mc_trop  - ayanamsa) % 360
    else:
        asc, mc = asc_trop, mc_trop

    dsc = (asc + 180.0) % 360
    ic  = (mc  + 180.0) % 360

    h1    = int(asc // 30) * 30.0
    cusps = [(h1 + i * 30.0) % 360.0 for i in range(12)]

    angles = {}
    for name, lon in [("ASC", asc), ("DSC", dsc), ("MC", mc), ("IC", ic)]:
        sign, degree = _longitude_to_sign(lon)
        angles[name] = {
            "longitude": round(lon, 4),
            "sign":      sign,
            "degree":    round(degree, 4),
            "retrograde": False,
        }
    return angles, cusps


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
    t_next = ts.from_datetime(dt_utc + timedelta(days=1))
    positions = {}

    for name, body in PLANETS:
        astrometric = earth.at(t).observe(planets[body])
        _, lon, _ = astrometric.frame_latlon(ecliptic_frame)
        tropical_lon = lon.degrees % 360

        if zodiac_system == "sidereal":
            final_lon = (tropical_lon - _lahiri_ayanamsa(t.tt)) % 360
        else:
            final_lon = tropical_lon

        # Retrograde: ecliptic longitude decreasing over the next day
        _, lon_next, _ = earth.at(t_next).observe(planets[body]).frame_latlon(ecliptic_frame)
        tropical_lon_next = lon_next.degrees % 360
        if zodiac_system == "sidereal":
            final_lon_next = (tropical_lon_next - _lahiri_ayanamsa(t_next.tt)) % 360
        else:
            final_lon_next = tropical_lon_next
        retrograde = bool(((final_lon_next - final_lon + 180) % 360 - 180) < 0)

        sign, degree = _longitude_to_sign(final_lon)
        positions[name] = {
            "longitude": round(final_lon, 4),
            "sign": sign,
            "degree": round(degree, 4),
            "retrograde": retrograde,
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
            "retrograde": True,  # Mean Node always moves retrograde
        }

    return positions


def compute_natal_chart(
    birth_datetime: datetime,
    birth_timezone: str,
    zodiac_system: str,
    birth_lat: float,
    birth_lon: float,
) -> tuple[dict, list[float]]:
    """Compute natal positions (planets + angles) and Whole Sign house cusps."""
    try:
        tz = ZoneInfo(birth_timezone)
    except ZoneInfoNotFoundError:
        raise ValueError(f"Unknown timezone in stored data: {birth_timezone!r}")
    dt_local = birth_datetime.replace(tzinfo=tz) if birth_datetime.tzinfo is None else birth_datetime.astimezone(tz)
    dt_utc = dt_local.astimezone(timezone.utc)

    _, ts = _load_ephemeris()
    t = ts.from_datetime(dt_utc)

    positions = compute_planet_positions(dt_utc, zodiac_system)
    angles, cusps = compute_angles_and_cusps(t, birth_lat, birth_lon, zodiac_system)
    positions.update(angles)
    return positions, cusps


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
