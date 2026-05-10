from unittest.mock import MagicMock, patch
import pytest

from app.frontend import api_client


@pytest.fixture
def mock_api(monkeypatch):
    """Replaces all api_client functions with MagicMocks for the duration of the test."""
    mocks = {}
    for name in dir(api_client):
        obj = getattr(api_client, name)
        if callable(obj) and not name.startswith("_"):
            m = MagicMock()
            monkeypatch.setattr(api_client, name, m)
            mocks[name] = m
    return mocks
