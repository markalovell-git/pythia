"""Self-update for the packaged AppImage build.

A frozen bundle has no git/uv inside it, so updates come from the GitHub
Releases API: on launch the app checks for a newer release tag, and (on user
confirmation) downloads the new AppImage and swaps it in place.

The updater only acts when running as an AppImage (see
``app.common.runtime.can_self_update``); development runs skip it.
"""
import os
import shutil

import httpx

from app.version import get_version
from app.common import runtime
from app.common.logging_config import get_logger

log = get_logger(__name__)

_REPO = "markalovell-git/pythia"
_LATEST_URL = f"https://api.github.com/repos/{_REPO}/releases/latest"
# Must match the asset built by scripts/build_appimage.sh and published by
# .github/workflows/release.yml — a rename in any one breaks updates silently.
_ASSET_NAME = "Pythia-x86_64.AppImage"
_API_HEADERS = {"Accept": "application/vnd.github+json"}


def _parse_semver(tag: str) -> tuple[int, int, int]:
    """'v1.2.3' or '1.2.3-4-gabc' -> (1, 2, 3); missing parts become 0.

    Always returns exactly three components so comparisons are well-defined
    regardless of any git-describe suffix.
    """
    base = tag.lstrip("vV").split("-", 1)[0].strip()
    parts = []
    for chunk in base.split(".")[:3]:
        digits = "".join(c for c in chunk if c.isdigit())
        parts.append(int(digits) if digits else 0)
    while len(parts) < 3:
        parts.append(0)
    return parts[0], parts[1], parts[2]


def fetch_latest_release() -> dict | None:
    """Return the latest release dict from GitHub, or None on any failure."""
    try:
        resp = httpx.get(
            _LATEST_URL, timeout=8, headers=_API_HEADERS, follow_redirects=True
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        log.debug("Release check failed: %s", e)
        return None


def check_for_update() -> tuple[str, str | None, dict | None, bool]:
    """Return (current, latest_tag, release, behind).

    Fetches the release once so the same dict is reused for the download (no
    second API round-trip, no TOCTOU). Failures degrade to not-behind.
    """
    current = get_version()
    release = fetch_latest_release()
    if not release or not release.get("tag_name"):
        return current, None, None, False
    latest = release["tag_name"]
    behind = _parse_semver(latest) > _parse_semver(current)
    return current, latest, release, behind


def _asset(release: dict) -> dict | None:
    for asset in release.get("assets", []):
        if asset.get("name") == _ASSET_NAME:
            return asset
    return None


def apply_update(release: dict) -> tuple[bool, str]:
    """Download the release AppImage and replace the running one in place.

    Verifies the downloaded size against the asset metadata and fsyncs before an
    atomic swap, keeping a ``.bak`` of the previous image for recovery. On
    success the caller should re-exec the new image.
    """
    target = runtime.appimage_path()
    if target is None:
        return False, "Not running as an AppImage."

    asset = _asset(release)
    if not asset or not asset.get("browser_download_url"):
        return False, f"Release has no {_ASSET_NAME} asset."

    url = asset["browser_download_url"]
    expected = asset.get("size")
    tmp = target.with_name(target.name + ".new")
    timeout = httpx.Timeout(connect=10.0, read=30.0, write=30.0, pool=10.0)
    try:
        written = 0
        with httpx.stream("GET", url, timeout=timeout, follow_redirects=True) as resp:
            resp.raise_for_status()
            with open(tmp, "wb") as fh:
                for chunk in resp.iter_bytes(chunk_size=1 << 16):
                    fh.write(chunk)
                    written += len(chunk)
                fh.flush()
                os.fsync(fh.fileno())
        if expected and written != expected:
            raise IOError(f"size mismatch: got {written}, expected {expected}")
        os.chmod(tmp, 0o755)
        # Keep the old image recoverable in case the new one won't launch.
        try:
            shutil.copy2(target, target.with_name(target.name + ".bak"))
        except OSError:
            pass
        os.replace(tmp, target)  # atomic; safe while the image is mounted
    except Exception as e:
        log.warning("Update download/swap failed: %s", e)
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass
        return False, str(e)

    return True, "Update installed."
