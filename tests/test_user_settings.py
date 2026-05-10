from unittest.mock import patch

MOCK_POSITIONS = {
    "Sun": {"longitude": 84.50, "sign": "Gemini", "degree": 24.50},
}


def test_settings_created_with_defaults(client, created_user):
    response = client.get(f"/api/get_user_settings/{created_user}")
    assert response.status_code == 200
    assert response.json()["zodiac_system"] == "sidereal"


def test_update_zodiac_system_to_tropical(client, created_user):
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"zodiac_system": "tropical"},
    )
    assert response.status_code == 200
    assert response.json()["zodiac_system"] == "tropical"


def test_update_zodiac_system_back_to_sidereal(client, created_user):
    client.put(f"/api/update_user_settings/{created_user}", json={"zodiac_system": "tropical"})
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"zodiac_system": "sidereal"},
    )
    assert response.status_code == 200
    assert response.json()["zodiac_system"] == "sidereal"


def test_update_zodiac_system_invalid(client, created_user):
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"zodiac_system": "galactic"},
    )
    assert response.status_code == 422


def test_get_user_settings_not_found(client):
    response = client.get("/api/get_user_settings/nonexistent-uuid")
    assert response.status_code == 404


def test_update_user_settings_not_found(client):
    response = client.put(
        "/api/update_user_settings/nonexistent-uuid",
        json={"zodiac_system": "tropical"},
    )
    assert response.status_code == 404


def test_zodiac_change_invalidates_natal_chart(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_POSITIONS):
        client.post(f"/api/calculate_natal_chart/{created_user}")

    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 200
    client.put(f"/api/update_user_settings/{created_user}", json={"zodiac_system": "tropical"})
    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 404
