import httpx

from app.common.config import BACKEND_HOST, BACKEND_PORT

BASE_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}/api"
_HEALTH_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}/health"
_TIMEOUT        = 10.0
_HEALTH_TIMEOUT = 1.0   # shorter fast-fail timeout for the health check


def _get(path: str, **params) -> dict | list | None:
    try:
        r = httpx.get(f"{BASE_URL}{path}", params=params, timeout=_TIMEOUT)
        r.raise_for_status()
        return r.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        raise


def _post(path: str, json: dict | None = None) -> dict:
    r = httpx.post(f"{BASE_URL}{path}", json=json, timeout=_TIMEOUT)
    r.raise_for_status()
    return r.json()


def _put(path: str, json: dict) -> dict:
    r = httpx.put(f"{BASE_URL}{path}", json=json, timeout=_TIMEOUT)
    r.raise_for_status()
    return r.json()


def _delete(path: str) -> dict:
    r = httpx.delete(f"{BASE_URL}{path}", timeout=_TIMEOUT)
    r.raise_for_status()
    return r.json()


# ── Health ────────────────────────────────────────────────────────────────────

def health_check() -> bool:
    try:
        httpx.get(_HEALTH_URL, timeout=_HEALTH_TIMEOUT).raise_for_status()
        return True
    except Exception:
        return False


# ── Users ─────────────────────────────────────────────────────────────────────

def list_users() -> list:
    return _get("/list_users") or []


def submit_user_data(payload: dict) -> dict:
    return _post("/submit_user_data", json=payload)


def get_user_data(user_id: str) -> dict | None:
    return _get(f"/get_user_data/{user_id}")


def get_user_by_username(username: str) -> dict | None:
    return _get(f"/get_user_by_username/{username}")


def update_user_data(user_id: str, payload: dict) -> dict:
    return _put(f"/update_user_data/{user_id}", json=payload)


def delete_user(user_id: str) -> dict:
    return _delete(f"/delete_user/{user_id}")


# ── Settings ──────────────────────────────────────────────────────────────────

def get_user_settings(user_id: str) -> dict | None:
    return _get(f"/get_user_settings/{user_id}")


def update_user_settings(
    user_id: str,
    zodiac_system: str | None = None,
    house_system: str | None = None,
) -> dict:
    payload: dict = {}
    if zodiac_system is not None:
        payload["zodiac_system"] = zodiac_system
    if house_system is not None:
        payload["house_system"] = house_system
    return _put(f"/update_user_settings/{user_id}", json=payload)


# ── Charts ────────────────────────────────────────────────────────────────────

def calculate_natal_chart(user_id: str) -> dict:
    return _post(f"/calculate_natal_chart/{user_id}")


def get_natal_chart(user_id: str) -> dict | None:
    return _get(f"/get_natal_chart/{user_id}")


def calculate_transits(user_id: str, date: str | None = None) -> dict:
    params = {"date": date} if date else {}
    return _get(f"/calculate_transits/{user_id}", **params)


def get_sky_aspects(user_id: str, date: str | None = None) -> dict:
    params = {"date": date} if date else {}
    return _get(f"/sky_aspects/{user_id}", **params)


def get_sky_windows(user_id: str, date: str | None = None) -> dict | None:
    params = {"date": date} if date else {}
    return _get(f"/sky_windows/{user_id}", **params)


def get_transit_windows(user_id: str, date: str | None = None) -> dict | None:
    params = {"date": date} if date else {}
    return _get(f"/transit_windows/{user_id}", **params)


def get_transit_positions(user_id: str, date: str | None = None) -> dict:
    params = {"date": date} if date else {}
    return _get(f"/transit_positions/{user_id}", **params)


# ── Geocode ───────────────────────────────────────────────────────────────────

def geocode(query: str) -> dict | None:
    return _get("/geocode", q=query)


# ── Diary ─────────────────────────────────────────────────────────────────────

def get_diary_entries(user_id: str, date: str | None = None) -> list:
    params = {"date": date} if date else {}
    return _get(f"/get_diary_entries/{user_id}", **params) or []


def create_diary_entry(user_id: str, entry_date: str, content: str) -> dict:
    return _post(f"/create_diary_entry/{user_id}", json={"entry_date": entry_date, "content": content})


def update_diary_entry(entry_id: str, content: str) -> dict:
    return _put(f"/update_diary_entry/{entry_id}", json={"content": content})


def delete_diary_entry(entry_id: str) -> dict:
    return _delete(f"/delete_diary_entry/{entry_id}")
