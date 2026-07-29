from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QCompleter,
)

from app.frontend import api_client
from app.frontend.models import location_model
from app.frontend.workers.api_worker import ApiWorker
from app.common.logging_config import get_logger

log = get_logger(__name__)

try:
    from timezonefinder import TimezoneFinder
    _tf = TimezoneFinder()
    def _tz_from_coords(lat: float, lon: float) -> str | None:
        return _tf.timezone_at(lat=lat, lng=lon)
except ImportError:
    _tf = None
    def _tz_from_coords(lat: float, lon: float) -> str | None:
        return None


class LocationPicker(QWidget):
    """Searchable picker over saved locations.

    Picking an existing location reuses its row; "Search" geocodes the typed
    text via Nominatim and saves the result (with coordinates + timezone) as a
    new location. Text typed without searching has no ``location_id()`` — the
    consumer saves it name-only (offline-safe), coordinates backfillable later.
    """

    changed = pyqtSignal()

    def __init__(self, placeholder: str = "e.g. Chicago, IL", parent=None):
        super().__init__(parent)
        self._location_id: str | None = None
        self._load_worker: ApiWorker | None = None
        self._geocode_worker: ApiWorker | None = None
        self._save_worker: ApiWorker | None = None

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        row = QHBoxLayout()
        self.combo = QComboBox()
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.combo.lineEdit().setPlaceholderText(placeholder)
        self.combo.setCurrentIndex(-1)
        self.combo.activated.connect(self._on_picked)
        self.combo.editTextChanged.connect(self._on_text_edited)
        row.addWidget(self.combo, stretch=1)

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self._on_search)
        row.addWidget(self.search_btn)
        # Absorbs leftover width so Search stays beside a width-capped combo
        # (see set_field_width) instead of a gap opening between them.
        row.addStretch()
        layout.addLayout(row)

        self.status_label = QLabel("")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

        self._load_locations()

    # ── Public API ────────────────────────────────────────────────────────────

    def set_field_width(self, width: int):
        """Cap the combo's width (the Search button keeps its natural size)."""
        self.combo.setMaximumWidth(width)

    def location_id(self) -> str | None:
        return self._location_id

    def text(self) -> str:
        return self.combo.currentText().strip()

    def set_location(self, location_id: str | None, name: str | None):
        # Block signals so editTextChanged doesn't clear the id we're setting.
        self.combo.blockSignals(True)
        self.combo.setEditText(name or "")
        self.combo.blockSignals(False)
        self._location_id = location_id
        self.status_label.setText("")

    # ── Saved-locations list ──────────────────────────────────────────────────

    def _load_locations(self):
        if self._load_worker is not None:
            self._load_worker.cancel()
        self._load_worker = ApiWorker(location_model.search_locations, "")
        self._load_worker.result.connect(self._on_locations_loaded)
        self._load_worker.error.connect(lambda msg: log.warning("Location list failed: %s", msg))
        self._load_worker.start()

    def _on_locations_loaded(self, locations: list):
        current = self.combo.currentText()
        self.combo.blockSignals(True)
        self.combo.clear()
        for loc in locations:
            self.combo.addItem(loc.name, loc.location_id)
        self.combo.setCurrentIndex(-1)
        self.combo.setEditText(current)
        self.combo.blockSignals(False)

        completer = QCompleter([loc.name for loc in locations], self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.combo.setCompleter(completer)

    def _on_picked(self, index: int):
        self._location_id = self.combo.itemData(index)
        self.status_label.setText("")
        self.changed.emit()

    def _on_text_edited(self, text: str):
        # Typing invalidates the previously resolved id unless it still matches.
        idx = self.combo.findText(text, Qt.MatchFlag.MatchFixedString)
        self._location_id = self.combo.itemData(idx) if idx >= 0 else None
        self.changed.emit()

    # ── Geocode search ────────────────────────────────────────────────────────

    def _on_search(self):
        query = self.text()
        if not query:
            return
        if self._geocode_worker is not None:
            self._geocode_worker.cancel()
        self.search_btn.setEnabled(False)
        self.status_label.setText("Searching…")
        self.status_label.setStyleSheet("color: #888;")
        self._geocode_worker = ApiWorker(api_client.geocode, query)
        self._geocode_worker.result.connect(self._on_geocode_result)
        self._geocode_worker.error.connect(self._on_geocode_error)
        self._geocode_worker.start()

    def _on_geocode_result(self, result):
        if not result:
            self.search_btn.setEnabled(True)
            self.status_label.setText("Location not found. Try a different search.")
            self.status_label.setStyleSheet("color: red;")
            return
        name = result["display_name"]
        lat = float(result["lat"])
        lon = float(result["lon"])
        tz = _tz_from_coords(lat, lon)
        self._save_worker = ApiWorker(location_model.create_location, name, lat, lon, tz)
        self._save_worker.result.connect(self._on_location_saved)
        self._save_worker.error.connect(self._on_geocode_error)
        self._save_worker.start()

    def _on_location_saved(self, loc):
        self.search_btn.setEnabled(True)
        self.combo.blockSignals(True)
        self.combo.setEditText(loc.name)
        self.combo.blockSignals(False)
        self._location_id = loc.location_id
        self.status_label.setText(f"Found: {loc.name}")
        self.status_label.setStyleSheet("color: green;")
        self._load_locations()
        self.changed.emit()

    def _on_geocode_error(self, msg: str):
        self.search_btn.setEnabled(True)
        self.status_label.setText(f"Search failed: {msg}")
        self.status_label.setStyleSheet("color: red;")
