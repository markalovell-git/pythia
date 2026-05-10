from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QMessageBox,
)

from app.frontend.models import user_model


class WelcomeWidget(QWidget):
    user_selected = pyqtSignal(str)   # emits user_id
    create_profile = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Pythia")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 32px; font-weight: bold; margin-bottom: 8px;")
        layout.addWidget(title)

        subtitle = QLabel("Select a profile or create a new one")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: gray; margin-bottom: 24px;")
        layout.addWidget(subtitle)

        self.empty_label = QLabel("No profiles yet — click New Profile to get started.")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_label.setStyleSheet("color: #888; font-style: italic;")
        self.empty_label.hide()
        layout.addWidget(self.empty_label)

        self.user_list = QListWidget()
        self.user_list.setMaximumWidth(400)
        self.user_list.setMinimumHeight(200)
        self.user_list.itemDoubleClicked.connect(self._on_double_click)
        self.user_list.currentItemChanged.connect(self._update_buttons)
        layout.addWidget(self.user_list, alignment=Qt.AlignmentFlag.AlignHCenter)

        btn_row = QHBoxLayout()
        self.sign_in_btn = QPushButton("Sign In")
        self.sign_in_btn.setDefault(True)
        self.sign_in_btn.clicked.connect(self._on_sign_in)

        self.new_profile_btn = QPushButton("New Profile")
        self.new_profile_btn.clicked.connect(self.create_profile.emit)

        self.delete_btn = QPushButton("Delete Profile")
        self.delete_btn.clicked.connect(self._on_delete)

        btn_row.addWidget(self.sign_in_btn)
        btn_row.addWidget(self.new_profile_btn)
        btn_row.addWidget(self.delete_btn)
        layout.addLayout(btn_row)

    def refresh(self):
        self.user_list.clear()
        users = user_model.list_users()
        for user in users:
            item = QListWidgetItem(f"{user.name}  (@{user.username})")
            item.setData(Qt.ItemDataRole.UserRole, user.user_id)
            self.user_list.addItem(item)

        has_users = len(users) > 0
        self.user_list.setVisible(has_users)
        self.empty_label.setVisible(not has_users)
        self._update_buttons()

    def _update_buttons(self):
        has_selection = self.user_list.currentItem() is not None
        self.sign_in_btn.setEnabled(has_selection)
        self.delete_btn.setEnabled(has_selection)

    def _on_sign_in(self):
        item = self.user_list.currentItem()
        if item:
            self.user_selected.emit(item.data(Qt.ItemDataRole.UserRole))

    def _on_double_click(self, item):
        self.user_selected.emit(item.data(Qt.ItemDataRole.UserRole))

    def _on_delete(self):
        item = self.user_list.currentItem()
        if not item:
            return
        name = item.text()
        user_id = item.data(Qt.ItemDataRole.UserRole)
        reply = QMessageBox.question(
            self,
            "Delete Profile",
            f"Permanently delete {name}? This cannot be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel,
        )
        if reply == QMessageBox.StandardButton.Yes:
            user_model.delete_user(user_id)
            self.refresh()
