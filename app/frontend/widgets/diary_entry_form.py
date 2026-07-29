import re

from PyQt6.QtCore import Qt, QDate, QTime, pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit,
    QPushButton, QCheckBox, QColorDialog,
    QDateEdit, QTimeEdit, QMessageBox, QScrollArea, QFrame,
)

from app.frontend.models import diary_model, location_model
from app.frontend.widgets.location_picker import LocationPicker
from app.frontend.workers.api_worker import ApiWorker
from app.common.constants import DIARY_CATEGORIES, category_display

_DEFAULT_SEGMENT_COLOR = "255,0,0"

# Date and time hold short, fixed-shape values, so they stay narrow.
_FIELD_WIDTH = 180

# Place names run long ("Dallas, Dallas County, Texas, United States"), so the
# location fields get considerably more room than the date/time pickers.
_WIDE_FIELD_WIDTH = 600

_TIME_RE = re.compile(r"^(\d{1,2}):(\d{2})$")

# 12:01pm — a neutral midday stand-in for "time not known", far enough from
# midnight that a real 00:00 stays distinguishable from an unset one.
_DEFAULT_TIME = QTime(12, 1)

# Categories are split across this many fixed rows rather than free-flowing,
# so the block keeps a stable, balanced shape instead of reflowing as the
# panel is resized.
_CHIP_ROWS = 2

# Pill-shaped toggles. Scoped to the category container so it overrides the
# app-wide QPushButton rules from app/frontend/main.py without touching the
# New/Update/Delete buttons.
_CHIP_STYLE = """
QPushButton {
    background: #1e1e38;
    color: #9a9ac0;
    border: 1px solid #3a3a66;
    border-radius: 11px;
    padding: 4px 12px;
    font-size: 12px;
}
QPushButton:hover {
    border-color: #7a7acc;
    color: #d8d8f4;
}
/* Colour alone signals the lit state: a bolder/larger font would widen the
   chip past the size hint Qt measured when it was unchecked, clipping the
   label. */
QPushButton:checked {
    background: #4a4aa8;
    color: #ffffff;
    border-color: #9a9aee;
}
QPushButton:checked:hover {
    background: #5656c4;
}
"""


def _save_entry(user_id: str, entry_id: str | None, payload: dict,
                 location_text: str, destination_text: str) -> diary_model.DiaryEntry:
    """Runs in a worker thread: create name-only locations for unresolved
    typed names, then create or update the entry."""
    if payload["location_id"] is None and location_text:
        payload["location_id"] = location_model.create_location(location_text).location_id
    if payload["destination_id"] is None and destination_text:
        payload["destination_id"] = location_model.create_location(destination_text).location_id
    if entry_id:
        return diary_model.update_entry(entry_id, payload)
    return diary_model.create_entry(user_id, payload)


class DiaryEntryForm(QWidget):
    """Inline create/edit form for a single diary entry (lower-right panel).

    A permanent, always-visible sibling of the old 'Make New Diary Entry'
    popup: the same fields, but `set_entry()` re-populates them in place as
    the caller steps between entries, instead of a modal being opened per
    entry.
    """

    saved = pyqtSignal(object)   # diary_model.DiaryEntry
    deleted = pyqtSignal(str)    # entry_id

    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._entry: diary_model.DiaryEntry | None = None
        self._segment_color: str | None = None
        self._current_date = QDate.currentDate()
        self._save_worker: ApiWorker | None = None
        self._delete_worker: ApiWorker | None = None
        self._snapshot: tuple | None = None
        self._build_ui()

    # ── Construction ──────────────────────────────────────────────────────────

    def _build_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        inner = QWidget()
        layout = QFormLayout(inner)

        self.category_box = QWidget()
        self.category_box.setStyleSheet(_CHIP_STYLE)
        chip_box = QVBoxLayout(self.category_box)
        chip_box.setContentsMargins(0, 0, 0, 0)
        chip_box.setSpacing(6)
        self._chip_rows = []
        for _ in range(_CHIP_ROWS):
            row = QHBoxLayout()
            row.setSpacing(6)
            chip_box.addLayout(row)
            self._chip_rows.append(row)
        self._chips: dict[str, QPushButton] = {}
        for slug, display in DIARY_CATEGORIES:
            self._add_chip(slug, display)
        self._relayout_chips()
        layout.addRow("Category:", self.category_box)

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("d MMM yyyy")
        self.date_edit.setMaximumWidth(_FIELD_WIDTH)
        layout.addRow("Date:", self.date_edit)

        # Steppable/typable picker, the QTimeEdit counterpart of the date's
        # calendar popup. Every entry has a time; missing or unreadable
        # values default to midnight (see _set_time).
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setMaximumWidth(_FIELD_WIDTH)
        layout.addRow("Time:", self.time_edit)

        self.location_picker = LocationPicker()
        self.location_picker.set_field_width(_WIDE_FIELD_WIDTH)
        layout.addRow("Location:", self.location_picker)

        self.destination_picker = LocationPicker(placeholder="(optional)")
        self.destination_picker.set_field_width(_WIDE_FIELD_WIDTH)
        layout.addRow("Destination:", self.destination_picker)

        segment_row = QHBoxLayout()
        self.segment_check = QCheckBox("Segment Starts")
        self.segment_check.toggled.connect(self._on_segment_toggled)
        self.color_btn = QPushButton("Choose Color")
        self.color_btn.setEnabled(False)
        self.color_btn.clicked.connect(self._on_choose_color)
        segment_row.addWidget(self.segment_check)
        segment_row.addWidget(self.color_btn)
        segment_row.addStretch()
        layout.addRow("", segment_row)

        self.title_edit = QLineEdit()
        layout.addRow("Title:", self.title_edit)

        self.description_edit = QTextEdit()
        self.description_edit.setAcceptRichText(False)
        self.description_edit.setMinimumHeight(140)
        layout.addRow("Description:", self.description_edit)

        self.visuals_edit = QTextEdit()
        self.visuals_edit.setAcceptRichText(False)
        self.visuals_edit.setMaximumHeight(70)
        layout.addRow("Visual cues:", self.visuals_edit)

        scroll.setWidget(inner)
        outer.addWidget(scroll, stretch=1)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.new_btn = QPushButton("New")
        self.new_btn.clicked.connect(self._on_new)
        self.save_btn = QPushButton("Create")
        self.save_btn.setDefault(True)
        self.save_btn.clicked.connect(self._on_save)
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setEnabled(False)
        self.delete_btn.clicked.connect(self._on_delete)
        btn_row.addWidget(self.new_btn)
        btn_row.addWidget(self.save_btn)
        btn_row.addWidget(self.delete_btn)
        outer.addLayout(btn_row)

    # ── Populate / read fields ───────────────────────────────────────────────

    def set_user(self, user_id: str):
        self._user_id = user_id

    def set_entry(self, entry: diary_model.DiaryEntry | None, default_date: QDate):
        """Populate every field from `entry`, or clear them into create mode
        (dated `default_date`) when `entry` is None."""
        self._entry = entry
        self._segment_color = entry.segment_color if entry else None
        self._current_date = (
            QDate.fromString(entry.entry_date, "yyyy-MM-dd") if entry else default_date
        )

        self._set_categories(set(entry.categories) if entry else set())

        self.date_edit.setDate(self._current_date)
        self._set_time(entry.entry_time if entry else None)

        if entry and (entry.location_id or entry.location_name):
            self.location_picker.set_location(entry.location_id, entry.location_name)
        else:
            self.location_picker.set_location(None, "")
        if entry and (entry.destination_id or entry.destination_name):
            self.destination_picker.set_location(entry.destination_id, entry.destination_name)
        else:
            self.destination_picker.set_location(None, "")

        self.segment_check.setChecked(bool(entry and entry.segment_start))
        self._apply_color_swatch()

        self.title_edit.setText(entry.title or "" if entry else "")
        self.description_edit.setPlainText(entry.content if entry else "")
        self.visuals_edit.setPlainText(entry.visual_cues or "" if entry else "")

        self.save_btn.setText("Update" if entry else "Create")
        self.save_btn.setEnabled(True)
        self.delete_btn.setEnabled(entry is not None)
        self._snapshot = self._current_snapshot()

    def _set_time(self, raw: str | None):
        """Load `raw` into the time picker, defaulting to _DEFAULT_TIME.

        Anything QTimeEdit can't represent — a missing time, or legacy
        free-text from the diary.xml import such as "2h" — is discarded in
        favour of the default, which is then written back on the next save.
        """
        match = _TIME_RE.match(raw.strip()) if raw else None
        time = QTime(int(match.group(1)), int(match.group(2))) if match else _DEFAULT_TIME
        self.time_edit.blockSignals(True)
        try:
            self.time_edit.setTime(time)
        finally:
            self.time_edit.blockSignals(False)

    def _time_value(self) -> str:
        return self.time_edit.time().toString("HH:mm")

    def is_dirty(self) -> bool:
        return self._snapshot is not None and self._current_snapshot() != self._snapshot

    def _current_snapshot(self) -> tuple:
        return (
            tuple(sorted(self._checked_categories())),
            self.date_edit.date().toString("yyyy-MM-dd"),
            self._time_value(),
            self.location_picker.text(),
            self.location_picker.location_id(),
            self.destination_picker.text(),
            self.destination_picker.location_id(),
            self.segment_check.isChecked(),
            self._segment_color,
            self.title_edit.text().strip(),
            self.description_edit.toPlainText().strip(),
            self.visuals_edit.toPlainText().strip(),
        )

    def _add_chip(self, slug: str, display: str) -> QPushButton:
        chip = QPushButton(display, self.category_box)
        chip.setCheckable(True)
        chip.setCursor(Qt.CursorShape.PointingHandCursor)
        self._chips[slug] = chip
        return chip

    def _relayout_chips(self):
        """Deal the chips out evenly across _CHIP_ROWS rows.

        Split by count, not pixel width, so each row holds the same number of
        categories — with 11 categories and 2 rows that is 6 then 5. A
        legacy slug adding a 12th chip just rebalances to 6 and 6.
        """
        for row in self._chip_rows:
            while row.count():
                row.takeAt(0)

        chips = list(self._chips.values())
        rows = len(self._chip_rows)
        per_row = -(-len(chips) // rows)  # ceil, so earlier rows take the extra
        for index, chip in enumerate(chips):
            row_index = min(index // per_row, rows - 1)
            self._chip_rows[row_index].addWidget(chip)
        for row in self._chip_rows:
            row.addStretch()

    def _set_categories(self, slugs: set[str]):
        """Light up the chips for `slugs`, adding chips for any unknown slug
        (legacy 'travel' and friends survive a round-trip through the form)."""
        known = {slug for slug, _ in DIARY_CATEGORIES}
        for slug in sorted(slugs - known):
            if slug not in self._chips:
                self._add_chip(slug, category_display(slug))
        changed = False
        for slug, chip in list(self._chips.items()):
            if slug not in known and slug not in slugs:
                # Stale extra chip from a previously shown entry.
                chip.setParent(None)
                chip.deleteLater()
                del self._chips[slug]
                changed = True
                continue
            chip.setChecked(slug in slugs)
        if changed or any(slug not in known for slug in slugs):
            self._relayout_chips()
        self.category_box.updateGeometry()

    def _checked_categories(self) -> list[str]:
        return [slug for slug, chip in self._chips.items() if chip.isChecked()]

    # ── Segment color ─────────────────────────────────────────────────────────

    def _on_segment_toggled(self, checked: bool):
        self.color_btn.setEnabled(checked)
        if checked and self._segment_color is None:
            self._segment_color = _DEFAULT_SEGMENT_COLOR
        self._apply_color_swatch()

    def _on_choose_color(self):
        initial = QColor(*self._parsed_color())
        color = QColorDialog.getColor(initial, self, "Segment Color")
        if color.isValid():
            self._segment_color = f"{color.red()},{color.green()},{color.blue()}"
            self._apply_color_swatch()

    def _parsed_color(self) -> tuple[int, int, int]:
        try:
            r, g, b = (int(p) for p in (self._segment_color or _DEFAULT_SEGMENT_COLOR).split(","))
            return r, g, b
        except ValueError:
            return 255, 0, 0

    def _apply_color_swatch(self):
        if self.segment_check.isChecked():
            r, g, b = self._parsed_color()
            self.color_btn.setStyleSheet(
                f"background-color: rgb({r},{g},{b});"
                f" color: {'black' if r + g + b > 380 else 'white'};"
            )
        else:
            self.color_btn.setStyleSheet("")

    # ── New / Delete / Save ──────────────────────────────────────────────────

    def _on_new(self):
        if self.is_dirty():
            reply = QMessageBox.question(
                self, "Discard Changes",
                "Discard unsaved changes to this entry?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            if reply != QMessageBox.StandardButton.Yes:
                return
        self.set_entry(None, self._current_date)

    def _on_delete(self):
        if not self._entry:
            return
        reply = QMessageBox.question(
            self, "Delete Entry", "Delete this diary entry?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        entry_id = self._entry.entry_id
        self.delete_btn.setEnabled(False)
        self._delete_worker = ApiWorker(diary_model.delete_entry, entry_id)
        self._delete_worker.result.connect(lambda _: self.deleted.emit(entry_id))
        self._delete_worker.error.connect(self._on_delete_error)
        self._delete_worker.start()

    def _on_delete_error(self, msg: str):
        self.delete_btn.setEnabled(True)
        QMessageBox.warning(self, "Delete Failed", msg)

    def _on_save(self):
        if not self._user_id:
            return
        categories = self._checked_categories()
        description = self.description_edit.toPlainText().strip()
        location_text = self.location_picker.text()

        missing = []
        if not categories:
            missing.append("at least one Category")
        if not location_text:
            missing.append("Location")
        if not description:
            missing.append("Description")
        if missing:
            QMessageBox.warning(self, "Missing Fields", "Please provide: " + ", ".join(missing))
            return

        segment = self.segment_check.isChecked()
        payload = {
            "entry_date": self.date_edit.date().toString("yyyy-MM-dd"),
            "content": description,
            "title": self.title_edit.text().strip() or None,
            "visual_cues": self.visuals_edit.toPlainText().strip() or None,
            "categories": categories,
            "entry_time": self._time_value(),
            "location_id": self.location_picker.location_id(),
            "destination_id": self.destination_picker.location_id(),
            "segment_start": segment,
            "segment_color": (self._segment_color or _DEFAULT_SEGMENT_COLOR) if segment else None,
        }

        self.save_btn.setEnabled(False)
        prior_text = self.save_btn.text()
        self.save_btn.setText("Saving…")
        self._save_worker = ApiWorker(
            _save_entry,
            self._user_id,
            self._entry.entry_id if self._entry else None,
            payload,
            location_text,
            self.destination_picker.text(),
        )
        self._save_worker.result.connect(self._on_saved)
        self._save_worker.error.connect(lambda msg: self._on_save_error(msg, prior_text))
        self._save_worker.start()

    def _on_saved(self, entry: diary_model.DiaryEntry):
        self.save_btn.setEnabled(True)
        self.saved.emit(entry)

    def _on_save_error(self, msg: str, prior_text: str):
        self.save_btn.setEnabled(True)
        self.save_btn.setText(prior_text)
        QMessageBox.warning(self, "Save Failed", msg)
