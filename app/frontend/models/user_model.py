from dataclasses import dataclass
from app.frontend import api_client


@dataclass
class UserSummary:
    user_id: str
    username: str
    name: str


@dataclass
class UserDetail:
    user_id: str
    username: str
    name: str
    birth_datetime: str
    birth_timezone: str
    birth_location: str
    birth_lat: float
    birth_lon: float


def list_users() -> list[UserSummary]:
    rows = api_client.list_users()
    return [UserSummary(**r) for r in rows]


def get_user(user_id: str) -> UserDetail | None:
    raw = api_client.get_user_data(user_id)
    if not raw:
        return None
    d = raw["user_data"]
    return UserDetail(
        user_id=user_id,
        username=d["username"],
        name=d["name"],
        birth_datetime=d["birth_datetime"],
        birth_timezone=d["birth_timezone"],
        birth_location=d["birth_location"],
        birth_lat=d["birth_lat"],
        birth_lon=d["birth_lon"],
    )


def create_user(payload: dict) -> str:
    """Returns the new user_id."""
    raw = api_client.submit_user_data(payload)
    return raw["user_id"]


def update_user(user_id: str, payload: dict) -> None:
    api_client.update_user_data(user_id, payload)


def delete_user(user_id: str) -> None:
    api_client.delete_user(user_id)


def username_exists(username: str) -> bool:
    return api_client.get_user_by_username(username) is not None
