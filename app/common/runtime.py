"""Runtime environment detection — frozen build vs source, AppImage, resources.

Centralizes the `sys.frozen` / `sys._MEIPASS` / `$APPIMAGE` checks that would
otherwise be scattered across version, paths, and the updater.
"""
import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def is_frozen() -> bool:
    """True when running from a PyInstaller bundle."""
    return getattr(sys, "frozen", False)


def resource_dir() -> Path:
    """Directory holding bundled read-only resources (e.g. data/de421.bsp).

    ``sys._MEIPASS`` in a frozen build, the repository root from source.
    """
    bundle = getattr(sys, "_MEIPASS", None)
    return Path(bundle) if bundle else _REPO_ROOT


def appimage_path() -> Path | None:
    """Path to the running AppImage, or None if not running as one.

    The AppImage runtime sets ``$APPIMAGE`` to the image's own path.
    """
    p = os.environ.get("APPIMAGE")
    return Path(p) if p else None


def can_self_update() -> bool:
    """True only when running as an AppImage (the only self-updatable form)."""
    return appimage_path() is not None
