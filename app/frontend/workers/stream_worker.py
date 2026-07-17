from PyQt6.QtCore import QThread, pyqtSignal

from app.frontend.services import llm_client
from app.common.constants import (
    DEFAULT_ANTHROPIC_MODEL, DEFAULT_OPENAI_MODEL,
    DEFAULT_OLLAMA_MODEL, DEFAULT_OLLAMA_URL,
)

# Keeps references alive so Python's GC doesn't destroy a thread while it runs.
_active: set = set()


class StreamWorker(QThread):
    """Streams an LLM response, emitting one chunk signal per piece of text."""

    chunk = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, ai_settings: dict, system: str, messages: list[dict], think: bool = True):
        super().__init__()
        self._ai_settings = ai_settings
        self._system = system
        self._messages = messages
        self._think = think
        _active.add(self)
        self.finished.connect(lambda: _active.discard(self))

    def run(self):
        provider = self._ai_settings.get("ai_provider", "ollama")
        key = (
            self._ai_settings.get("anthropic_key") if provider == "claude"
            else self._ai_settings.get("openai_key") if provider == "openai"
            else ""
        )
        if provider == "claude":
            model = self._ai_settings.get("anthropic_model") or DEFAULT_ANTHROPIC_MODEL
        elif provider == "openai":
            model = self._ai_settings.get("openai_model") or DEFAULT_OPENAI_MODEL
        else:
            model = self._ai_settings.get("ollama_model") or DEFAULT_OLLAMA_MODEL
        try:
            for text in llm_client.stream_chat(
                provider=provider,
                api_key=key or "",
                model=model,
                base_url=self._ai_settings.get("ollama_url") or DEFAULT_OLLAMA_URL,
                system=self._system,
                messages=self._messages,
                think=self._think,
            ):
                self.chunk.emit(text)
        except Exception as e:
            self.error.emit(str(e))
