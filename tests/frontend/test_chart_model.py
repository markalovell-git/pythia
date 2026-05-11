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


def test_load_transits_sorted_by_orb(mock_api):
    mock_api["calculate_transits"].return_value = {
        "date": "2026-05-09T12:00:00",
        "transits": [
            {
                "transit_planet": "Mars", "natal_planet": "Sun",
                "aspect": "square", "orb": 3.5,
                "transit_position": {"longitude": 90.0, "sign": "Cancer", "degree": 0.0},
                "natal_position": {"longitude": 84.5, "sign": "Gemini", "degree": 24.5},
            },
            {
                "transit_planet": "Jupiter", "natal_planet": "Moon",
                "aspect": "trine", "orb": 1.2,
                "transit_position": {"longitude": 121.2, "sign": "Leo", "degree": 1.2},
                "natal_position": {"longitude": 120.0, "sign": "Leo", "degree": 0.0},
            },
        ],
    }
    data = chart_model.load_transits("u1")
    assert data.transits[0].orb == 1.2
    assert data.transits[1].orb == 3.5


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
