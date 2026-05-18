from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QDateTimeEdit, QHeaderView,
)

from app.frontend.models import chart_model
from app.frontend.widgets.chart_view import ASPECT_COLORS
from app.frontend.workers.api_worker import ApiWorker


_CATEGORY_COLORS = {
    "major":      "#ffd700",
    "notable":    "#44bb88",
    "minor":      "#7070a0",
    "background": "#444444",
}

_SIGNIFICANT_CATEGORIES = {"major", "notable"}


def _table_cell(text: str, color: str | None = None) -> QTableWidgetItem:
    item = QTableWidgetItem(text)
    if color:
        item.setForeground(QColor(color))
    return item




class TransitView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._worker: ApiWorker | None = None
        self._sky_worker: ApiWorker | None = None
        self._windows_worker: ApiWorker | None = None
        self._current_transits: list[chart_model.Transit] = []
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Transits")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Date/time:"))
        self.dt_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.dt_edit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.dt_edit.setCalendarPopup(True)
        controls.addWidget(self.dt_edit)

        self.now_btn = QPushButton("Now")
        self.now_btn.clicked.connect(self._set_now)
        controls.addWidget(self.now_btn)

        self.calc_btn = QPushButton("Calculate")
        self.calc_btn.clicked.connect(self._on_calculate)
        controls.addWidget(self.calc_btn)

        self.sig_btn = QPushButton("Significant Transits Only: OFF")
        self.sig_btn.setCheckable(True)
        self.sig_btn.setChecked(False)
        self.sig_btn.toggled.connect(self._on_sig_toggled)
        self._update_sig_btn_style(False)
        controls.addWidget(self.sig_btn)

        controls.addStretch()
        layout.addLayout(controls)

        transit_label = QLabel("Transit → Natal")
        transit_label.setStyleSheet("font-weight: bold; margin-top: 6px;")
        layout.addWidget(transit_label)

        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels([
            "Transit Planet", "Aspect", "Natal Planet", "Orb", "Score", "Transit Position", "Dates",
        ])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        sky_label = QLabel("Current Sky Aspects (Transit → Transit)")
        sky_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(sky_label)

        self.sky_table = QTableWidget(0, 4)
        self.sky_table.setHorizontalHeaderLabels([
            "Planet 1", "Aspect", "Planet 2", "Orb",
        ])
        self.sky_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.sky_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.sky_table)

        self.sky_status_label = QLabel("")
        self.sky_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.sky_status_label)

    def load(self, user_id: str):
        self._user_id = user_id
        self._on_calculate()

    def _set_now(self):
        self.dt_edit.setDateTime(QDateTime.currentDateTime())

    def _on_calculate(self):
        if not self._user_id:
            return
        for w in (self._worker, self._sky_worker, self._windows_worker):
            if w is not None:
                w.cancel()
        date_str = self.dt_edit.dateTime().toString("yyyy-MM-ddTHH:mm:ss")

        self.status_label.setText("Calculating…")
        self._worker = ApiWorker(chart_model.load_transits, self._user_id, date_str)
        self._worker.result.connect(self._on_result)
        self._worker.error.connect(self._on_error)
        self._worker.start()

        self.sky_status_label.setText("Calculating…")
        self._sky_worker = ApiWorker(chart_model.load_sky_aspects, self._user_id, date_str)
        self._sky_worker.result.connect(self._on_sky_result)
        self._sky_worker.error.connect(self._on_sky_error)
        self._sky_worker.start()

        self._windows_worker = ApiWorker(chart_model.load_transit_windows, self._user_id, date_str)
        self._windows_worker.result.connect(self._on_windows_result)
        self._windows_worker.error.connect(lambda _: None)
        self._windows_worker.start()

    def _on_result(self, data: chart_model.TransitData):
        self.status_label.setText(f"{len(data.transits)} active aspect(s) — {data.date[:16]}")
        self._current_transits = data.transits
        self.table.setRowCount(len(data.transits))
        for row, t in enumerate(data.transits):
            clr = ASPECT_COLORS.get(t.aspect)
            cat_clr = _CATEGORY_COLORS.get(t.category, "#888")
            self.table.setItem(row, 0, _table_cell(t.transit_planet))
            self.table.setItem(row, 1, _table_cell(t.aspect.title(), clr))
            self.table.setItem(row, 2, _table_cell(t.natal_planet))
            self.table.setItem(row, 3, _table_cell(f"{t.orb:.2f}°"))
            score_item = _table_cell(f"{t.score:.2f}", cat_clr)
            score_item.setData(Qt.ItemDataRole.UserRole, t.peak_score)
            self.table.setItem(row, 4, score_item)
            self.table.setItem(row, 5, _table_cell(f"{t.transit_position.sign} {t.transit_position.degree:.1f}°"))
        self._apply_sig_filter()

    def _on_sig_toggled(self, checked: bool):
        self._update_sig_btn_style(checked)
        self._apply_sig_filter()

    def _update_sig_btn_style(self, checked: bool):
        self.sig_btn.setText(
            "Significant Transits Only: ON" if checked else "Significant Transits Only: OFF"
        )
        if checked:
            self.sig_btn.setStyleSheet("""
                QPushButton {
                    color: #e0e0e0;
                    background: #2e2e52;
                    border: 1px solid #6666aa;
                    border-radius: 6px;
                    padding-left: 12px;
                    padding-right: 12px;
                    font-weight: bold;
                }
                QPushButton:hover { background: #383870; }
            """)
        else:
            self.sig_btn.setStyleSheet("""
                QPushButton {
                    color: #aaa;
                    background: #2a2a3e;
                    border: 1px solid #444466;
                    border-radius: 6px;
                    padding-left: 12px;
                    padding-right: 12px;
                }
                QPushButton:hover { background: #333352; color: #ccc; }
            """)

    def _apply_sig_filter(self):
        sig_only = self.sig_btn.isChecked()
        for row, t in enumerate(self._current_transits):
            hide = sig_only and t.category not in _SIGNIFICANT_CATEGORIES
            self.table.setRowHidden(row, hide)

    def _on_windows_result(self, windows: list[chart_model.TransitWindowResult]):
        lookup = {(w.transit_planet, w.natal_planet, w.aspect): w.windows for w in windows}
        for row, t in enumerate(self._current_transits):
            ws = lookup.get((t.transit_planet, t.natal_planet, t.aspect), [])
            if ws:
                self.table.setItem(row, 6, _table_cell(chart_model.format_transit_dates(ws)))

    def _on_error(self, msg: str):
        self.status_label.setText(f"Error: {msg}")

    def _on_sky_result(self, aspects: list[chart_model.Aspect]):
        self.sky_status_label.setText(f"{len(aspects)} sky aspect(s)")
        self.sky_table.setRowCount(len(aspects))
        for row, a in enumerate(aspects):
            clr = ASPECT_COLORS.get(a.aspect)
            self.sky_table.setItem(row, 0, _table_cell(a.planet1))
            self.sky_table.setItem(row, 1, _table_cell(a.aspect.title(), clr))
            self.sky_table.setItem(row, 2, _table_cell(a.planet2))
            self.sky_table.setItem(row, 3, _table_cell(f"{a.orb:.2f}°"))

    def _on_sky_error(self, msg: str):
        self.sky_status_label.setText(f"Error: {msg}")
