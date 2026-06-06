from PyQt6.QtCore import QThread, pyqtSignal

from app.frontend.services import llm_client

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
        try:
            for text in llm_client.stream_chat(
                provider=provider,
                api_key=key or "",
                model=self._ai_settings.get("ollama_model", "qwen3:14b"),
                base_url=self._ai_settings.get("ollama_url", "http://localhost:11434"),
                system=self._system,
                messages=self._messages,
                think=self._think,
            ):
                self.chunk.emit(text)
        except Exception as e:
            self.error.emit(str(e))
