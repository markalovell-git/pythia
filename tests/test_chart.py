from unittest.mock import patch

from app.astrology.chart import compute_sky_aspects

MOCK_POSITIONS = {
    "Sun":     {"longitude": 84.50,  "sign": "Gemini",    "degree": 24.50},
    "Moon":    {"longitude": 234.20, "sign": "Scorpio",   "degree": 24.20},
    "Mercury": {"longitude": 76.30,  "sign": "Gemini",    "degree": 16.30},
    "Venus":   {"longitude": 61.80,  "sign": "Taurus",    "degree": 1.80},
    "Mars":    {"longitude": 187.40, "sign": "Libra",     "degree": 7.40},
    "Jupiter": {"longitude": 99.10,  "sign": "Cancer",    "degree": 9.10},
    "Saturn":  {"longitude": 305.20, "sign": "Aquarius",  "degree": 5.20},
    "Uranus":  {"longitude": 280.60, "sign": "Capricorn", "degree": 10.60},
    "Neptune": {"longitude": 285.10, "sign": "Capricorn", "degree": 15.10},
    "Pluto":   {"longitude": 234.80, "sign": "Scorpio",   "degree": 24.80},
}
MOCK_CUSPS = [i * 30.0 for i in range(12)]
MOCK_CHART_RETURN = (MOCK_POSITIONS, MOCK_CUSPS)

MOCK_TRANSITS = [
    {
        "transit_planet": "Mars",
        "natal_planet": "Sun",
        "aspect": "conjunction",
        "orb": 2.3,
        "transit_position": {"longitude": 86.80, "sign": "Gemini", "degree": 26.80},
        "natal_position":   {"longitude": 84.50, "sign": "Gemini", "degree": 24.50},
    }
]


def test_calculate_natal_chart_success(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        response = client.post(f"/api/calculate_natal_chart/{created_user}")
    assert response.status_code == 200
    data = response.json()
    assert data["zodiac_system"] == "sidereal"
    assert "Sun" in data["positions"]
    assert data["positions"]["Sun"]["sign"] == "Gemini"


def test_calculate_natal_chart_user_not_found(client):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        response = client.post("/api/calculate_natal_chart/nonexistent-uuid")
    assert response.status_code == 404


def test_calculate_natal_chart_overwrites_previous(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
        response = client.post(f"/api/calculate_natal_chart/{created_user}")
    assert response.status_code == 200


def test_calculate_natal_chart_out_of_range_birth_date(client):
    response = client.post("/api/submit_user_data", json={
        "username": "olduser",
        "name": "Old User",
        "birth_datetime": "1850-03-15T12:00:00",
        "birth_timezone": "Europe/London",
        "birth_location": "London, UK",
        "birth_lat": 51.5074,
        "birth_lon": -0.1278,
    })
    user_id = response.json()["user_id"]
    response = client.post(f"/api/calculate_natal_chart/{user_id}")
    assert response.status_code == 422
    assert "1900" in response.json()["detail"]


def test_get_natal_chart_success(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    response = client.get(f"/api/get_natal_chart/{created_user}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == created_user
    assert "positions" in data
    assert "computed_at" in data


def test_get_natal_chart_not_found(client, created_user):
    response = client.get(f"/api/get_natal_chart/{created_user}")
    assert response.status_code == 404


def test_calculate_transits_success(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS):
        response = client.get(f"/api/calculate_transits/{created_user}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == created_user
    assert "date" in data
    assert len(data["transits"]) == 1
    assert data["transits"][0]["aspect"] == "conjunction"


def test_calculate_transits_no_natal_chart(client, created_user):
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS):
        response = client.get(f"/api/calculate_transits/{created_user}")
    assert response.status_code == 404


def test_calculate_transits_with_past_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS) as mock:
        response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "1997-04-15T12:00:00"})
    assert response.status_code == 200
    assert "1997-04-15" in response.json()["date"]
    assert mock.call_args[0][2].year == 1997


def test_calculate_transits_with_future_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS) as mock:
        response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "2044-06-15T12:00:00"})
    assert response.status_code == 200
    assert mock.call_args[0][2].year == 2044


def test_calculate_transits_invalid_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "not-a-date"})
    assert response.status_code == 422


def test_calculate_transits_out_of_range_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "1850-01-01T00:00:00"})
    assert response.status_code == 422
    assert "range" in response.json()["detail"].lower()


MOCK_SKY_ASPECTS = [
    {
        "planet1": "Mars", "planet2": "Jupiter", "aspect": "trine", "orb": 1.5,
        "position1": {"longitude": 120.0, "sign": "Leo",   "degree": 0.0, "retrograde": False},
        "position2": {"longitude": 0.0,   "sign": "Aries", "degree": 0.0, "retrograde": False},
    }
]

_CONJUNCTION_POSITIONS = {
    "Mars":    {"longitude": 0.0, "sign": "Aries", "degree": 0.0, "retrograde": False},
    "Jupiter": {"longitude": 2.0, "sign": "Aries", "degree": 2.0, "retrograde": False},
}

_NODE_PAIR_POSITIONS = {
    "North Node": {"longitude": 0.0,   "sign": "Aries", "degree": 0.0, "retrograde": True},
    "South Node": {"longitude": 180.0, "sign": "Libra", "degree": 0.0, "retrograde": True},
}

_TWO_ASPECT_POSITIONS = {
    "Mars":    {"longitude": 0.0,  "sign": "Aries",      "degree": 0.0, "retrograde": False},
    "Saturn":  {"longitude": 60.5, "sign": "Gemini",     "degree": 0.5, "retrograde": False},
    "Jupiter": {"longitude": 95.0, "sign": "Cancer",     "degree": 5.0, "retrograde": False},
}

_NO_ASPECT_POSITIONS = {
    "Mars":    {"longitude": 0.0,  "sign": "Aries",  "degree": 0.0,  "retrograde": False},
    "Jupiter": {"longitude": 45.0, "sign": "Taurus", "degree": 15.0, "retrograde": False},
}


# ── Unit tests: compute_sky_aspects ──────────────────────────────────────────

def test_compute_sky_aspects_detects_conjunction():
    with patch("app.astrology.chart.compute_planet_positions", return_value=_CONJUNCTION_POSITIONS):
        aspects = compute_sky_aspects("tropical")
    assert len(aspects) == 1
    assert aspects[0]["planet1"] == "Mars"
    assert aspects[0]["planet2"] == "Jupiter"
    assert aspects[0]["aspect"] == "conjunction"
    assert aspects[0]["orb"] == 2.0


def test_compute_sky_aspects_excludes_north_south_node_pair():
    with patch("app.astrology.chart.compute_planet_positions", return_value=_NODE_PAIR_POSITIONS):
        aspects = compute_sky_aspects("tropical")
    assert aspects == []


def test_compute_sky_aspects_sorted_by_orb():
    with patch("app.astrology.chart.compute_planet_positions", return_value=_TWO_ASPECT_POSITIONS):
        aspects = compute_sky_aspects("tropical")
    # Mars-Saturn sextile orb=0.5; Mars-Jupiter square orb=5.0; Jupiter-Saturn is ~34.5° apart (no aspect)
    assert len(aspects) == 2
    assert aspects[0]["orb"] == 0.5
    assert aspects[1]["orb"] == 5.0


def test_compute_sky_aspects_no_aspects_for_distant_planets():
    with patch("app.astrology.chart.compute_planet_positions", return_value=_NO_ASPECT_POSITIONS):
        aspects = compute_sky_aspects("tropical")
    assert aspects == []


# ── Endpoint tests: GET /sky_aspects/{user_id} ────────────────────────────────

def test_sky_aspects_success(client, created_user):
    with patch("app.backend.chart_router.compute_sky_aspects", return_value=MOCK_SKY_ASPECTS):
        response = client.get(f"/api/sky_aspects/{created_user}")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == created_user
    assert "date" in data
    assert len(data["aspects"]) == 1
    assert data["aspects"][0]["aspect"] == "trine"


def test_sky_aspects_user_not_found(client):
    with patch("app.backend.chart_router.compute_sky_aspects", return_value=MOCK_SKY_ASPECTS):
        response = client.get("/api/sky_aspects/nonexistent-uuid")
    assert response.status_code == 404


def test_sky_aspects_with_date(client, created_user):
    with patch("app.backend.chart_router.compute_sky_aspects", return_value=MOCK_SKY_ASPECTS) as mock:
        response = client.get(f"/api/sky_aspects/{created_user}", params={"date": "2024-03-20T12:00:00"})
    assert response.status_code == 200
    assert "2024-03-20" in response.json()["date"]
    assert mock.call_args[0][1].year == 2024


def test_sky_aspects_invalid_date(client, created_user):
    response = client.get(f"/api/sky_aspects/{created_user}", params={"date": "not-a-date"})
    assert response.status_code == 422


def test_sky_aspects_out_of_range_date(client, created_user):
    response = client.get(f"/api/sky_aspects/{created_user}", params={"date": "1850-01-01T00:00:00"})
    assert response.status_code == 422
    assert "range" in response.json()["detail"].lower()
