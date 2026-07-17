"""API-key storage: OS keyring first, Fernet-encrypted DB value as fallback.

The DB column for a provider key (user_settings.anthropic_key / openai_key)
holds one of:

- NULL          — the key lives in the OS keyring (or no key is set)
- ``enc:<...>`` — Fernet ciphertext, decryptable with the local key file
- anything else — legacy plaintext (moved out by migrate_plaintext_value on
  the next backend startup)

This module also owns the SQLCipher key for the database itself (get_db_key):
same storage strategy, with a ``.dbkey`` file as the non-keyring fallback.

The keyring is the real protection (secrets unlocked with the desktop login).
The file fallbacks only guard against casual DB copying — the key files sit
on the same disk — but they keep the app working on systems without a Secret
Service daemon.
"""
import logging
import os
from pathlib import Path

from app.common import paths

_log = logging.getLogger(__name__)

_SERVICE = "Pythia"
_ENC_PREFIX = "enc:"
_DB_KEY_NAME = "database"

# Tests set this to False to keep test keys out of the user's real keyring
# (and to exercise the Fernet fallback path).
keyring_enabled = True


def _keyring_name(user_id: str, provider: str) -> str:
    return f"{user_id}/{provider}"


def _keyfile_path() -> Path:
    return paths.data_dir() / ".keyfile"


def _fernet():
    from cryptography.fernet import Fernet

    keyfile = _keyfile_path()
    if keyfile.exists():
        return Fernet(keyfile.read_bytes().strip())
    key = Fernet.generate_key()
    keyfile.touch(mode=0o600, exist_ok=True)
    keyfile.chmod(0o600)  # in case the file predates the touch() above
    keyfile.write_bytes(key)
    return Fernet(key)


def set_api_key(user_id: str, provider: str, key: str) -> str | None:
    """Store an API key; return the value to persist in the DB column.

    Returns None when the key went into the OS keyring, or an ``enc:``-prefixed
    ciphertext to store in the column when it didn't.
    """
    if keyring_enabled:
        try:
            import keyring
            keyring.set_password(_SERVICE, _keyring_name(user_id, provider), key)
            return None
        except Exception as e:
            _log.info("Keyring unavailable (%s); storing key encrypted in DB", e)
    return _ENC_PREFIX + _fernet().encrypt(key.encode()).decode()


def get_api_key(user_id: str, provider: str, db_value: str | None) -> str | None:
    """Resolve an API key from the keyring, the encrypted column, or legacy plaintext."""
    if keyring_enabled:
        try:
            import keyring
            value = keyring.get_password(_SERVICE, _keyring_name(user_id, provider))
            if value:
                return value
        except Exception:
            pass
    if db_value and db_value.startswith(_ENC_PREFIX):
        try:
            return _fernet().decrypt(db_value[len(_ENC_PREFIX):].encode()).decode()
        except Exception as e:
            _log.error("Could not decrypt stored %s key for %s: %s", provider, user_id, e)
            return None
    return db_value  # legacy plaintext, or None


def delete_api_key(user_id: str, provider: str) -> None:
    """Best-effort removal of a key from the OS keyring."""
    if not keyring_enabled:
        return
    try:
        import keyring
        keyring.delete_password(_SERVICE, _keyring_name(user_id, provider))
    except Exception:
        pass


def migrate_plaintext_value(user_id: str, provider: str, db_value: str | None) -> tuple[bool, str | None]:
    """If db_value is legacy plaintext, move it to protected storage.

    Returns (changed, new_db_value).
    """
    if not db_value or db_value.startswith(_ENC_PREFIX):
        return False, db_value
    return True, set_api_key(user_id, provider, db_value)


# ── Database (SQLCipher) key ───────────────────────────────────────────────────

def _db_keyfile_path() -> Path:
    return paths.data_dir() / ".dbkey"


def _read_or_create_db_keyfile() -> str:
    keyfile = _db_keyfile_path()
    if keyfile.exists():
        return keyfile.read_text().strip()
    key = os.urandom(32).hex()
    keyfile.touch(mode=0o600, exist_ok=True)
    keyfile.chmod(0o600)
    keyfile.write_text(key)
    return key


def get_db_key() -> str:
    """Return the hex SQLCipher key for the database, creating one on first use.

    Keyring first, ``.dbkey`` file fallback. A file-stored key is promoted into
    the keyring (and the file removed) once a keyring becomes available, so the
    key never lives in two places.
    """
    if keyring_enabled:
        try:
            import keyring
            key = keyring.get_password(_SERVICE, _DB_KEY_NAME)
            if key:
                return key
            keyfile = _db_keyfile_path()
            if keyfile.exists():
                key = keyfile.read_text().strip()
                keyring.set_password(_SERVICE, _DB_KEY_NAME, key)
                keyfile.unlink()
                _log.info("Promoted DB key from file into the OS keyring")
            else:
                key = os.urandom(32).hex()
                keyring.set_password(_SERVICE, _DB_KEY_NAME, key)
            return key
        except Exception as e:
            _log.info("Keyring unavailable (%s); using DB key file", e)
    return _read_or_create_db_keyfile()
