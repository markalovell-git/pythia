from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QGroupBox, QLineEdit, QMessageBox,
)
import httpx

from app.frontend.models import chart_model, user_model
from app.frontend.workers.api_worker import ApiWorker
from app.frontend import desktop_integration
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
            detail = ""
        raise RuntimeError(detail or f"HTTP {e.response.status_code}")


_AI_PROVIDERS = [
    ("Ollama (local)",    "ollama"),
    ("Claude (Anthropic)", "claude"),
    ("ChatGPT (OpenAI)",  "openai"),
]


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

        # ── AI Interpreter ────────────────────────────────────────────────────
        ai_group = QGroupBox("AI Interpreter")
        ai_layout = QVBoxLayout(ai_group)

        provider_row = QHBoxLayout()
        provider_row.addWidget(QLabel("Provider:"))
        self.ai_provider_combo = QComboBox()
        for label, key in _AI_PROVIDERS:
            self.ai_provider_combo.addItem(label, userData=key)
        self.ai_provider_combo.currentIndexChanged.connect(self._on_ai_provider_changed)
        provider_row.addWidget(self.ai_provider_combo)
        provider_row.addStretch()
        ai_layout.addLayout(provider_row)

        # API key row (Claude / OpenAI)
        self._key_row = QHBoxLayout()
        self._key_row.addWidget(QLabel("API Key:"))
        self.ai_key_edit = QLineEdit()
        self.ai_key_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.ai_key_edit.setPlaceholderText("sk-…")
        self._key_row.addWidget(self.ai_key_edit)
        ai_layout.addLayout(self._key_row)

        # Ollama URL row
        self._url_row = QHBoxLayout()
        self._url_row.addWidget(QLabel("Ollama URL:"))
        self.ollama_url_edit = QLineEdit()
        self.ollama_url_edit.setPlaceholderText("http://localhost:11434")
        self._url_row.addWidget(self.ollama_url_edit)
        ai_layout.addLayout(self._url_row)

        # Ollama model row
        self._model_row = QHBoxLayout()
        self._model_row.addWidget(QLabel("Model:"))
        self.ollama_model_edit = QLineEdit()
        self.ollama_model_edit.setPlaceholderText("qwen3:14b")
        self._model_row.addWidget(self.ollama_model_edit)
        ai_layout.addLayout(self._model_row)

        save_ai_btn = QPushButton("Save")
        save_ai_btn.clicked.connect(self._on_save_ai)
        ai_layout.addWidget(save_ai_btn)
        layout.addWidget(ai_group)

        # ── Desktop (AppImage only) ───────────────────────────────────────────
        if desktop_integration.is_available():
            desktop_group = QGroupBox("Desktop")
            desktop_layout = QVBoxLayout(desktop_group)
            self.desktop_btn = QPushButton()
            self.desktop_btn.clicked.connect(self._on_toggle_desktop)
            desktop_layout.addWidget(self.desktop_btn)
            hint = QLabel(
                "Add Pythia to your applications menu so you can launch and pin "
                "it like a normal app."
            )
            hint.setWordWrap(True)
            hint.setStyleSheet("color: #7070a0; font-size: 11px;")
            desktop_layout.addWidget(hint)
            layout.addWidget(desktop_group)
            self._refresh_desktop_btn()

        account_group = QGroupBox("Account")
        account_layout = QVBoxLayout(account_group)
        delete_btn = QPushButton("Delete My Account…")
        delete_btn.setStyleSheet("color: red;")
        delete_btn.clicked.connect(self._on_delete_account)
        account_layout.addWidget(delete_btn)
        layout.addWidget(account_group)

        layout.addStretch()

    def _refresh_desktop_btn(self):
        installed = desktop_integration.is_installed()
        self.desktop_btn.setText(
            "Remove from Applications Menu" if installed
            else "Add to Applications Menu"
        )

    def _on_toggle_desktop(self):
        if desktop_integration.is_installed():
            ok, msg = desktop_integration.uninstall()
        else:
            ok, msg = desktop_integration.install()
        self._refresh_desktop_btn()
        if ok:
            QMessageBox.information(self, "Desktop", msg)
        else:
            QMessageBox.warning(self, "Desktop", f"Couldn't update the menu entry:\n\n{msg}")

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
        ai = chart_model.get_ai_settings(user_id)
        idx = self.ai_provider_combo.findData(ai["ai_provider"])
        if idx >= 0:
            self.ai_provider_combo.setCurrentIndex(idx)
        self.ollama_url_edit.setText(ai.get("ollama_url") or "http://localhost:11434")
        self.ollama_model_edit.setText(ai.get("ollama_model") or "llama3.2")
        # Populate the key field based on current provider
        provider = ai["ai_provider"]
        if provider == "claude":
            self.ai_key_edit.setText(ai.get("anthropic_key") or "")
        elif provider == "openai":
            self.ai_key_edit.setText(ai.get("openai_key") or "")
        self._on_ai_provider_changed()

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

    def _on_ai_provider_changed(self, _index: int = 0):
        provider = self.ai_provider_combo.currentData()
        is_ollama = (provider == "ollama")
        # Show/hide relevant rows
        for i in range(self._key_row.count()):
            w = self._key_row.itemAt(i).widget()
            if w:
                w.setVisible(not is_ollama)
        for i in range(self._url_row.count()):
            w = self._url_row.itemAt(i).widget()
            if w:
                w.setVisible(is_ollama)
        for i in range(self._model_row.count()):
            w = self._model_row.itemAt(i).widget()
            if w:
                w.setVisible(is_ollama)

    def _on_save_ai(self):
        if not self._user_id:
            return
        provider = self.ai_provider_combo.currentData()
        key = self.ai_key_edit.text().strip() or None
        chart_model.set_ai_settings(
            self._user_id,
            ai_provider=provider,
            anthropic_key=key if provider == "claude" else None,
            openai_key=key if provider == "openai" else None,
            ollama_url=self.ollama_url_edit.text().strip() or None,
            ollama_model=self.ollama_model_edit.text().strip() or None,
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
