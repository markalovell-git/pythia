class AppState:
    """Single in-memory state object shared across the app via reference."""

    def __init__(self):
        self.current_user_id: str | None = None
        self.current_username: str | None = None
        self.current_user_name: str | None = None


state = AppState()
