import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.backend.main import app
from app.common import secrets
from app.common.database import Base, get_db

TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def isolated_secrets(tmp_path, monkeypatch):
    """Keep test API keys out of the user's real keyring and data dir.

    Forces the Fernet-fallback path with a throwaway key file.
    """
    monkeypatch.setattr(secrets, "keyring_enabled", False)
    monkeypatch.setattr(secrets, "_keyfile_path", lambda: tmp_path / ".keyfile")
    monkeypatch.setattr(secrets, "_db_keyfile_path", lambda: tmp_path / ".dbkey")


@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture
def created_user(client):
    response = client.post("/api/submit_user_data", json={
        "username": "jdoe",
        "name": "John Doe",
        "birth_datetime": "1990-06-15T08:30:00",
        "birth_timezone": "America/Chicago",
        "birth_location": "Chicago, IL",
        "birth_lat": 41.8781,
        "birth_lon": -87.6298,
    })
    return response.json()["user_id"]
