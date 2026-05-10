from typing import Callable, Any
from PyQt6.QtCore import QThread, pyqtSignal

from app.common.logging_config import get_logger

log = get_logger(__name__)

# Keeps references alive so Python's GC doesn't destroy a thread while it runs.
_active: set = set()


class ApiWorker(QThread):
    """Runs any callable in a background thread and emits result or error."""

    result = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, fn: Callable, *args: Any, **kwargs: Any):
        super().__init__()
        self._fn = fn
        self._args = args
        self._kwargs = kwargs
        self.setObjectName(fn.__name__)
        _active.add(self)
        log.debug("created  [%s]  active=%d", fn.__name__, len(_active))
        self.finished.connect(self._on_finished)

    def _on_finished(self):
        _active.discard(self)
        log.debug("finished [%s]  active=%d", self.objectName(), len(_active))

    def run(self):
        log.debug("running  [%s]", self.objectName())
        try:
            result = self._fn(*self._args, **self._kwargs)
            log.debug("success  [%s]", self.objectName())
            self.result.emit(result)
        except Exception as exc:
            log.error("error    [%s]: %s", self.objectName(), exc, exc_info=True)
            self.error.emit(str(exc))
