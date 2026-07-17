"""Tests for API-key protection (app.common.secrets, Fernet-fallback path).

The autouse isolated_secrets fixture disables the OS keyring, so these tests
exercise the encrypted-column fallback that also runs on systems without a
Secret Service daemon.
"""
from app.common import secrets


def test_set_returns_ciphertext_and_get_round_trips():
    stored = secrets.set_api_key("user-1", "anthropic", "sk-ant-test-123")
    assert stored is not None and stored.startswith("enc:")
    assert "sk-ant-test-123" not in stored
    assert secrets.get_api_key("user-1", "anthropic", stored) == "sk-ant-test-123"


def test_get_passes_through_legacy_plaintext():
    assert secrets.get_api_key("user-1", "openai", "sk-legacy") == "sk-legacy"
    assert secrets.get_api_key("user-1", "openai", None) is None


def test_migrate_plaintext_value():
    changed, new_value = secrets.migrate_plaintext_value("user-1", "anthropic", "sk-plain")
    assert changed
    assert new_value.startswith("enc:")
    assert secrets.get_api_key("user-1", "anthropic", new_value) == "sk-plain"

    # Already-protected and empty values are left alone
    assert secrets.migrate_plaintext_value("user-1", "anthropic", new_value) == (False, new_value)
    assert secrets.migrate_plaintext_value("user-1", "anthropic", None) == (False, None)


def test_undecryptable_value_returns_none():
    assert secrets.get_api_key("user-1", "anthropic", "enc:not-real-ciphertext") is None


# ── Router integration ─────────────────────────────────────────────────────────

def test_key_saved_via_api_is_not_stored_plaintext(client, created_user, tmp_path):
    from tests.conftest import TestingSessionLocal
    from app.common.database import UserSettings

    resp = client.put(
        f"/api/update_user_settings/{created_user}",
        json={"ai_provider": "claude", "anthropic_key": "sk-ant-secret"},
    )
    assert resp.status_code == 200
    # The API returns the resolved key to the (local) frontend…
    assert resp.json()["anthropic_key"] == "sk-ant-secret"
    # …but the DB column never holds it in plaintext.
    db = TestingSessionLocal()
    try:
        row = db.query(UserSettings).filter(UserSettings.user_id == created_user).first()
        assert row.anthropic_key != "sk-ant-secret"
        assert row.anthropic_key is None or row.anthropic_key.startswith("enc:")
    finally:
        db.close()

    # And a fresh read resolves it back.
    resp = client.get(f"/api/get_user_settings/{created_user}")
    assert resp.json()["anthropic_key"] == "sk-ant-secret"
