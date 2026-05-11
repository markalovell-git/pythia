from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QDateTimeEdit, QHeaderView,
)

from app.frontend.models import chart_model
from app.frontend.workers.api_worker import ApiWorker

ASPECT_COLORS = {
    "conjunction": "#FFD700",
    "sextile": "#90EE90",
    "square": "#FF6B6B",
    "trine": "#66BB6A",
    "opposition": "#FF4500",
}


class TransitView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._worker: ApiWorker | None = None
        self._sky_worker: ApiWorker | None = None
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
        controls.addStretch()
        layout.addLayout(controls)

        transit_label = QLabel("Transit → Natal")
        transit_label.setStyleSheet("font-weight: bold; margin-top: 6px;")
        layout.addWidget(transit_label)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels([
            "Transit Planet", "Aspect", "Natal Planet", "Orb", "Transit Position",
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

    def _on_result(self, data: chart_model.TransitData):
        self.status_label.setText(f"{len(data.transits)} active aspect(s) — {data.date[:16]}")
        self.table.setRowCount(len(data.transits))
        for row, t in enumerate(data.transits):
            clr = ASPECT_COLORS.get(t.aspect)

            def _cell(text, color=None):
                item = QTableWidgetItem(text)
                if color:
                    item.setForeground(QColor(color))
                return item

            self.table.setItem(row, 0, _cell(t.transit_planet))
            self.table.setItem(row, 1, _cell(t.aspect.title(), clr))
            self.table.setItem(row, 2, _cell(t.natal_planet))
            self.table.setItem(row, 3, _cell(f"{t.orb:.2f}°"))
            self.table.setItem(row, 4, _cell(f"{t.transit_position.sign} {t.transit_position.degree:.1f}°"))

    def _on_error(self, msg: str):
        self.status_label.setText(f"Error: {msg}")

    def _on_sky_result(self, aspects: list):
        self.sky_status_label.setText(f"{len(aspects)} sky aspect(s)")
        self.sky_table.setRowCount(len(aspects))
        for row, a in enumerate(aspects):
            clr = ASPECT_COLORS.get(a.aspect)

            def _cell(text, color=None):
                item = QTableWidgetItem(text)
                if color:
                    item.setForeground(QColor(color))
                return item

            self.sky_table.setItem(row, 0, _cell(a.planet1))
            self.sky_table.setItem(row, 1, _cell(a.aspect.title(), clr))
            self.sky_table.setItem(row, 2, _cell(a.planet2))
            self.sky_table.setItem(row, 3, _cell(f"{a.orb:.2f}°"))

    def _on_sky_error(self, msg: str):
        self.sky_status_label.setText(f"Error: {msg}")
