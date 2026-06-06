def test_history_empty_for_fresh_user(client, created_user):
    response = client.get(f"/api/chat_history/{created_user}")
    assert response.status_code == 200
    assert response.json() == []


def test_append_and_get_preserves_order(client, created_user):
    client.post(f"/api/chat_history/{created_user}", json={"role": "user", "content": "hello"})
    client.post(f"/api/chat_history/{created_user}", json={"role": "assistant", "content": "hi there"})

    response = client.get(f"/api/chat_history/{created_user}")
    assert response.status_code == 200
    assert response.json() == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi there"},
    ]


def test_append_invalid_role(client, created_user):
    response = client.post(
        f"/api/chat_history/{created_user}", json={"role": "system", "content": "nope"}
    )
    assert response.status_code == 422


def test_get_history_user_not_found(client):
    response = client.get("/api/chat_history/nonexistent-uuid")
    assert response.status_code == 404


def test_append_history_user_not_found(client):
    response = client.post(
        "/api/chat_history/nonexistent-uuid", json={"role": "user", "content": "hi"}
    )
    assert response.status_code == 404


def test_clear_history(client, created_user):
    client.post(f"/api/chat_history/{created_user}", json={"role": "user", "content": "hello"})
    client.post(f"/api/chat_history/{created_user}", json={"role": "assistant", "content": "hi"})

    response = client.delete(f"/api/chat_history/{created_user}")
    assert response.status_code == 200

    assert client.get(f"/api/chat_history/{created_user}").json() == []


def test_clear_history_user_not_found(client):
    response = client.delete("/api/chat_history/nonexistent-uuid")
    assert response.status_code == 404
