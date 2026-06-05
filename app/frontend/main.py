import os
import sys
import time
from PyQt6.QtWidgets import QApplication, QSplashScreen, QLabel, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap

from app.common.logging_config import setup_logging, get_logger
from app.common.config import BACKEND_STARTUP_TIMEOUT
from app.version import get_version
setup_logging()
log = get_logger(__name__)

from app.frontend.workers.backend_worker import BackendWorker
from app.frontend import api_client
from app.frontend import updater


def _wait_for_backend(timeout: float = 10.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if api_client.health_check():
            return True
        time.sleep(0.1)
    return False


def _relaunch():
    """Re-exec the freshly downloaded AppImage. Guards against re-checking."""
    appimage = updater.appimage_path()
    if appimage is None:
        return
    os.environ["PYTHIA_SKIP_UPDATE"] = "1"
    log.debug("Relaunching updated AppImage: %s", appimage)
    os.execve(str(appimage), [str(appimage)], os.environ)


def _maybe_update():
    """If a newer release exists, prompt and (on confirm) update + relaunch."""
    if os.environ.pop("PYTHIA_SKIP_UPDATE", None):
        return
    if not updater.can_self_update():
        return
    try:
        current, latest, behind = updater.check_for_update()
    except Exception as e:
        log.warning("Update check failed: %s", e)
        return
    if not behind:
        return

    resp = QMessageBox.question(
        None,
        "Update available",
        f"A new version of Pythia is available.\n\n"
        f"{current}  →  {latest}\n\nUpdate now?",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.Yes,
    )
    if resp != QMessageBox.StandardButton.Yes:
        return

    progress = QSplashScreen()
    pix = QPixmap(400, 120)
    from PyQt6.QtGui import QColor
    pix.fill(QColor("#0d0d1a"))
    progress.setPixmap(pix)
    lbl = QLabel(f"Downloading {latest}…", progress)
    lbl.setStyleSheet("color: #aaaaff; font-size: 16px;")
    lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lbl.setGeometry(0, 0, 400, 120)
    progress.show()
    QApplication.processEvents()

    ok, msg = updater.apply_update()
    progress.close()
    log.debug("Update result: %s", msg)
    if not ok:
        QMessageBox.warning(
            None, "Update failed",
            "The update could not be completed. Starting the current version.\n\n"
            f"{msg}",
        )
        return
    _relaunch()


def _selftest() -> int:
    """Verify bundled data loads (ephemeris + timezone). Exits 0 on success.

    Used to smoke-test a packaged build (`pythia --selftest`) without a GUI.
    """
    from datetime import datetime, timezone
    try:
        from app.astrology.chart import compute_planet_positions
        positions = compute_planet_positions(
            datetime(2000, 1, 1, 12, tzinfo=timezone.utc), "tropical"
        )
        assert "Sun" in positions, "Sun missing from computed positions"

        from timezonefinder import TimezoneFinder
        tz = TimezoneFinder().timezone_at(lat=51.5074, lng=-0.1278)
        assert tz, "timezone lookup returned nothing"

        sign = positions["Sun"]["sign"]
        print(
            f"selftest OK — {get_version()}; Sun in {sign}; tz={tz}; "
            f"self-update={'yes' if updater.can_self_update() else 'no'}"
        )
        return 0
    except Exception as e:
        print(f"selftest FAILED: {e}", file=sys.stderr)
        return 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(_selftest())

    app = QApplication(sys.argv)
    app.setApplicationName("Pythia")
    app.setApplicationVersion(get_version())
    app.setStyle("Fusion")

    # Dark palette
    from PyQt6.QtGui import QPalette, QColor
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#0d0d1a"))
    palette.setColor(QPalette.ColorRole.WindowText, QColor("#e0e0e0"))
    palette.setColor(QPalette.ColorRole.Base, QColor("#1a1a2e"))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#16213e"))
    palette.setColor(QPalette.ColorRole.Text, QColor("#e0e0e0"))
    palette.setColor(QPalette.ColorRole.Button, QColor("#1a1a2e"))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor("#e0e0e0"))
    palette.setColor(QPalette.ColorRole.Highlight, QColor("#3a3a6e"))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#ffffff"))
    app.setPalette(palette)

    app.setStyleSheet("""
        QPushButton {
            background: #2a2a50;
            color: #d0d0f0;
            border: 1px solid #4a4a8a;
            border-radius: 5px;
            padding: 6px 18px;
            font-size: 13px;
        }
        QPushButton:hover {
            background: #3c3c72;
            border-color: #7a7acc;
            color: #ffffff;
        }
        QPushButton:pressed {
            background: #12122e;
            border-color: #9a9aee;
            border-top-color: #5a5a9a;
            border-left-color: #5a5a9a;
            padding: 8px 16px 4px 20px;
            color: #aaaacc;
        }
        QPushButton:disabled {
            background: #1a1a2e;
            color: #444466;
            border-color: #2a2a44;
        }
        QPushButton:default {
            border-color: #7a7acc;
        }
        QPushButton:default:disabled {
            border-color: #2a2a44;
        }
    """)

    # Check for updates before doing any real work, so a re-exec is cheap.
    _maybe_update()

    # Start backend
    backend = BackendWorker()
    backend.start()

    # Splash while waiting
    splash_pix = QPixmap(400, 200)
    splash_pix.fill(QColor("#0d0d1a"))
    splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
    splash_label = QLabel("Starting Pythia…", splash)
    splash_label.setStyleSheet("color: #aaaaff; font-size: 18px;")
    splash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    splash_label.setGeometry(0, 0, 400, 200)
    splash.show()
    app.processEvents()

    if not _wait_for_backend(BACKEND_STARTUP_TIMEOUT):
        splash.close()
        QMessageBox.critical(None, "Startup Error", "Backend failed to start.")
        backend.stop()
        sys.exit(1)

    splash.close()

    from app.frontend.widgets.welcome import WelcomeWidget
    from app.frontend.main_window import MainWindow

    welcome: WelcomeWidget | None = None
    main_win: MainWindow | None = None

    def show_welcome():
        nonlocal welcome, main_win
        if main_win:
            main_win.close()
            main_win = None
        welcome = WelcomeWidget()
        welcome.setWindowTitle(f"Pythia {get_version()}")
        welcome.setMinimumSize(500, 400)
        welcome.user_selected.connect(sign_in)
        welcome.create_profile.connect(open_wizard)
        welcome.show()

    def sign_in(user_id: str):
        nonlocal welcome, main_win
        log.debug("sign_in: user_id=%s", user_id)
        if welcome:
            welcome.close()
            welcome = None
        main_win = MainWindow(user_id, on_sign_out=show_welcome)
        main_win.show()
        log.debug("sign_in: MainWindow shown")

    def open_wizard():
        from app.frontend.widgets.account_wizard import AccountWizard
        from PyQt6.QtWidgets import QDialog
        log.debug("open_wizard: starting")
        wizard = AccountWizard(welcome)
        result = wizard.exec()
        log.debug("open_wizard: exec returned %s, created_user_id=%s", result, wizard.created_user_id)
        if result == QDialog.DialogCode.Accepted and wizard.created_user_id:
            sign_in(wizard.created_user_id)
        elif welcome:
            welcome.refresh()

    show_welcome()

    exit_code = app.exec()
    backend.stop()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
