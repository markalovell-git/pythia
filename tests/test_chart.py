from unittest.mock import patch

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
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        response = client.post(f"/api/calculate_natal_chart/{created_user}")
    assert response.status_code == 200
    data = response.json()
    assert data["zodiac_system"] == "sidereal"
    assert "Sun" in data["positions"]
    assert data["positions"]["Sun"]["sign"] == "Gemini"


def test_calculate_natal_chart_user_not_found(client):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        response = client.post("/api/calculate_natal_chart/nonexistent-uuid")
    assert response.status_code == 404


def test_calculate_natal_chart_overwrites_previous(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
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
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
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
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
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
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS) as mock:
        response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "1997-04-15T12:00:00"})
    assert response.status_code == 200
    assert "1997-04-15" in response.json()["date"]
    assert mock.call_args[0][2].year == 1997


def test_calculate_transits_with_future_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    with patch("app.backend.chart_router.compute_transits", return_value=MOCK_TRANSITS) as mock:
        response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "2044-06-15T12:00:00"})
    assert response.status_code == 200
    assert mock.call_args[0][2].year == 2044


def test_calculate_transits_invalid_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "not-a-date"})
    assert response.status_code == 422


def test_calculate_transits_out_of_range_date(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    response = client.get(f"/api/calculate_transits/{created_user}", params={"date": "1850-01-01T00:00:00"})
    assert response.status_code == 422
    assert "range" in response.json()["detail"].lower()
