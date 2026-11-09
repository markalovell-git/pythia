import bisect
import os
import re
from pathlib import Path

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QColor, QTextCharFormat, QFont
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCalendarWidget, QSplitter, QMessageBox, QFileDialog,
)

from app.frontend.models import diary_model
from app.frontend.widgets.diary_entry_form import DiaryEntryForm
from app.frontend.workers.api_worker import ApiWorker


class DiaryView(QWidget):
    """Calendar on the left; on the right, a permanently-visible entry form
    stepped through with arrow buttons instead of a popup + list.

    All of a user's entries are loaded once, in the same (date, time,
    creation-order) sequence the arrows walk through — see
    `diary_model.order_entries`. Navigating is just moving an index into that
    list, so a day with several entries is stepped through internally, and
    the left/right arrows only cross to a neighbouring day once the current
    day's entries are exhausted.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._load_worker: ApiWorker | None = None
        self._dates_worker: ApiWorker | None = None
        self._import_worker: ApiWorker | None = None
        self._export_worker: ApiWorker | None = None
        self._highlighted: set[QDate] = set()
        self._entries: list[diary_model.DiaryEntry] = []
        self._index: int = -1
        # Anchor date used to find neighbouring entries when `_index == -1`
        # (i.e. the calendar is sitting on a date with no entry of its own).
        self._anchor_date: QDate = QDate.currentDate()
        self._suppress_calendar = False
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Diary")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.import_btn = QPushButton("Import XML…")
        self.import_btn.clicked.connect(self._on_import_clicked)
        title_row = QHBoxLayout()
        title_row.addWidget(title)
        title_row.addStretch()
        title_row.addWidget(self.import_btn)
        self.export_btn = QPushButton("Export XML…")
        self.export_btn.clicked.connect(self._on_export_clicked)
        title_row.addWidget(self.export_btn)
        layout.addLayout(title_row)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left: calendar
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.addWidget(QLabel("Select a date:"))
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self._on_date_changed)
        left_layout.addWidget(self.calendar)
        splitter.addWidget(left)

        # Right: arrow nav row above the inline entry form
        right = QWidget()
        right_layout = QVBoxLayout(right)

        nav_row = QHBoxLayout()
        self.prev_btn = QPushButton("◀")
        self.prev_btn.clicked.connect(lambda: self._go(-1))
        self.position_label = QLabel("")
        self.position_label.setStyleSheet("font-weight: bold;")
        self.position_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.next_btn = QPushButton("▶")
        self.next_btn.clicked.connect(lambda: self._go(1))
        nav_row.addWidget(self.prev_btn)
        nav_row.addWidget(self.position_label, stretch=1)
        nav_row.addWidget(self.next_btn)
        right_layout.addLayout(nav_row)

        self.form = DiaryEntryForm()
        self.form.saved.connect(self._on_saved)
        self.form.deleted.connect(self._on_deleted)
        right_layout.addWidget(self.form, stretch=1)

        splitter.addWidget(right)
        splitter.setSizes([300, 500])
        layout.addWidget(splitter)

    def load(self, user_id: str):
        self._user_id = user_id
        self.form.set_user(user_id)
        self._reload_entries()
        self._refresh_highlights()

    # ── Loading & navigation ─────────────────────────────────────────────────

    def _reload_entries(self, select_entry_id: str | None = None):
        if not self._user_id:
            return
        if self._load_worker is not None:
            self._load_worker.cancel()
        self._load_worker = ApiWorker(diary_model.get_entries, self._user_id)
        self._load_worker.result.connect(
            lambda entries: self._on_entries_loaded(entries, select_entry_id)
        )
        self._load_worker.start()

    def _on_entries_loaded(self, entries: list[diary_model.DiaryEntry], select_entry_id: str | None):
        self._entries = diary_model.order_entries(entries)
        idx = -1
        if select_entry_id:
            idx = next((i for i, e in enumerate(self._entries) if e.entry_id == select_entry_id), -1)
        if idx == -1:
            idx = self._index_for_date(self.calendar.selectedDate())
        self._index = idx
        if idx == -1:
            self._anchor_date = self.calendar.selectedDate()
        self._show_current()

    def _index_for_date(self, date: QDate) -> int:
        """Index of the first entry on `date`, or -1 if none."""
        date_str = date.toString("yyyy-MM-dd")
        return next((i for i, e in enumerate(self._entries) if e.entry_date == date_str), -1)

    def _entry_dates(self) -> list[str]:
        return [e.entry_date for e in self._entries]

    def _go(self, delta: int):
        if not self._entries or self._confirm_discard_if_dirty():
            return
        if self._index == -1:
            # Currently anchored on a date with no entry of its own: jump to
            # the nearest entry in the requested direction, if any.
            pos = bisect.bisect_left(self._entry_dates(), self._anchor_date.toString("yyyy-MM-dd"))
            new_index = pos if delta > 0 else pos - 1
        else:
            new_index = self._index + delta
        if not (0 <= new_index < len(self._entries)):
            return
        self._index = new_index
        self._show_current()

    def _show_current(self):
        if self._index >= 0:
            entry = self._entries[self._index]
            date = QDate.fromString(entry.entry_date, "yyyy-MM-dd")
        else:
            entry = None
            date = self._anchor_date

        self._suppress_calendar = True
        try:
            if self.calendar.selectedDate() != date:
                self.calendar.setSelectedDate(date)
        finally:
            self._suppress_calendar = False

        label = date.toString("dddd, MMMM d, yyyy")
        if entry:
            date_str = entry.entry_date
            day_indices = [i for i, e in enumerate(self._entries) if e.entry_date == date_str]
            if len(day_indices) > 1:
                position = day_indices.index(self._index) + 1
                label += f"  ({position} of {len(day_indices)})"
        self.position_label.setText(label)

        self.form.set_entry(entry, date)

        if self._index >= 0:
            self.prev_btn.setEnabled(self._index > 0)
            self.next_btn.setEnabled(self._index < len(self._entries) - 1)
        else:
            pos = bisect.bisect_left(self._entry_dates(), date.toString("yyyy-MM-dd"))
            self.prev_btn.setEnabled(pos > 0)
            self.next_btn.setEnabled(pos < len(self._entries))

    # ── Calendar clicks ──────────────────────────────────────────────────────

    def _on_date_changed(self):
        if not self._user_id or self._suppress_calendar:
            return
        if self._confirm_discard_if_dirty():
            # Snap the calendar back to the date actually being shown.
            self._suppress_calendar = True
            try:
                current = (
                    QDate.fromString(self._entries[self._index].entry_date, "yyyy-MM-dd")
                    if self._index >= 0 else self._anchor_date
                )
                self.calendar.setSelectedDate(current)
            finally:
                self._suppress_calendar = False
            return
        date = self.calendar.selectedDate()
        self._index = self._index_for_date(date)
        if self._index == -1:
            self._anchor_date = date
        self._show_current()

    def _confirm_discard_if_dirty(self) -> bool:
        """Returns True if navigation should be cancelled (user kept editing)."""
        if not self.form.is_dirty():
            return False
        reply = QMessageBox.question(
            self, "Discard Changes",
            "Discard unsaved changes to this entry?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        return reply != QMessageBox.StandardButton.Yes

    # ── Form signals ─────────────────────────────────────────────────────────

    def _on_saved(self, entry: diary_model.DiaryEntry):
        self._reload_entries(select_entry_id=entry.entry_id)
        self._refresh_highlights()

    def _on_deleted(self, entry_id: str):
        # Land on the entry that will occupy this slot once the deleted one
        # is gone (i.e. the "next" entry), or the new last entry if it was
        # the final one.
        landing_index = min(self._index, len(self._entries) - 2)
        landing_id = None
        if 0 <= landing_index < len(self._entries):
            remaining = [e for e in self._entries if e.entry_id != entry_id]
            if 0 <= landing_index < len(remaining):
                landing_id = remaining[landing_index].entry_id
        self._reload_entries(select_entry_id=landing_id)
        self._refresh_highlights()

    # ── XML import ───────────────────────────────────────────────────────────

    def _on_import_clicked(self):
        if not self._user_id or self._confirm_discard_if_dirty():
            return
        path, _ = QFileDialog.getOpenFileName(
            self, "Import Diary XML", "", "XML files (*.xml);;All files (*)"
        )
        if not path:
            return
        try:
            xml_text = Path(path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            QMessageBox.critical(self, "Import Failed", f"Could not read the file:\n{e}")
            return
        reply = QMessageBox.warning(
            self, "Replace All Diary Entries",
            f"This will permanently delete all {len(self._entries)} current diary "
            f"entries for this profile and replace them with the entries in "
            f"{Path(path).name}.\n\nThis cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Cancel,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        self.import_btn.setEnabled(False)
        self._import_worker = ApiWorker(diary_model.import_entries, self._user_id, xml_text)
        self._import_worker.result.connect(self._on_import_done)
        self._import_worker.error.connect(self._on_import_error)
        self._import_worker.start()

    def _on_import_done(self, result: dict):
        self.import_btn.setEnabled(True)
        self._reload_entries()
        self._refresh_highlights()
        message = f"Imported {result['imported']} entries, replacing {result['deleted']}."
        if result["month_only_dates"]:
            message += (
                f"\n\n{result['month_only_dates']} entries gave only a month, "
                "so they were set to the 1st of that month."
            )
        QMessageBox.information(self, "Import Complete", message)

    def _on_import_error(self, msg: str):
        self.import_btn.setEnabled(True)
        # Reload anyway: after a client-side timeout the import may still have
        # completed, so show what's really stored.
        self._reload_entries()
        self._refresh_highlights()
        QMessageBox.critical(self, "Import Failed", f"The diary was not imported:\n{msg}")

    # ── XML export ───────────────────────────────────────────────────────────

    def _on_export_clicked(self):
        if not self._user_id:
            return
        if self.form.is_dirty():
            reply = QMessageBox.question(
                self, "Unsaved Changes",
                "This entry has unsaved changes, which won't be in the export. Export anyway?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
            )
            if reply != QMessageBox.StandardButton.Yes:
                return
        self.export_btn.setEnabled(False)
        self._export_worker = ApiWorker(diary_model.export_entries, self._user_id)
        self._export_worker.result.connect(self._on_export_ready)
        self._export_worker.error.connect(self._on_export_error)
        self._export_worker.start()

    def _on_export_ready(self, result: dict):
        self.export_btn.setEnabled(True)
        if not result["exported"]:
            QMessageBox.information(self, "Nothing to Export", "This profile has no diary entries.")
            return
        username = re.sub(r"[^\w-]+", "_", result["username"]).strip("_") or "user"
        date_str = QDate.currentDate().toString("yyyy-MM-dd")
        path, _ = QFileDialog.getSaveFileName(
            self, "Export Diary XML",
            str(Path.home() / f"diary_{username}_{date_str}.xml"),
            "XML files (*.xml);;All files (*)",
        )
        if not path:
            return
        if not Path(path).suffix:
            path += ".xml"
        # Write beside the target, then swap, so a failed write can't damage
        # an earlier backup being overwritten.
        tmp_path = f"{path}.tmp"
        try:
            Path(tmp_path).write_text(result["xml"], encoding="utf-8")
            os.replace(tmp_path, path)
        except OSError as e:
            Path(tmp_path).unlink(missing_ok=True)
            QMessageBox.critical(self, "Export Failed", f"Could not write the file:\n{e}")
            return
        QMessageBox.information(
            self, "Export Complete", f"Exported {result['exported']} entries to:\n{path}"
        )

    def _on_export_error(self, msg: str):
        self.export_btn.setEnabled(True)
        QMessageBox.critical(self, "Export Failed", f"The diary was not exported:\n{msg}")

    # ── Calendar highlighting ─────────────────────────────────────────────────

    def _refresh_highlights(self):
        if not self._user_id:
            return
        if self._dates_worker is not None:
            self._dates_worker.cancel()
        self._dates_worker = ApiWorker(diary_model.dates_with_entries, self._user_id)
        self._dates_worker.result.connect(self._on_dates_loaded)
        self._dates_worker.start()

    def _on_dates_loaded(self, date_strs: set[str]):
        for old in self._highlighted:
            self.calendar.setDateTextFormat(old, QTextCharFormat())
        self._highlighted.clear()
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Bold)
        fmt.setBackground(QColor(255, 235, 175))
        for date_str in date_strs:
            date = QDate.fromString(date_str, "yyyy-MM-dd")
            if date.isValid():
                self.calendar.setDateTextFormat(date, fmt)
                self._highlighted.add(date)
