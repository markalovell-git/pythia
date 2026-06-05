"""Self-update for the packaged AppImage build.

A frozen bundle has no git/uv inside it, so updates come from the GitHub
Releases API: on launch the app checks for a newer release tag, and (on user
confirmation) downloads the new AppImage and swaps it in place.

The updater is a no-op unless the process is running as an AppImage, detected
via the ``APPIMAGE`` environment variable (set by the AppImage runtime to the
path of the running image). Development runs (``uv run pythia``) skip updates.
"""
import os
from pathlib import Path

import httpx

from app.version import get_version
from app.common.logging_config import get_logger

log = get_logger(__name__)

_REPO = "markalovell-git/pythia"
_LATEST_URL = f"https://api.github.com/repos/{_REPO}/releases/latest"
_ASSET_NAME = "Pythia-x86_64.AppImage"


def appimage_path() -> Path | None:
    """Path to the running AppImage, or None if not running as one."""
    p = os.environ.get("APPIMAGE")
    return Path(p) if p else None


def can_self_update() -> bool:
    return appimage_path() is not None


def _parse_semver(tag: str) -> tuple[int, ...]:
    """Turn 'v1.2.3' / '1.2.3' into (1, 2, 3); unparsable parts become 0."""
    cleaned = tag.lstrip("vV").strip()
    parts = []
    for chunk in cleaned.split("."):
        num = "".join(c for c in chunk if c.isdigit())
        parts.append(int(num) if num else 0)
    return tuple(parts) or (0,)


def check_for_update() -> tuple[str, str | None, bool]:
    """Return (current, latest_tag, behind).

    Network/API failures degrade gracefully to (current, None, False).
    """
    current = get_version()
    try:
        resp = httpx.get(
            _LATEST_URL,
            timeout=8,
            headers={"Accept": "application/vnd.github+json"},
            follow_redirects=True,
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        log.debug("Release check failed: %s", e)
        return current, None, False

    latest = data.get("tag_name")
    if not latest:
        return current, None, False

    behind = _parse_semver(latest) > _parse_semver(current)
    return current, latest, behind


def _asset_url(release: dict) -> str | None:
    for asset in release.get("assets", []):
        if asset.get("name") == _ASSET_NAME:
            return asset.get("browser_download_url")
    return None


def fetch_latest_release() -> dict | None:
    try:
        resp = httpx.get(
            _LATEST_URL,
            timeout=8,
            headers={"Accept": "application/vnd.github+json"},
            follow_redirects=True,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        log.debug("Fetching release failed: %s", e)
        return None


def apply_update() -> tuple[bool, str]:
    """Download the latest AppImage and replace the running one in place.

    Returns (ok, message). On success the caller should re-exec the new image.
    """
    target = appimage_path()
    if target is None:
        return False, "Not running as an AppImage."

    release = fetch_latest_release()
    if release is None:
        return False, "Could not reach the update server."

    url = _asset_url(release)
    if not url:
        return False, f"Release has no {_ASSET_NAME} asset."

    tmp = target.with_name(target.name + ".new")
    try:
        with httpx.stream("GET", url, timeout=None, follow_redirects=True) as resp:
            resp.raise_for_status()
            with open(tmp, "wb") as fh:
                for chunk in resp.iter_bytes(chunk_size=1 << 16):
                    fh.write(chunk)
        os.chmod(tmp, 0o755)
        # Atomic swap; safe while running since the image is already mounted.
        os.replace(tmp, target)
    except Exception as e:
        log.warning("Update download/swap failed: %s", e)
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        return False, str(e)

    return True, "Update installed."
