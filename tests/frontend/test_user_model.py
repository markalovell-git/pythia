from app.frontend.models import user_model


def test_list_users_returns_summaries(mock_api):
    mock_api["list_users"].return_value = [
        {"user_id": "u1", "username": "jdoe", "name": "John Doe"},
        {"user_id": "u2", "username": "jsmith", "name": "Jane Smith"},
    ]
    result = user_model.list_users()
    assert len(result) == 2
    assert result[0].username == "jdoe"
    assert result[1].name == "Jane Smith"


def test_list_users_empty(mock_api):
    mock_api["list_users"].return_value = []
    assert user_model.list_users() == []


def test_get_user_returns_detail(mock_api):
    mock_api["get_user_data"].return_value = {
        "user_id": "u1",
        "user_data": {
            "username": "jdoe",
            "name": "John Doe",
            "birth_datetime": "1990-06-15T08:30:00",
            "birth_timezone": "America/Chicago",
            "birth_location": "Chicago, IL",
            "birth_lat": 41.8781,
            "birth_lon": -87.6298,
        },
    }
    user = user_model.get_user("u1")
    assert user.username == "jdoe"
    assert user.birth_lat == 41.8781


def test_get_user_not_found(mock_api):
    mock_api["get_user_data"].return_value = None
    assert user_model.get_user("missing") is None


def test_create_user_returns_id(mock_api):
    mock_api["submit_user_data"].return_value = {"user_id": "new-uuid"}
    uid = user_model.create_user({"username": "x", "name": "X"})
    assert uid == "new-uuid"


def test_username_exists_true(mock_api):
    mock_api["get_user_by_username"].return_value = {"user_id": "u1"}
    assert user_model.username_exists("jdoe") is True


def test_username_exists_false(mock_api):
    mock_api["get_user_by_username"].return_value = None
    assert user_model.username_exists("ghost") is False
