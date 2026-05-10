from unittest.mock import patch
import httpx

MOCK_GEOCODE_RESULT = {
    "display_name": "Chicago, Cook County, Illinois, United States",
    "lat": 41.8781,
    "lon": -87.6298,
}


def test_geocode_success(client):
    with patch("app.backend.geocode_router.geocode_location", return_value=MOCK_GEOCODE_RESULT):
        response = client.get("/api/geocode", params={"q": "Chicago, IL"})
    assert response.status_code == 200
    data = response.json()
    assert data["lat"] == 41.8781
    assert data["lon"] == -87.6298
    assert "display_name" in data


def test_geocode_not_found(client):
    with patch("app.backend.geocode_router.geocode_location", return_value=None):
        response = client.get("/api/geocode", params={"q": "xyzzy nowhere"})
    assert response.status_code == 404


def test_geocode_empty_query(client):
    response = client.get("/api/geocode", params={"q": "   "})
    assert response.status_code == 422


def test_geocode_network_error(client):
    with patch("app.backend.geocode_router.geocode_location", side_effect=httpx.ConnectError("timeout")):
        response = client.get("/api/geocode", params={"q": "Chicago, IL"})
    assert response.status_code == 503


def test_geocode_malformed_response(client):
    with patch("app.backend.geocode_router.geocode_location", return_value=None):
        response = client.get("/api/geocode", params={"q": "somewhere"})
    assert response.status_code == 404
