"""Centralized, per-user writable paths.

All mutable application state (database, downloaded ephemeris, logs) lives under
a single per-user data directory rather than inside the source checkout. This
keeps ``git pull`` updates clean and preserves user data across updates and
re-clones.

On Linux this resolves to ``~/.local/share/Pythia/``.
"""
import shutil
from pathlib import Path

from platformdirs import user_data_dir

from app.common import runtime

_APP_NAME = "Pythia"
_APP_AUTHOR = "Pythia"

_DATA_DIR = Path(user_data_dir(_APP_NAME, _APP_AUTHOR))
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def data_dir() -> Path:
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    return _DATA_DIR


def db_path() -> Path:
    """SQLite database file path (pure accessor — see migrate_legacy_db)."""
    return data_dir() / "pythia.db"


def migrate_legacy_db() -> None:
    """One-time copy of a legacy ./sql_app.db into the user data dir."""
    target = db_path()
    if not target.exists():
        legacy = _REPO_ROOT / "sql_app.db"
        if legacy.exists():
            shutil.copy2(legacy, target)


def ephemeris_dir() -> Path:
    """Directory where Skyfield stores/downloads the ephemeris (de421.bsp).

    Seeds the bundled copy (one-time, guarded) so first launch needn't download.
    """
    d = data_dir() / "ephemeris"
    d.mkdir(parents=True, exist_ok=True)
    seed = runtime.resource_dir() / "data" / "de421.bsp"
    target = d / "de421.bsp"
    if seed.exists() and not target.exists():
        shutil.copy2(seed, target)
    return d


def log_dir() -> Path:
    d = data_dir() / "logs"
    d.mkdir(parents=True, exist_ok=True)
    return d
