"""Single source of truth for the application version.

The canonical fallback lives in ``app.__version__``. When running from a git
checkout we prefer ``git describe --tags`` so the displayed version reflects the
exact release/dev state (e.g. ``v0.2.0`` or ``v0.2.0-3-gabc123``).
"""
import subprocess
from pathlib import Path

from app import __version__
from app.common import runtime

# Repo root = two levels up from this file (app/version.py -> app -> repo).
_REPO_ROOT = Path(__file__).resolve().parent.parent


def _git_describe() -> str | None:
    """Latest tag (optionally with commits-ahead suffix), or None if untagged."""
    try:
        out = subprocess.run(
            ["git", "describe", "--tags"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    described = out.stdout.strip()
    return described or None


def get_version() -> str:
    """Human-readable version string for display (About dialog, window title)."""
    # A frozen build has no .git; __version__ is the baked-in source of truth.
    if not runtime.is_frozen():
        described = _git_describe()
        if described:
            return described
    return f"v{__version__}"
