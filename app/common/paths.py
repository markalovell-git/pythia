"""Centralized, per-user writable paths.

All mutable application state (database, downloaded ephemeris, logs) lives under
a single per-user data directory rather than inside the source checkout. This
keeps ``git pull`` updates clean and preserves user data across updates and
re-clones.

On Linux this resolves to ``~/.local/share/Pythia/``.
"""
import shutil
import sys
from pathlib import Path

from platformdirs import user_data_dir

_APP_NAME = "Pythia"
_APP_AUTHOR = "Pythia"

_DATA_DIR = Path(user_data_dir(_APP_NAME, _APP_AUTHOR))
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _resource_dir() -> Path:
    """Directory holding bundled read-only resources (e.g. data/de421.bsp).

    In a frozen PyInstaller build this is ``sys._MEIPASS``; from source it is
    the repository root.
    """
    bundle = getattr(sys, "_MEIPASS", None)
    return Path(bundle) if bundle else _REPO_ROOT


def data_dir() -> Path:
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    return _DATA_DIR


def db_path() -> Path:
    """SQLite database path. Migrates a legacy ./sql_app.db on first use."""
    target = data_dir() / "pythia.db"
    if not target.exists():
        legacy = _REPO_ROOT / "sql_app.db"
        if legacy.exists():
            shutil.copy2(legacy, target)
    return target


def ephemeris_dir() -> Path:
    """Directory where Skyfield stores/downloads the ephemeris (de421.bsp)."""
    d = data_dir() / "ephemeris"
    d.mkdir(parents=True, exist_ok=True)
    # Seed from the bundled copy (frozen bundle or source tree) to avoid a
    # first-run download.
    seed = _resource_dir() / "data" / "de421.bsp"
    target = d / "de421.bsp"
    if seed.exists() and not target.exists():
        shutil.copy2(seed, target)
    return d


def log_dir() -> Path:
    d = data_dir() / "logs"
    d.mkdir(parents=True, exist_ok=True)
    return d
