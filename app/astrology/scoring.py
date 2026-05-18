import math

DEFAULT_CONFIG = {
    "transiting_planet_weights": {
        "Pluto": 1.0, "Neptune": 1.0, "Uranus": 1.0,
        "Saturn": 0.9, "Jupiter": 0.8, "Chiron": 0.7,
        "Mars": 0.5, "Sun": 0.4, "North Node": 0.4, "South Node": 0.4,
        "Venus": 0.3, "Mercury": 0.3, "Moon": 0.1,
    },
    "natal_point_weights": {
        "Sun": 1.0, "Moon": 1.0, "ASC": 1.0, "MC": 1.0,
        "DSC": 0.8, "IC": 0.8,
        "Mercury": 0.7, "Venus": 0.7, "Mars": 0.7,
        "Jupiter": 0.5, "Saturn": 0.5,
        "North Node": 0.6, "South Node": 0.6,
        "Uranus": 0.3, "Neptune": 0.3, "Pluto": 0.3,
    },
    "aspect_weights": {
        "conjunction": 1.0, "opposition": 0.9, "square": 0.9,
        "trine": 0.8, "sextile": 0.6, "quincunx": 0.4,
    },
    "max_orbs": {
        "conjunction": 8, "opposition": 8, "square": 7,
        "trine": 7, "sextile": 5,
    },
    "applying_bonus": 1.15,
    "categories": [(0.7, "major"), (0.4, "notable"), (0.2, "minor"), (0.0, "background")],
    "timescales": {
        "long":   {"Pluto", "Neptune", "Uranus", "Saturn"},
        "medium": {"Jupiter", "Mars"},
        "short":  {"Sun", "Mercury", "Venus"},
        "daily":  {"Moon"},
    },
    "fast_planets": {"Moon", "Mercury", "Venus", "Sun"},
    "station_threshold": 0.05,
    "normal_speeds": {
        "Saturn": 0.034, "Jupiter": 0.083, "Mars": 0.524,
        "Uranus": 0.012, "Neptune": 0.006, "Pluto": 0.004,
    },
}

_ANGULAR_HOUSE_BONUS   = 1.10
_SUCCEDENT_HOUSE_BONUS = 1.00
_CADENT_HOUSE_BONUS    = 0.95


def score_transit(
    transiting_planet: str,
    natal_point: str,
    aspect_type: str,
    orb: float,
    is_applying: bool,
    speed: float | None,
    natal_house: int | None,
    chart_ruler: str | None,
    config: dict,
) -> tuple[float, float] | None:
    """Return (current_score, peak_score), or None if filtered out."""
    max_orb = config["max_orbs"].get(aspect_type)
    if max_orb is None:
        return None

    fast_planets = config["fast_planets"]
    effective_max_orb = max_orb / 2 if transiting_planet in fast_planets else max_orb

    if orb > effective_max_orb:
        return None

    orb_strength = math.cos((orb / effective_max_orb) * (math.pi / 2))

    t_weight = config["transiting_planet_weights"].get(transiting_planet, 0.3)
    n_weight = config["natal_point_weights"].get(natal_point, 0.3)
    a_weight = config["aspect_weights"].get(aspect_type, 0.3)

    if chart_ruler and natal_point == chart_ruler:
        n_weight = min(1.0, n_weight + 0.2)

    applying_bonus = config["applying_bonus"] if is_applying else 1.0

    station_bonus = 1.0
    if speed is not None and transiting_planet in config["normal_speeds"]:
        normal_speed = config["normal_speeds"][transiting_planet]
        if abs(speed) < config["station_threshold"]:
            station_bonus = min(1.5, 1.0 + (1.0 - abs(speed) / normal_speed) * 0.5)

    if natal_house in (1, 4, 7, 10):
        house_bonus = _ANGULAR_HOUSE_BONUS
    elif natal_house in (2, 5, 8, 11):
        house_bonus = _SUCCEDENT_HOUSE_BONUS
    elif natal_house in (3, 6, 9, 12):
        house_bonus = _CADENT_HOUSE_BONUS
    else:
        house_bonus = 1.0

    base_score = t_weight * n_weight * a_weight * applying_bonus * station_bonus * house_bonus
    current_score = round(orb_strength * base_score, 3)
    peak_score = round(base_score, 3)
    return current_score, peak_score


def categorize(score: float, config: dict) -> str:
    for threshold, label in config["categories"]:
        if score >= threshold:
            return label
    return "background"


def get_timescale(planet: str, config: dict) -> str:
    for label, planets in config["timescales"].items():
        if planet in planets:
            return label
    return "other"
