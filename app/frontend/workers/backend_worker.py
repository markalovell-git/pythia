import uvicorn
from PyQt6.QtCore import QThread, pyqtSignal

from app.common.config import BACKEND_HOST, BACKEND_PORT
from app.common.logging_config import get_logger

log = get_logger(__name__)


class BackendWorker(QThread):
    """Runs the FastAPI/uvicorn server in a background thread."""

    started_ok = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setObjectName("BackendWorker")

    def run(self):
        log.debug("BackendWorker starting uvicorn")
        config = uvicorn.Config(
            "app.backend.main:app",
            host=BACKEND_HOST,
            port=BACKEND_PORT,
            log_level="error",
        )
        self.server = uvicorn.Server(config)
        self.server.run()
        log.debug("BackendWorker uvicorn exited")

    def stop(self):
        log.debug("BackendWorker stopping")
        if hasattr(self, "server"):
            self.server.should_exit = True
        self.wait()
