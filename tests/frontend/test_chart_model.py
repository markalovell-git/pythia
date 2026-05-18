from app.frontend.models import chart_model

_RAW_CHART = {
    "user_id": "u1",
    "zodiac_system": "sidereal",
    "computed_at": "2026-05-09T12:00:00",
    "positions": {
        "Sun": {"longitude": 84.5, "sign": "Gemini", "degree": 24.5},
        "Moon": {"longitude": 120.0, "sign": "Leo", "degree": 0.0},
    },
}


def test_load_chart_parses_positions(mock_api):
    mock_api["get_natal_chart"].return_value = _RAW_CHART
    chart = chart_model.load_chart("u1")
    assert chart is not None
    assert chart.zodiac_system == "sidereal"
    assert chart.positions["Sun"].sign == "Gemini"
    assert chart.positions["Sun"].degree == 24.5


def test_load_chart_returns_none_when_missing(mock_api):
    mock_api["get_natal_chart"].return_value = None
    assert chart_model.load_chart("u1") is None


def test_load_transits_preserves_api_order(mock_api):
    # The backend now sorts by peak_score descending; the frontend preserves that order.
    # Simulate the API returning transits already ordered by peak_score (Saturn first).
    mock_api["calculate_transits"].return_value = {
        "date": "2026-05-09T12:00:00",
        "transits": [
            {
                "transit_planet": "Saturn", "natal_planet": "Sun",
                "aspect": "conjunction", "orb": 1.0,
                "transit_position": {"longitude": 85.5, "sign": "Gemini", "degree": 25.5},
                "natal_position": {"longitude": 84.5, "sign": "Gemini", "degree": 24.5},
                "score": 0.80, "peak_score": 0.85, "category": "major",
                "is_applying": True, "days_to_exact": 5.0, "speed": 0.034,
            },
            {
                "transit_planet": "Mars", "natal_planet": "Moon",
                "aspect": "trine", "orb": 3.5,
                "transit_position": {"longitude": 123.5, "sign": "Leo", "degree": 3.5},
                "natal_position": {"longitude": 120.0, "sign": "Leo", "degree": 0.0},
                "score": 0.30, "peak_score": 0.45, "category": "notable",
                "is_applying": False, "days_to_exact": -2.0, "speed": 0.5,
            },
        ],
    }
    data = chart_model.load_transits("u1")
    assert data.transits[0].transit_planet == "Saturn"
    assert data.transits[0].score == 0.80
    assert data.transits[0].peak_score == 0.85
    assert data.transits[0].category == "major"
    assert data.transits[0].is_applying is True
    assert data.transits[0].days_to_exact == 5.0
    assert data.transits[1].transit_planet == "Mars"
    assert data.transits[1].category == "notable"
    assert data.transits[1].is_applying is False


def test_get_zodiac_system(mock_api):
    mock_api["get_user_settings"].return_value = {"zodiac_system": "tropical"}
    assert chart_model.get_zodiac_system("u1") == "tropical"


def test_get_zodiac_system_fallback(mock_api):
    mock_api["get_user_settings"].return_value = None
    assert chart_model.get_zodiac_system("u1") == "sidereal"


def test_get_house_system(mock_api):
    mock_api["get_user_settings"].return_value = {"zodiac_system": "sidereal", "house_system": "whole_sign"}
    assert chart_model.get_house_system("u1") == "whole_sign"


def test_get_house_system_default_placidus(mock_api):
    mock_api["get_user_settings"].return_value = None
    assert chart_model.get_house_system("u1") == "placidus"


def test_get_house_system_missing_field_defaults_to_placidus(mock_api):
    # Backwards compatibility: an old settings payload may not include house_system
    mock_api["get_user_settings"].return_value = {"zodiac_system": "sidereal"}
    assert chart_model.get_house_system("u1") == "placidus"


def test_set_house_system_calls_api(mock_api):
    chart_model.set_house_system("u1", "whole_sign")
    mock_api["update_user_settings"].assert_called_once_with("u1", house_system="whole_sign")


def test_load_chart_includes_house_system(mock_api):
    mock_api["get_natal_chart"].return_value = {**_RAW_CHART, "house_system": "whole_sign"}
    chart = chart_model.load_chart("u1")
    assert chart.house_system == "whole_sign"


def test_load_chart_house_system_defaults_to_placidus(mock_api):
    mock_api["get_natal_chart"].return_value = _RAW_CHART  # no house_system field
    chart = chart_model.load_chart("u1")
    assert chart.house_system == "placidus"


# ── compute_natal_aspects ────────────────────────────────────────────────────

def _chart_with(**positions) -> chart_model.ChartData:
    return chart_model.ChartData(
        user_id="u1", zodiac_system="tropical", computed_at="2026-05-11T00:00:00",
        positions=positions,
    )


def test_compute_natal_aspects_detects_conjunction():
    chart = _chart_with(
        Mars=chart_model.PlanetPosition(longitude=0.0, sign="Aries", degree=0.0),
        Jupiter=chart_model.PlanetPosition(longitude=2.0, sign="Aries", degree=2.0),
    )
    aspects = chart_model.compute_natal_aspects(chart)
    assert len(aspects) == 1
    assert aspects[0].planet1 == "Mars"
    assert aspects[0].planet2 == "Jupiter"
    assert aspects[0].aspect == "conjunction"
    assert aspects[0].orb == 2.0


def test_compute_natal_aspects_skips_angle_angle_pairs():
    chart = _chart_with(
        ASC=chart_model.PlanetPosition(longitude=0.0,   sign="Aries", degree=0.0),
        DSC=chart_model.PlanetPosition(longitude=180.0, sign="Libra", degree=0.0),
    )
    assert chart_model.compute_natal_aspects(chart) == []


def test_compute_natal_aspects_planet_to_angle_is_included():
    chart = _chart_with(
        Sun=chart_model.PlanetPosition(longitude=0.0, sign="Aries", degree=0.0),
        ASC=chart_model.PlanetPosition(longitude=2.0, sign="Aries", degree=2.0),
    )
    aspects = chart_model.compute_natal_aspects(chart)
    assert len(aspects) == 1
    assert aspects[0].aspect == "conjunction"


def test_compute_natal_aspects_sorted_by_orb():
    # Mars-Saturn sextile orb=0.5; Mars-Jupiter square orb=5.0; Jupiter-Saturn ~34.5° apart (no aspect)
    chart = _chart_with(
        Mars=chart_model.PlanetPosition(longitude=0.0,  sign="Aries",  degree=0.0),
        Saturn=chart_model.PlanetPosition(longitude=60.5, sign="Gemini", degree=0.5),
        Jupiter=chart_model.PlanetPosition(longitude=95.0, sign="Cancer", degree=5.0),
    )
    aspects = chart_model.compute_natal_aspects(chart)
    assert len(aspects) == 2
    assert aspects[0].orb == 0.5
    assert aspects[1].orb == 5.0


def test_compute_natal_aspects_no_aspects_for_distant_planets():
    chart = _chart_with(
        Mars=chart_model.PlanetPosition(longitude=0.0,  sign="Aries",  degree=0.0),
        Jupiter=chart_model.PlanetPosition(longitude=45.0, sign="Taurus", degree=15.0),
    )
    assert chart_model.compute_natal_aspects(chart) == []


# ── load_sky_aspects ─────────────────────────────────────────────────────────

_RAW_SKY_ASPECTS = {
    "user_id": "u1",
    "date": "2026-05-11T12:00:00+00:00",
    "aspects": [
        {"planet1": "Mars", "planet2": "Jupiter", "aspect": "trine",  "orb": 1.5},
        {"planet1": "Sun",  "planet2": "Saturn",  "aspect": "square", "orb": 0.3},
    ],
}


def test_load_sky_aspects_sorted_by_orb(mock_api):
    mock_api["get_sky_aspects"].return_value = _RAW_SKY_ASPECTS
    aspects = chart_model.load_sky_aspects("u1")
    assert len(aspects) == 2
    assert aspects[0].orb == 0.3
    assert aspects[0].planet1 == "Sun"
    assert aspects[0].aspect == "square"
    assert aspects[1].orb == 1.5


def test_load_sky_aspects_returns_empty_list_when_api_returns_none(mock_api):
    mock_api["get_sky_aspects"].return_value = None
    assert chart_model.load_sky_aspects("u1") == []


def test_load_sky_aspects_passes_date_param(mock_api):
    mock_api["get_sky_aspects"].return_value = {
        "user_id": "u1", "date": "2025-01-01T00:00:00+00:00", "aspects": [],
    }
    chart_model.load_sky_aspects("u1", date="2025-01-01T00:00:00")
    mock_api["get_sky_aspects"].assert_called_once_with("u1", date="2025-01-01T00:00:00")
