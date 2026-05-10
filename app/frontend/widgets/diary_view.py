from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCalendarWidget, QTextEdit, QSplitter, QMessageBox,
)

from app.frontend.models import diary_model
from app.frontend.workers.api_worker import ApiWorker


class DiaryView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._current_entry: diary_model.DiaryEntry | None = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Diary")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left: calendar
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.addWidget(QLabel("Select a date:"))
        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self._on_date_changed)
        left_layout.addWidget(self.calendar)
        splitter.addWidget(left)

        # Right: editor
        right = QWidget()
        right_layout = QVBoxLayout(right)
        self.date_label = QLabel("")
        self.date_label.setStyleSheet("font-weight: bold;")
        right_layout.addWidget(self.date_label)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Write your thoughts for this day…")
        right_layout.addWidget(self.editor)

        btn_row = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self._on_save)
        self.delete_btn = QPushButton("Delete Entry")
        self.delete_btn.clicked.connect(self._on_delete)
        btn_row.addWidget(self.save_btn)
        btn_row.addWidget(self.delete_btn)
        btn_row.addStretch()
        right_layout.addLayout(btn_row)

        splitter.addWidget(right)
        splitter.setSizes([300, 500])
        layout.addWidget(splitter)

    def load(self, user_id: str):
        self._user_id = user_id
        self._on_date_changed()

    def _on_date_changed(self):
        if not self._user_id:
            return
        date = self.calendar.selectedDate()
        date_str = date.toString("yyyy-MM-dd")
        self.date_label.setText(date.toString("dddd, MMMM d, yyyy"))
        worker = ApiWorker(diary_model.get_entries, self._user_id, date_str)
        worker.result.connect(self._on_entries_loaded)
        worker.start()

    def _on_entries_loaded(self, entries: list[diary_model.DiaryEntry]):
        self._current_entry = entries[0] if entries else None
        self.editor.setPlainText(self._current_entry.content if self._current_entry else "")
        self.delete_btn.setEnabled(self._current_entry is not None)

    def _on_save(self):
        if not self._user_id:
            return
        content = self.editor.toPlainText().strip()
        date_str = self.calendar.selectedDate().toString("yyyy-MM-dd")
        if self._current_entry:
            worker = ApiWorker(diary_model.update_entry, self._current_entry.entry_id, content)
        else:
            worker = ApiWorker(diary_model.create_entry, self._user_id, date_str, content)
        worker.result.connect(lambda entry: self._on_entries_loaded([entry]))
        worker.error.connect(lambda msg: QMessageBox.warning(self, "Error", msg))
        worker.start()

    def _on_delete(self):
        if not self._current_entry:
            return
        reply = QMessageBox.question(
            self, "Delete Entry", "Delete this diary entry?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            worker = ApiWorker(diary_model.delete_entry, self._current_entry.entry_id)
            worker.result.connect(lambda _: self._on_entries_loaded([]))
            worker.start()
