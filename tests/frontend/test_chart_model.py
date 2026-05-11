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
