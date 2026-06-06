"""Desktop integration for the AppImage build (Linux).

Writes/removes a ``.desktop`` launcher + icon under ``~/.local/share`` so Pythia
appears in the application menu and can be pinned to the dash. Only meaningful
when running as an AppImage — the launcher's ``Exec`` points at the running
``$APPIMAGE``.

The launcher's ``StartupWMClass`` matches the Wayland app_id the GUI advertises
via ``QGuiApplication.setDesktopFileName(WM_CLASS)`` so the dock binds to the
running window (correct icon, no ghost/duplicate entry, pinnable).
"""
import os
import shutil
import subprocess
from pathlib import Path

from app.common import runtime
from app.common.logging_config import get_logger

log = get_logger(__name__)

# Must match QGuiApplication.setDesktopFileName(...) in app.frontend.main and the
# basename of the .desktop file below.
WM_CLASS = "pythia"

_ICON_ROOT = Path.home() / ".local/share/icons/hicolor"
_APPS_DIR = Path.home() / ".local/share/applications"
_ICON_DIR = _ICON_ROOT / "scalable/apps"
_DESKTOP_FILE = _APPS_DIR / f"{WM_CLASS}.desktop"
_ICON_FILE = _ICON_DIR / f"{WM_CLASS}.svg"

_DESKTOP_TEMPLATE = """\
[Desktop Entry]
Type=Application
Name=Pythia
GenericName=Astrology
Comment=Natal charts, transits, diary, and timeline
Exec={exec}
Icon={wm_class}
Terminal=false
Categories=Education;
StartupNotify=true
StartupWMClass={wm_class}
"""


def is_available() -> bool:
    """True only when running as an AppImage (the only integrable form)."""
    return runtime.can_self_update()


def is_installed() -> bool:
    return _DESKTOP_FILE.exists()


def _bundled_icon() -> Path | None:
    for cand in (
        runtime.resource_dir() / "pythia.svg",              # frozen bundle
        runtime.resource_dir() / "packaging" / "pythia.svg",  # source tree
    ):
        if cand.exists():
            return cand
    return None


def _refresh_caches() -> None:
    for cmd in (
        ["update-desktop-database", str(_APPS_DIR)],
        ["gtk-update-icon-cache", "-f", "-t", str(_ICON_ROOT)],
    ):
        try:
            subprocess.run(cmd, check=False, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            pass  # best-effort; GNOME also rescans on next login


def _desktop_contents(appimage: Path) -> str:
    return _DESKTOP_TEMPLATE.format(exec=appimage, wm_class=WM_CLASS)


def install() -> tuple[bool, str]:
    """Create the menu launcher + icon pointing at the running AppImage."""
    appimage = runtime.appimage_path()
    if appimage is None:
        return False, "Not running as an AppImage."
    try:
        _APPS_DIR.mkdir(parents=True, exist_ok=True)
        _ICON_DIR.mkdir(parents=True, exist_ok=True)
        icon = _bundled_icon()
        if icon is not None:
            shutil.copyfile(icon, _ICON_FILE)
        _DESKTOP_FILE.write_text(_desktop_contents(appimage))
        os.chmod(_DESKTOP_FILE, 0o644)
        _refresh_caches()
        return True, "Pythia was added to your applications menu."
    except OSError as e:
        log.warning("Desktop integration install failed: %s", e)
        return False, str(e)


def uninstall() -> tuple[bool, str]:
    """Remove the menu launcher + icon."""
    try:
        for f in (_DESKTOP_FILE, _ICON_FILE):
            try:
                f.unlink()
            except FileNotFoundError:
                pass
        _refresh_caches()
        return True, "Pythia was removed from your applications menu."
    except OSError as e:
        log.warning("Desktop integration uninstall failed: %s", e)
        return False, str(e)


def sync_exec_path() -> None:
    """Keep an installed launcher's Exec pointed at the current AppImage.

    The path can change if the user moves the file (updates swap it in place, so
    the path is stable across updates). No-op if not installed.
    """
    appimage = runtime.appimage_path()
    if appimage is None or not is_installed():
        return
    desired = _desktop_contents(appimage)
    try:
        if _DESKTOP_FILE.read_text() != desired:
            _DESKTOP_FILE.write_text(desired)
            _refresh_caches()
            log.debug("Re-pointed desktop launcher Exec to %s", appimage)
    except OSError as e:
        log.debug("sync_exec_path failed: %s", e)
