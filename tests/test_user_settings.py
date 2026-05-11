from unittest.mock import patch

MOCK_POSITIONS = {
    "Sun": {"longitude": 84.50, "sign": "Gemini", "degree": 24.50},
}
MOCK_CHART_RETURN = (MOCK_POSITIONS, [i * 30.0 for i in range(12)])


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
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")

    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 200
    client.put(f"/api/update_user_settings/{created_user}", json={"zodiac_system": "tropical"})
    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 404


# ── house_system ──────────────────────────────────────────────────────────────

def test_settings_includes_house_system_with_default(client, created_user):
    response = client.get(f"/api/get_user_settings/{created_user}")
    assert response.status_code == 200
    assert response.json()["house_system"] == "placidus"


def test_update_house_system_to_whole_sign(client, created_user):
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"house_system": "whole_sign"},
    )
    assert response.status_code == 200
    assert response.json()["house_system"] == "whole_sign"


def test_update_house_system_invalid(client, created_user):
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"house_system": "koch"},
    )
    assert response.status_code == 422


def test_update_both_settings_in_one_request(client, created_user):
    response = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"zodiac_system": "tropical", "house_system": "whole_sign"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["zodiac_system"] == "tropical"
    assert body["house_system"] == "whole_sign"


def test_update_zodiac_alone_preserves_house_system(client, created_user):
    client.put(f"/api/update_user_settings/{created_user}", json={"house_system": "whole_sign"})
    client.put(f"/api/update_user_settings/{created_user}", json={"zodiac_system": "tropical"})
    response = client.get(f"/api/get_user_settings/{created_user}")
    assert response.json()["house_system"] == "whole_sign"
    assert response.json()["zodiac_system"] == "tropical"


def test_house_system_change_invalidates_natal_chart(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 200
    client.put(f"/api/update_user_settings/{created_user}", json={"house_system": "whole_sign"})
    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 404
