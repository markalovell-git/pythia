from unittest.mock import patch

VALID_PAYLOAD = {
    "username": "jdoe",
    "name": "John Doe",
    "birth_datetime": "1990-06-15T08:30:00",
    "birth_timezone": "America/Chicago",
    "birth_location": "Chicago, IL",
    "birth_lat": 41.8781,
    "birth_lon": -87.6298,
}

UPDATED_PAYLOAD = {
    "name": "John Doe",
    "birth_datetime": "1990-06-15T08:30:00",
    "birth_timezone": "America/New_York",
    "birth_location": "New York, NY",
    "birth_lat": 40.7128,
    "birth_lon": -74.0060,
}

MOCK_POSITIONS = {
    "Sun": {"longitude": 84.50, "sign": "Gemini", "degree": 24.50},
}
MOCK_CHART_RETURN = (MOCK_POSITIONS, [i * 30.0 for i in range(12)])


def test_submit_user_data_success(client):
    response = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["user_data"]["username"] == "jdoe"
    assert "user_id" in data


def test_submit_user_data_default_house_system_is_placidus(client):
    response = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = response.json()["user_id"]
    settings = client.get(f"/api/get_user_settings/{user_id}").json()
    assert settings["house_system"] == "placidus"


def test_submit_user_data_with_whole_sign(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "house_system": "whole_sign"})
    user_id = response.json()["user_id"]
    settings = client.get(f"/api/get_user_settings/{user_id}").json()
    assert settings["house_system"] == "whole_sign"


def test_submit_user_data_invalid_house_system(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "house_system": "regiomontanus"})
    assert response.status_code == 422


def test_submit_user_data_duplicate_username(client):
    client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    response = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    assert response.status_code == 409


def test_submit_user_data_invalid_timezone(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "birth_timezone": "string"})
    assert response.status_code == 422


def test_submit_user_data_invalid_lat(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "birth_lat": 91.0})
    assert response.status_code == 422


def test_submit_user_data_invalid_negative_lat(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "birth_lat": -91.0})
    assert response.status_code == 422


def test_submit_user_data_invalid_lon(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "birth_lon": 181.0})
    assert response.status_code == 422


def test_submit_user_data_invalid_negative_lon(client):
    response = client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "birth_lon": -181.0})
    assert response.status_code == 422


def test_submit_user_data_boundary_lat_lon(client):
    for lat, lon in [(90.0, 180.0), (-90.0, -180.0), (0.0, 0.0)]:
        payload = {**VALID_PAYLOAD, "username": f"user_{lat}_{lon}", "birth_lat": lat, "birth_lon": lon}
        response = client.post("/api/submit_user_data", json=payload)
        assert response.status_code == 200, f"Expected valid for lat={lat}, lon={lon}"


def test_get_user_data_success(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]

    response = client.get(f"/api/get_user_data/{user_id}")
    assert response.status_code == 200
    data = response.json()["user_data"]
    assert data["username"] == "jdoe"
    assert data["name"] == "John Doe"
    assert data["birth_timezone"] == "America/Chicago"
    assert data["birth_location"] == "Chicago, IL"
    assert data["birth_lat"] == 41.8781
    assert data["birth_lon"] == -87.6298


def test_get_user_data_not_found(client):
    response = client.get("/api/get_user_data/nonexistent-uuid")
    assert response.status_code == 404


def test_get_user_by_username_success(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    expected_user_id = submit.json()["user_id"]

    response = client.get("/api/get_user_by_username/jdoe")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == expected_user_id
    assert data["name"] == "John Doe"
    assert data["birth_lat"] == 41.8781
    assert data["birth_lon"] == -87.6298


def test_get_user_by_username_not_found(client):
    response = client.get("/api/get_user_by_username/ghost")
    assert response.status_code == 404


def test_update_user_data_success(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]

    response = client.put(f"/api/update_user_data/{user_id}", json=UPDATED_PAYLOAD)
    assert response.status_code == 200

    data = client.get(f"/api/get_user_data/{user_id}").json()["user_data"]
    assert data["birth_timezone"] == "America/New_York"
    assert data["birth_location"] == "New York, NY"
    assert data["birth_lat"] == 40.7128


def test_update_user_data_not_found(client):
    response = client.put("/api/update_user_data/nonexistent-uuid", json=UPDATED_PAYLOAD)
    assert response.status_code == 404


def test_update_user_data_invalid_timezone(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]
    response = client.put(f"/api/update_user_data/{user_id}", json={**UPDATED_PAYLOAD, "birth_timezone": "bad/zone"})
    assert response.status_code == 422


def test_update_user_data_username_unchanged(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]
    client.put(f"/api/update_user_data/{user_id}", json=UPDATED_PAYLOAD)
    data = client.get(f"/api/get_user_data/{user_id}").json()["user_data"]
    assert data["username"] == "jdoe"


def test_update_user_data_invalidates_natal_chart(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]

    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{user_id}")

    assert client.get(f"/api/get_natal_chart/{user_id}").status_code == 200
    client.put(f"/api/update_user_data/{user_id}", json=UPDATED_PAYLOAD)
    assert client.get(f"/api/get_natal_chart/{user_id}").status_code == 404


def test_list_users_empty(client):
    response = client.get("/api/list_users")
    assert response.status_code == 200
    assert response.json() == []


def test_list_users_returns_all(client):
    client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    client.post("/api/submit_user_data", json={**VALID_PAYLOAD, "username": "jsmith", "name": "Jane Smith"})

    response = client.get("/api/list_users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    usernames = {u["username"] for u in data}
    assert usernames == {"jdoe", "jsmith"}


def test_list_users_fields(client):
    submit = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    user_id = submit.json()["user_id"]

    response = client.get("/api/list_users")
    user = response.json()[0]
    assert user["user_id"] == user_id
    assert user["username"] == "jdoe"
    assert user["name"] == "John Doe"
    assert "birth_lat" not in user


def test_delete_user_success(client, created_user):
    response = client.delete(f"/api/delete_user/{created_user}")
    assert response.status_code == 200
    assert client.get(f"/api/get_user_data/{created_user}").status_code == 404


def test_delete_user_not_found(client):
    response = client.delete("/api/delete_user/nonexistent-uuid")
    assert response.status_code == 404


def test_delete_user_removes_settings(client, created_user):
    client.delete(f"/api/delete_user/{created_user}")
    assert client.get(f"/api/get_user_settings/{created_user}").status_code == 404


def test_delete_user_removes_natal_chart(client, created_user):
    with patch("app.backend.chart_router.compute_natal_chart", return_value=MOCK_CHART_RETURN):
        client.post(f"/api/calculate_natal_chart/{created_user}")
    client.delete(f"/api/delete_user/{created_user}")
    assert client.get(f"/api/get_natal_chart/{created_user}").status_code == 404


def test_delete_user_frees_username(client, created_user):
    client.delete(f"/api/delete_user/{created_user}")
    response = client.post("/api/submit_user_data", json=VALID_PAYLOAD)
    assert response.status_code == 200


def test_list_users_after_delete(client, created_user):
    assert len(client.get("/api/list_users").json()) == 1
    client.delete(f"/api/delete_user/{created_user}")
    assert client.get("/api/list_users").json() == []
