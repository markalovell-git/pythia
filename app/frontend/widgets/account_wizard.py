from PyQt6.QtCore import Qt, pyqtSignal, QDate, QTime
from PyQt6.QtWidgets import (
    QWizard, QWizardPage, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QCalendarWidget, QTimeEdit,
    QComboBox, QTextEdit, QMessageBox,
)

from app.frontend.models import user_model
from app.frontend import api_client
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


class _BasicInfoPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Basic Information")
        self._username_available = False
        layout = QFormLayout(self)

        self.name_edit = QLineEdit()
        self.username_edit = QLineEdit()
        self.username_status = QLabel()

        layout.addRow("Full name:", self.name_edit)
        layout.addRow("Username:", self.username_edit)
        layout.addRow("", self.username_status)

        self.name_edit.textChanged.connect(lambda _: self.completeChanged.emit())
        self.username_edit.textChanged.connect(self._check_username)

        self.registerField("name*", self.name_edit)
        self.registerField("username*", self.username_edit)

    def _check_username(self, text: str):
        if not text:
            self._username_available = False
            self.username_status.setText("")
            self.completeChanged.emit()
            return
        taken = user_model.username_exists(text)
        self._username_available = not taken
        if taken:
            self.username_status.setText("Username already taken")
            self.username_status.setStyleSheet("color: red;")
        else:
            self.username_status.setText("Available")
            self.username_status.setStyleSheet("color: green;")
        self.completeChanged.emit()

    def isComplete(self) -> bool:
        return (
            bool(self.name_edit.text().strip())
            and bool(self.username_edit.text().strip())
            and self._username_available
        )


class _BirthDatePage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Date & Time of Birth")
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Select your birth date:"))
        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(QDate(1990, 1, 1))
        layout.addWidget(self.calendar)

        time_row = QHBoxLayout()
        time_row.addWidget(QLabel("Birth time:"))
        self.time_edit = QTimeEdit(QTime(12, 0))
        self.time_edit.setDisplayFormat("HH:mm")
        time_row.addWidget(self.time_edit)
        time_row.addStretch()
        layout.addLayout(time_row)

    def birth_datetime_str(self) -> str:
        d = self.calendar.selectedDate()
        t = self.time_edit.time()
        return f"{d.year():04d}-{d.month():02d}-{d.day():02d}T{t.hour():02d}:{t.minute():02d}:00"


class _LocationPage(QWizardPage):
    _coords: tuple[float, float] | None = None

    def __init__(self):
        super().__init__()
        self.setTitle("Birth Location")
        layout = QVBoxLayout(self)

        search_row = QHBoxLayout()
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("e.g. Chicago, IL")
        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self._on_search)
        search_row.addWidget(self.search_edit)
        search_row.addWidget(self.search_btn)
        layout.addLayout(search_row)

        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

        self.tz_label = QLabel("Timezone: —")
        layout.addWidget(self.tz_label)

        self._location_str = ""
        self._lat = 0.0
        self._lon = 0.0
        self._tz = ""

    def _on_search(self):
        query = self.search_edit.text().strip()
        if not query:
            return
        result = api_client.geocode(query)
        if not result:
            self.result_label.setText("Location not found. Try a different search.")
            self.result_label.setStyleSheet("color: red;")
            return
        self._location_str = result["display_name"]
        self._lat = float(result["lat"])
        self._lon = float(result["lon"])

        tz = _tz_from_coords(self._lat, self._lon)
        self._tz = tz or ""

        self.result_label.setText(f"Found: {self._location_str}")
        self.result_label.setStyleSheet("color: green;")
        self.tz_label.setText(f"Timezone: {self._tz or '(unknown — enter manually)'}")
        self.completeChanged.emit()

    def isComplete(self) -> bool:
        return bool(self._location_str) and bool(self._tz)


class _ReviewPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Review")
        self.summary = QLabel()
        self.summary.setWordWrap(True)
        QVBoxLayout(self).addWidget(self.summary)

    def initializePage(self):
        w = self.wizard()
        self.summary.setText(
            f"Name: {w.field('name')}\n"
            f"Username: {w.field('username')}\n"
            f"Birth date/time: {w._date_page.birth_datetime_str()}\n"
            f"Location: {w._location_page._location_str}\n"
            f"Timezone: {w._location_page._tz}"
        )


class AccountWizard(QWizard):
    """Multi-step profile creation wizard.

    After exec() returns Accepted, read created_user_id to get the new user's ID.
    The caller is responsible for navigating to the main window — we don't do it
    from inside accept() to avoid creating windows while a modal dialog is active.
    """

    created_user_id: str | None = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Profile — Pythia")
        self.setMinimumSize(600, 500)

        self._info_page = _BasicInfoPage()
        self._date_page = _BirthDatePage()
        self._location_page = _LocationPage()
        self._review_page = _ReviewPage()

        self.addPage(self._info_page)
        self.addPage(self._date_page)
        self.addPage(self._location_page)
        self.addPage(self._review_page)

    def accept(self):
        payload = {
            "name": self.field("name"),
            "username": self.field("username"),
            "birth_datetime": self._date_page.birth_datetime_str(),
            "birth_timezone": self._location_page._tz,
            "birth_location": self._location_page._location_str,
            "birth_lat": self._location_page._lat,
            "birth_lon": self._location_page._lon,
        }
        log.debug("wizard accept: creating user %s", payload.get("username"))
        try:
            self.created_user_id = user_model.create_user(payload)
            log.debug("wizard accept: user created %s, calculating chart", self.created_user_id)
            from app.frontend.models import chart_model
            chart_model.calculate_chart(self.created_user_id)
            log.debug("wizard accept: chart done, closing wizard")
            super().accept()
            log.debug("wizard accept: complete")
        except Exception as exc:
            log.error("wizard accept failed: %s", exc, exc_info=True)
            QMessageBox.critical(self, "Error", f"Could not create profile:\n{exc}")
