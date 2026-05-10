import pytest
from unittest.mock import patch
from PyQt6.QtCore import Qt

from app.frontend.widgets.welcome import WelcomeWidget
from app.frontend.models.user_model import UserSummary


_USERS = [
    UserSummary(user_id="u1", username="jdoe", name="John Doe"),
    UserSummary(user_id="u2", username="jsmith", name="Jane Smith"),
]


@pytest.fixture
def welcome(qtbot, monkeypatch):
    monkeypatch.setattr("app.frontend.models.user_model.list_users", lambda: _USERS)
    monkeypatch.setattr("app.frontend.models.user_model.delete_user", lambda uid: None)
    w = WelcomeWidget()
    qtbot.addWidget(w)
    return w


def test_shows_all_users(welcome):
    assert welcome.user_list.count() == 2


def test_sign_in_emits_user_id(welcome, qtbot):
    welcome.user_list.setCurrentRow(0)
    with qtbot.waitSignal(welcome.user_selected, timeout=1000) as blocker:
        welcome.sign_in_btn.click()
    assert blocker.args[0] == "u1"


def test_double_click_signs_in(welcome, qtbot):
    item = welcome.user_list.item(1)
    with qtbot.waitSignal(welcome.user_selected, timeout=1000) as blocker:
        welcome.user_list.itemDoubleClicked.emit(item)
    assert blocker.args[0] == "u2"


def test_new_profile_emits_signal(welcome, qtbot):
    with qtbot.waitSignal(welcome.create_profile, timeout=1000):
        welcome.new_profile_btn.click()
