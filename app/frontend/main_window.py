from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget, QLabel, QSizePolicy,
)

from app.frontend import app_state
from app.frontend.widgets.chart_view import ChartView
from app.frontend.widgets.transit_view import TransitView
from app.frontend.widgets.diary_view import DiaryView
from app.frontend.widgets.timeline_view import TimelineView
from app.frontend.widgets.consult_view import ConsultView
from app.frontend.widgets.settings_view import SettingsView


class MainWindow(QMainWindow):
    """Main application window. Shown after a user signs in.

    The sidebar emits navigation; this class wires signals between
    views. No widget here imports another widget directly.
    """

    _settings = QSettings("Pythia", "Pythia")

    def __init__(self, user_id: str, on_sign_out=None):
        super().__init__()
        self._on_sign_out = on_sign_out
        self._user_id = user_id
        app_state.state.current_user_id = user_id
        self.setWindowTitle("Pythia")
        self.setMinimumSize(1000, 700)
        self._build_ui(user_id)
        self._load_all(user_id)
        self._restore_geometry()

    def _build_ui(self, user_id: str):
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Sidebar ───────────────────────────────────────────────
        sidebar = QWidget()
        sidebar.setFixedWidth(160)
        sidebar.setStyleSheet("background: #1a1a2e;")
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(8, 16, 8, 16)

        app_label = QLabel("Pythia")
        app_label.setStyleSheet("color: #aaaaff; font-size: 20px; font-weight: bold;")
        app_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sb_layout.addWidget(app_label)
        sb_layout.addSpacing(16)

        self._nav_buttons: list[QPushButton] = []
        nav_items = [
            ("Chart",    self._show_chart),
            ("Transits", self._show_transits),
            ("Diary",    self._show_diary),
            ("Timeline", self._show_timeline),
            ("Consult",  self._show_consult),
            ("Settings", self._show_settings),
        ]
        for label, slot in nav_items:
            btn = QPushButton(label)
            btn.setStyleSheet("""
                QPushButton { color: #ccc; background: transparent; border: none;
                              text-align: left; padding: 10px 8px; font-size: 14px; }
                QPushButton:hover { background: #2a2a4e; color: white; }
                QPushButton:checked { background: #3a3a6e; color: white; }
            """)
            btn.setCheckable(True)
            btn.clicked.connect(slot)
            sb_layout.addWidget(btn)
            self._nav_buttons.append(btn)

        sb_layout.addStretch()
        about_btn = QPushButton("About")
        about_btn.setStyleSheet(
            "color: #888; background: transparent; border: none; padding: 8px;"
        )
        about_btn.clicked.connect(self._show_about)
        sb_layout.addWidget(about_btn)

        sign_out_btn = QPushButton("Sign Out")
        sign_out_btn.setStyleSheet(
            "color: #888; background: transparent; border: none; padding: 8px;"
        )
        sign_out_btn.clicked.connect(self._on_sign_out_clicked)
        sb_layout.addWidget(sign_out_btn)
        root.addWidget(sidebar)

        # ── Content stack ─────────────────────────────────────────
        self.stack = QStackedWidget()
        self.chart_view = ChartView()
        self.transit_view = TransitView()
        self.diary_view = DiaryView()
        self.timeline_view = TimelineView()
        self.consult_view = ConsultView()
        self.settings_view = SettingsView()

        self.stack.addWidget(self.chart_view)
        self.stack.addWidget(self.transit_view)
        self.stack.addWidget(self.diary_view)
        self.stack.addWidget(self.timeline_view)
        self.stack.addWidget(self.consult_view)
        self.stack.addWidget(self.settings_view)
        root.addWidget(self.stack)

        # Wire settings signals
        self.settings_view.user_deleted.connect(self._on_sign_out_clicked)
        self.settings_view.chart_changed.connect(lambda: self.chart_view.load(user_id))

        self._select_nav(0)

    def _load_all(self, user_id: str):
        self.chart_view.load(user_id)
        self.transit_view.load(user_id)
        self.diary_view.load(user_id)
        self.timeline_view.load(user_id)
        self.consult_view.load(user_id)
        self.settings_view.load(user_id)

    def _select_nav(self, index: int):
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == index)
        self.stack.setCurrentIndex(index)

    def _show_chart(self):    self._select_nav(0)
    def _show_transits(self): self._select_nav(1)
    def _show_diary(self):    self._select_nav(2)
    def _show_timeline(self): self._select_nav(3)
    def _show_consult(self):  self._select_nav(4)
    def _show_settings(self): self._select_nav(5)

    def _show_about(self):
        from app.frontend.widgets.about_dialog import AboutDialog
        AboutDialog(self).exec()

    def _restore_geometry(self):
        geom = self._settings.value(f"geometry/{self._user_id}")
        if geom:
            self.restoreGeometry(geom)

    def closeEvent(self, event):
        self._settings.setValue(f"geometry/{self._user_id}", self.saveGeometry())
        super().closeEvent(event)

    def _on_sign_out_clicked(self):
        self._settings.setValue(f"geometry/{self._user_id}", self.saveGeometry())
        app_state.state.current_user_id = None
        self.close()
        if self._on_sign_out:
            self._on_sign_out()
