from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QGroupBox, QMessageBox,
)
import httpx

from app.frontend.models import chart_model, user_model
from app.frontend.workers.api_worker import ApiWorker
from app.common.constants import VALID_ZODIAC_SYSTEMS, VALID_HOUSE_SYSTEMS

_HOUSE_SYSTEM_LABELS = {"placidus": "Placidus", "whole_sign": "Whole Sign"}


def _calculate_chart_detail(user_id: str) -> chart_model.ChartData:
    """Run calculate_chart and convert HTTPStatusError detail into a plain RuntimeError."""
    try:
        return chart_model.calculate_chart(user_id)
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("detail", "")
        except Exception:
            detail = e.response.text
        raise RuntimeError(detail or str(e))


class SettingsView(QWidget):
    user_deleted = pyqtSignal()
    chart_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._loaded_house: str = "placidus"
        self._house_worker: ApiWorker | None = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        title = QLabel("Settings")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        zodiac_group = QGroupBox("Zodiac System")
        zodiac_layout = QHBoxLayout(zodiac_group)
        self.zodiac_combo = QComboBox()
        self.zodiac_combo.addItems(sorted(VALID_ZODIAC_SYSTEMS))
        self.save_zodiac_btn = QPushButton("Save")
        self.save_zodiac_btn.clicked.connect(self._on_save_zodiac)
        zodiac_layout.addWidget(QLabel("System:"))
        zodiac_layout.addWidget(self.zodiac_combo)
        zodiac_layout.addWidget(self.save_zodiac_btn)
        zodiac_layout.addStretch()
        layout.addWidget(zodiac_group)

        house_group = QGroupBox("House System")
        house_layout = QHBoxLayout(house_group)
        self.house_combo = QComboBox()
        for key in ("placidus", "whole_sign"):
            self.house_combo.addItem(_HOUSE_SYSTEM_LABELS[key], userData=key)
        self.save_house_btn = QPushButton("Save")
        self.save_house_btn.clicked.connect(self._on_save_house)
        house_layout.addWidget(QLabel("System:"))
        house_layout.addWidget(self.house_combo)
        house_layout.addWidget(self.save_house_btn)
        house_layout.addStretch()
        layout.addWidget(house_group)

        account_group = QGroupBox("Account")
        account_layout = QVBoxLayout(account_group)
        delete_btn = QPushButton("Delete My Account…")
        delete_btn.setStyleSheet("color: red;")
        delete_btn.clicked.connect(self._on_delete_account)
        account_layout.addWidget(delete_btn)
        layout.addWidget(account_group)

        layout.addStretch()

    def load(self, user_id: str):
        self._user_id = user_id
        current_zodiac = chart_model.get_zodiac_system(user_id)
        idx = self.zodiac_combo.findText(current_zodiac)
        if idx >= 0:
            self.zodiac_combo.setCurrentIndex(idx)
        self._loaded_house = chart_model.get_house_system(user_id)
        idx = self.house_combo.findData(self._loaded_house)
        if idx >= 0:
            self.house_combo.setCurrentIndex(idx)

    def _on_save_zodiac(self):
        if not self._user_id:
            return
        chart_model.set_zodiac_system(self._user_id, self.zodiac_combo.currentText())
        self.chart_changed.emit()

    def _on_save_house(self):
        if not self._user_id:
            return
        new_value = self.house_combo.currentData()
        previous = self._loaded_house
        chart_model.set_house_system(self._user_id, new_value)
        self.save_house_btn.setEnabled(False)
        if self._house_worker is not None:
            self._house_worker.cancel()
        self._house_worker = ApiWorker(_calculate_chart_detail, self._user_id)
        self._house_worker.result.connect(lambda _: self._on_house_saved(new_value))
        self._house_worker.error.connect(lambda msg: self._on_house_failed(previous, new_value, msg))
        self._house_worker.start()

    def _on_house_saved(self, new_value: str):
        self.save_house_btn.setEnabled(True)
        self._loaded_house = new_value
        self.chart_changed.emit()

    def _on_house_failed(self, previous: str, new_value: str, msg: str):
        self.save_house_btn.setEnabled(True)
        chart_model.set_house_system(self._user_id, previous)
        idx = self.house_combo.findData(previous)
        if idx >= 0:
            self.house_combo.setCurrentIndex(idx)
        QMessageBox.warning(
            self,
            "House system unavailable",
            f"Couldn't switch to {_HOUSE_SYSTEM_LABELS[new_value]}:\n\n{msg}",
        )

    def _on_delete_account(self):
        reply = QMessageBox.question(
            self,
            "Delete Account",
            "Permanently delete your account and all data? This cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            user_model.delete_user(self._user_id)
            self.user_deleted.emit()
