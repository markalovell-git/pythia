from PyQt6.QtCore import Qt, QEvent, QTimer
from PyQt6.QtGui import QColor, QTextCursor
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSplitter, QScrollArea, QLineEdit, QFrame, QSizePolicy, QTextEdit,
    QGroupBox,
)

from app.frontend import api_client
from app.frontend.models import chart_model, user_model
from app.frontend.models.chart_model import ChartData, TransitData, TransitWindowResult
from app.frontend.models.user_model import UserDetail
from app.frontend.workers.api_worker import ApiWorker
from app.frontend.workers.stream_worker import StreamWorker
from app.frontend.services import llm_client

_ASPECT_ABBR = {
    "conjunction": "☌",
    "sextile":     "⚹",
    "square":      "□",
    "trine":       "△",
    "opposition":  "☍",
}

_CATEGORY_COLORS = {
    "major":    "#e8c060",
    "notable":  "#80c0e0",
    "minor":    "#8080aa",
}



class _ScrollLabel(QScrollArea):
    """A scroll area wrapping a word-wrapped, selectable QLabel."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self._label = QLabel()
        self._label.setWordWrap(True)
        self._label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self._label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self._label.setStyleSheet("color: #c0c0d8; font-size: 15px; padding: 4px;")
        self._label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setWidget(self._label)
        self._think_step = 0
        self._think_timer = QTimer(self)
        self._think_timer.setInterval(450)
        self._think_timer.timeout.connect(self._tick_thinking)

    def _tick_thinking(self):
        self._think_step = (self._think_step + 1) % 4
        dots = "." * self._think_step
        self._label.setText(f"<i style='color:#6060a0;'>Thinking{dots}</i>")

    def start_thinking(self):
        self._think_step = 0
        self._label.setText("<i style='color:#6060a0;'>Thinking</i>")
        self._think_timer.start()

    def set_text(self, text: str):
        self._think_timer.stop()
        self._label.setText(text)

    def set_placeholder(self, text: str):
        self._think_timer.stop()
        self._label.setText(f"<i style='color:#6060a0;'>{text}</i>")


class ConsultView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._natal: ChartData | None = None
        self._transits: TransitData | None = None
        self._windows: list[TransitWindowResult] | None = None
        self._user: UserDetail | None = None
        self._ai_settings: dict = {}
        self._chat_history: list[dict] = []
        self._today_text: str = ""
        self._longer_text: str = ""
        self._today_accumulated: str = ""
        self._longer_accumulated: str = ""
        self._natal_worker:        ApiWorker | None = None
        self._transit_worker:      ApiWorker | None = None
        self._windows_worker:      ApiWorker | None = None
        self._user_worker:         ApiWorker | None = None
        self._today_cache_worker:  ApiWorker | None = None
        self._longer_cache_worker: ApiWorker | None = None
        self._today_worker:        ApiWorker | None = None
        self._longer_worker:       ApiWorker | None = None
        self._chat_worker:         ApiWorker | None = None
        self._bg_workers:          list[ApiWorker] = []  # fire-and-forget refs
        self._generated = False
        self._longer_done = False
        self._today_done = False
        self._build_ui()

    # ── UI construction ───────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(8)

        # Header row
        header = QHBoxLayout()
        title = QLabel("Consult")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        header.addWidget(title)
        header.addStretch()
        self._provider_label = QLabel("Provider: —")
        self._provider_label.setStyleSheet("color: #6060a0; font-size: 12px;")
        header.addWidget(self._provider_label)
        self._regen_btn = QPushButton("Regenerate")
        self._regen_btn.setEnabled(False)
        self._regen_btn.clicked.connect(self._on_regenerate)
        header.addWidget(self._regen_btn)
        root.addLayout(header)

        # Transit summary bar
        self._transit_bar = QLabel("Loading transits…")
        self._transit_bar.setStyleSheet(
            "color: #8080aa; font-size: 13px; padding: 4px 0;"
        )
        self._transit_bar.setWordWrap(True)
        root.addWidget(self._transit_bar)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet("color: #2a2a4e;")
        root.addWidget(sep)

        # Main splitter: interpretations top, chat bottom
        main_splitter = QSplitter(Qt.Orientation.Vertical)
        main_splitter.setChildrenCollapsible(False)

        # Top: side-by-side Today / Longer Term
        top_splitter = QSplitter(Qt.Orientation.Horizontal)
        top_splitter.setChildrenCollapsible(False)

        today_group = QGroupBox("Today")
        today_layout = QVBoxLayout(today_group)
        today_layout.setContentsMargins(4, 4, 4, 4)
        self._today_scroll = _ScrollLabel()
        self._today_scroll.set_placeholder("Generating…")
        today_layout.addWidget(self._today_scroll)
        top_splitter.addWidget(today_group)

        longer_group = QGroupBox("Longer Term")
        longer_layout = QVBoxLayout(longer_group)
        longer_layout.setContentsMargins(4, 4, 4, 4)
        self._longer_scroll = _ScrollLabel()
        self._longer_scroll.set_placeholder("Generating…")
        longer_layout.addWidget(self._longer_scroll)
        top_splitter.addWidget(longer_group)

        top_splitter.setSizes([500, 500])
        main_splitter.addWidget(top_splitter)

        # Bottom: chat
        chat_frame = QFrame()
        chat_layout = QVBoxLayout(chat_frame)
        chat_layout.setContentsMargins(0, 4, 0, 0)
        chat_layout.setSpacing(4)

        chat_label = QLabel("Chat")
        chat_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #c0c0e0;")
        chat_layout.addWidget(chat_label)

        self._chat_scroll = QScrollArea()
        self._chat_scroll.setWidgetResizable(True)
        self._chat_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self._chat_inner = QWidget()
        self._chat_inner_layout = QVBoxLayout(self._chat_inner)
        self._chat_inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._chat_inner_layout.setSpacing(8)
        self._chat_inner_layout.addStretch()
        self._chat_scroll.setWidget(self._chat_inner)
        chat_layout.addWidget(self._chat_scroll)

        input_row = QHBoxLayout()
        self._chat_input = QLineEdit()
        self._chat_input.setPlaceholderText("Ask about your chart…")
        self._chat_input.returnPressed.connect(self._on_send)
        input_row.addWidget(self._chat_input)
        self._send_btn = QPushButton("Send")
        self._send_btn.clicked.connect(self._on_send)
        input_row.addWidget(self._send_btn)
        chat_layout.addLayout(input_row)

        main_splitter.addWidget(chat_frame)
        main_splitter.setSizes([400, 300])
        root.addWidget(main_splitter)

    # ── Data loading ──────────────────────────────────────────────────────────

    def load(self, user_id: str):
        self._user_id = user_id
        self._ai_settings = chart_model.get_ai_settings(user_id)
        self._update_provider_label()

        self._natal_worker = ApiWorker(chart_model.load_chart, user_id)
        self._natal_worker.result.connect(self._on_natal)
        self._natal_worker.error.connect(lambda _: None)
        self._natal_worker.start()

        self._transit_worker = ApiWorker(chart_model.load_transits, user_id)
        self._transit_worker.result.connect(self._on_transits)
        self._transit_worker.error.connect(lambda _: None)
        self._transit_worker.start()

        self._windows_worker = ApiWorker(chart_model.load_transit_windows, user_id)
        self._windows_worker.result.connect(self._on_windows)
        self._windows_worker.error.connect(lambda _: None)
        self._windows_worker.start()

        self._user_worker = ApiWorker(user_model.get_user, user_id)
        self._user_worker.result.connect(self._on_user)
        self._user_worker.error.connect(lambda _: None)
        self._user_worker.start()

    def _on_natal(self, natal: ChartData):
        self._natal = natal
        self._try_generate()

    def _on_transits(self, transits: TransitData):
        self._transits = transits
        self._populate_transit_bar()
        self._try_generate()

    def _on_windows(self, windows: list):
        self._windows = windows
        self._try_generate()

    def _on_user(self, user: UserDetail):
        self._user = user
        self._try_generate()

    def _try_generate(self):
        if (self._natal is not None and self._transits is not None
                and self._windows is not None and self._user is not None
                and not self._generated):
            self._generated = True
            self._populate_transit_bar()
            self._check_cache_then_generate(skip_cache=False)

    # ── Transit bar ───────────────────────────────────────────────────────────

    def _populate_transit_bar(self):
        if not self._transits:
            return
        parts = []
        for t in self._transits.transits:
            if t.category not in ("major", "notable"):
                continue
            abbr = _ASPECT_ABBR.get(t.aspect, t.aspect[:3])
            color = _CATEGORY_COLORS.get(t.category, "#8080aa")
            parts.append(
                f"<span style='color:{color};'>{t.transit_planet} {abbr} {t.natal_planet}</span>"
            )
        if parts:
            self._transit_bar.setText("  ·  ".join(parts))
        else:
            self._transit_bar.setText("No major or notable transits active.")

    # ── Cache-aware generation ────────────────────────────────────────────────

    def _check_cache_then_generate(self, skip_cache: bool):
        self._today_done = False
        self._longer_done = False
        # Regen available as soon as data is loaded — don't hold it hostage to LLM completion
        self._regen_btn.setEnabled(True)

        if skip_cache:
            self._today_scroll.set_placeholder("Generating…")
            self._longer_scroll.set_placeholder("Generating…")
            self._start_today_llm()
            self._start_longer_llm()
            return

        self._today_scroll.set_placeholder("Loading…")
        self._longer_scroll.set_placeholder("Loading…")

        # Store workers as instance vars to prevent garbage collection before signals fire
        self._today_cache_worker = ApiWorker(api_client.get_consult_cache, self._user_id, "today")
        self._today_cache_worker.result.connect(self._on_today_cache)
        self._today_cache_worker.error.connect(lambda _: self._start_today_llm())
        self._today_cache_worker.start()

        self._longer_cache_worker = ApiWorker(api_client.get_consult_cache, self._user_id, "longer_term")
        self._longer_cache_worker.result.connect(self._on_longer_cache)
        self._longer_cache_worker.error.connect(lambda _: self._start_longer_llm())
        self._longer_cache_worker.start()

    def _on_today_cache(self, result):
        if result:
            self._on_today_result(result["content"])
        else:
            self._start_today_llm()

    def _on_longer_cache(self, result):
        if result:
            self._on_longer_result(result["content"])
        else:
            self._start_longer_llm()

    def _start_today_llm(self):
        self._today_scroll.start_thinking()
        self._today_accumulated = ""
        payload = llm_client.build_consult_payload(
            self._user, self._natal, self._transits, self._windows or [], "today"
        )
        w = StreamWorker(
            self._ai_settings, llm_client.DAILY_SYSTEM_PROMPT,
            [{"role": "user", "content": payload}],
        )
        w.chunk.connect(self._on_today_chunk)
        w.error.connect(self._on_today_error)
        w.finished.connect(self._on_today_stream_done)
        w.start()
        self._today_worker = w

    def _start_longer_llm(self):
        self._longer_scroll.start_thinking()
        self._longer_accumulated = ""
        payload = llm_client.build_consult_payload(
            self._user, self._natal, self._transits, self._windows or [], "longer_term"
        )
        w = StreamWorker(
            self._ai_settings, llm_client.LONGVIEW_SYSTEM_PROMPT,
            [{"role": "user", "content": payload}],
        )
        w.chunk.connect(self._on_longer_chunk)
        w.error.connect(self._on_longer_error)
        w.finished.connect(self._on_longer_stream_done)
        w.start()
        self._longer_worker = w

    def _on_today_chunk(self, text: str):
        self._today_accumulated += text
        self._today_scroll.set_text(self._today_accumulated)

    def _on_longer_chunk(self, text: str):
        self._longer_accumulated += text
        self._longer_scroll.set_text(self._longer_accumulated)

    def _on_today_stream_done(self):
        if self._today_accumulated:  # only save if we got content (not an error)
            self._fire_and_forget(
                api_client.set_consult_cache, self._user_id, "today", self._today_accumulated
            )
            self._on_today_result(self._today_accumulated)

    def _on_longer_stream_done(self):
        if self._longer_accumulated:
            self._fire_and_forget(
                api_client.set_consult_cache, self._user_id, "longer_term", self._longer_accumulated
            )
            self._on_longer_result(self._longer_accumulated)

    def _fire_and_forget(self, fn, *args):
        w = ApiWorker(fn, *args)
        self._bg_workers.append(w)
        w.finished.connect(lambda: self._bg_workers.remove(w) if w in self._bg_workers else None)
        w.start()

    def _on_today_result(self, text: str):
        self._today_text = text
        self._today_scroll.set_text(text)
        self._today_done = True

    def _on_today_error(self, msg: str):
        self._today_scroll.set_placeholder(f"Error: {msg}")
        self._today_done = True

    def _on_longer_result(self, text: str):
        self._longer_text = text
        self._longer_scroll.set_text(text)
        self._longer_done = True

    def _on_longer_error(self, msg: str):
        self._longer_scroll.set_placeholder(f"Error: {msg}")
        self._longer_done = True

    def _on_regenerate(self):
        if not (self._natal and self._transits and self._windows is not None and self._user):
            return
        self._ai_settings = chart_model.get_ai_settings(self._user_id)
        self._update_provider_label()
        self._today_text = ""
        self._longer_text = ""
        self._check_cache_then_generate(skip_cache=True)

    # ── Chat ──────────────────────────────────────────────────────────────────

    def _on_send(self):
        text = self._chat_input.text().strip()
        if not text or self._chat_worker is not None:
            return
        self._chat_input.clear()
        self._send_btn.setEnabled(False)
        self._append_chat_bubble(text, role="user")
        self._chat_history.append({"role": "user", "content": text})

        # Build system context including the two readings
        context_parts = []
        if self._today_text:
            context_parts.append(f"DAILY READING:\n{self._today_text}")
        if self._longer_text:
            context_parts.append(f"LONGER-TERM READING:\n{self._longer_text}")
        system = llm_client.CHAT_SYSTEM_PROMPT
        if context_parts:
            system += "\n\nCONTEXT — READINGS ALREADY GIVEN TO THE USER:\n\n" + "\n\n".join(context_parts)

        ai = chart_model.get_ai_settings(self._user_id)
        self._chat_worker = ApiWorker(
            _call_llm, ai, system, list(self._chat_history)
        )
        self._chat_worker.result.connect(self._on_chat_result)
        self._chat_worker.error.connect(self._on_chat_error)
        self._chat_worker.start()

    def _on_chat_result(self, text: str):
        self._chat_history.append({"role": "assistant", "content": text})
        self._append_chat_bubble(text, role="assistant")
        self._chat_worker = None
        self._send_btn.setEnabled(True)

    def _on_chat_error(self, msg: str):
        self._append_chat_bubble(f"Error: {msg}", role="error")
        self._chat_history.pop()  # remove the failed user message
        self._chat_worker = None
        self._send_btn.setEnabled(True)

    def _append_chat_bubble(self, text: str, role: str):
        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        if role == "user":
            bubble.setStyleSheet(
                "background: #1e2a4a; color: #c0c8e0; border-radius: 6px;"
                "padding: 8px; margin: 2px 40px 2px 2px; font-size: 14px;"
            )
            bubble.setAlignment(Qt.AlignmentFlag.AlignLeft)
        elif role == "assistant":
            bubble.setStyleSheet(
                "background: #1a2a1a; color: #a8c8a0; border-radius: 6px;"
                "padding: 8px; margin: 2px 2px 2px 40px; font-size: 14px;"
            )
            bubble.setAlignment(Qt.AlignmentFlag.AlignLeft)
        else:  # error
            bubble.setStyleSheet(
                "color: #e06060; font-size: 13px; padding: 4px; margin: 2px;"
            )

        # Insert before the trailing stretch
        count = self._chat_inner_layout.count()
        self._chat_inner_layout.insertWidget(count - 1, bubble)

        # Scroll to bottom
        self._chat_scroll.verticalScrollBar().setValue(
            self._chat_scroll.verticalScrollBar().maximum()
        )

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _update_provider_label(self):
        provider = self._ai_settings.get("ai_provider", "ollama")
        labels = {"ollama": "Ollama", "claude": "Claude", "openai": "ChatGPT"}
        self._provider_label.setText(f"Provider: {labels.get(provider, provider)}")
