"""Database-at-rest encryption: SQLCipher key management and the one-time
plaintext→encrypted migration.

The autouse isolated_secrets fixture disables the OS keyring, so get_db_key()
exercises the .dbkey-file fallback against a throwaway directory.
"""
import sqlite3

import pytest
import sqlcipher3

from app.common import database, secrets


def test_get_db_key_is_stable_hex():
    key = secrets.get_db_key()
    assert key == secrets.get_db_key()  # created once, then reused
    assert len(key) == 64
    int(key, 16)  # raises if not hex


def test_encrypt_plaintext_db_round_trip(tmp_path):
    db_file = tmp_path / "pythia.db"
    conn = sqlite3.connect(str(db_file))
    conn.executescript(
        "CREATE TABLE t (x TEXT); INSERT INTO t VALUES ('secret-natal-data');"
    )
    conn.close()
    key = secrets.get_db_key()

    database._encrypt_plaintext_db(db_file, key)

    raw = db_file.read_bytes()
    assert not raw.startswith(database._SQLITE_MAGIC)
    assert b"secret-natal-data" not in raw
    # Plain SQLite can no longer open it…
    with pytest.raises(sqlite3.DatabaseError):
        sqlite3.connect(str(db_file)).execute("SELECT * FROM t")
    # …but SQLCipher with the key reads the migrated data intact.
    conn = sqlcipher3.connect(str(db_file))
    conn.execute(f"PRAGMA key = \"x'{key}'\"")
    assert conn.execute("SELECT x FROM t").fetchone() == ("secret-natal-data",)
    conn.close()


def test_encrypt_is_idempotent(tmp_path):
    db_file = tmp_path / "pythia.db"
    sqlite3.connect(str(db_file)).executescript("CREATE TABLE t (x TEXT);")
    key = secrets.get_db_key()

    database._encrypt_plaintext_db(db_file, key)
    encrypted_bytes = db_file.read_bytes()
    database._encrypt_plaintext_db(db_file, key)  # second run must not touch it

    assert db_file.read_bytes() == encrypted_bytes


def test_missing_or_empty_db_is_left_alone(tmp_path):
    database._encrypt_plaintext_db(tmp_path / "absent.db", "ab" * 32)
    assert not (tmp_path / "absent.db").exists()

    empty = tmp_path / "empty.db"
    empty.touch()
    database._encrypt_plaintext_db(empty, "ab" * 32)
    assert empty.read_bytes() == b""
