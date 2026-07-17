from datetime import datetime
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QTextCursor, QTextBlockFormat
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSplitter, QScrollArea, QLineEdit, QFrame, QTextBrowser,
    QGroupBox, QMessageBox,
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

_BROWSER_SS = "background-color: #0d0d1a; border: none; font-size: 15px; padding: 2px;"


class _ScrollLabel(QTextBrowser):
    """Markdown-rendering scrollable text area with thinking animation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setOpenLinks(False)
        self.setReadOnly(True)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setStyleSheet(_BROWSER_SS)
        self._think_step = 0
        self._think_timer = QTimer(self)
        self._think_timer.setInterval(450)
        self._think_timer.timeout.connect(self._tick_thinking)

    def _apply_spacing(self):
        """Fix up block margins after setMarkdown() — Qt's inline styles override CSS."""
        doc = self.document()
        cursor = QTextCursor(doc)
        block = doc.begin()
        while block.isValid():
            fmt = block.blockFormat()
            new_fmt = QTextBlockFormat(fmt)
            is_list_item = block.textList() is not None
            if fmt.headingLevel() > 0:
                new_fmt.setTopMargin(20.0 if fmt.headingLevel() <= 2 else 14.0)
                new_fmt.setBottomMargin(4.0)
            elif not is_list_item and block.text().strip():
                # Detect all-bold paragraph (LLM uses **text** as section titles)
                it = block.begin()
                weights = []
                while not it.atEnd():
                    weights.append(it.fragment().charFormat().fontWeight())
                    it += 1
                if weights and all(w >= 600 for w in weights):
                    new_fmt.setTopMargin(14.0)
                    new_fmt.setBottomMargin(4.0)
                else:
                    new_fmt.setBottomMargin(10.0)
            cursor.setPosition(block.position())
            cursor.setBlockFormat(new_fmt)
            block = block.next()

    def _tick_thinking(self):
        self._think_step = (self._think_step + 1) % 4
        dots = "." * self._think_step
        self.setHtml(f"<span style='color:#6060a0; font-style:italic;'>Thinking{dots}</span>")

    def start_thinking(self):
        self._think_step = 0
        self.setHtml("<span style='color:#6060a0; font-style:italic;'>Thinking</span>")
        self._think_timer.start()

    def set_text(self, text: str):
        self._think_timer.stop()
        self.setMarkdown(text)
        self._apply_spacing()

    def set_placeholder(self, text: str):
        self._think_timer.stop()
        self.setHtml(f"<span style='color:#6060a0; font-style:italic;'>{text}</span>")


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
        self._ai_settings_worker:  ApiWorker | None = None
        self._transit_worker:      ApiWorker | None = None
        self._windows_worker:      ApiWorker | None = None
        self._user_worker:         ApiWorker | None = None
        self._today_cache_worker:  ApiWorker | None = None
        self._longer_cache_worker: ApiWorker | None = None
        self._today_worker:        ApiWorker | None = None
        self._longer_worker:       ApiWorker | None = None
        self._history_worker:      ApiWorker | None = None
        self._chat_worker:         StreamWorker | None = None
        self._chat_accumulated:    str = ""
        self._pending_user_msg:    str = ""
        self._streaming_bubble:    QLabel | None = None
        self._chat_pending_scroll: bool = False
        self._chat_think_step:     int = 0
        self._chat_think_timer = QTimer(self)
        self._chat_think_timer.setInterval(450)
        self._chat_think_timer.timeout.connect(self._tick_chat_thinking)
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
        self._longer_generated_label = QLabel()
        self._longer_generated_label.setStyleSheet("color: #6060a0; font-size: 11px; padding: 0 2px;")
        self._longer_generated_label.setVisible(False)
        longer_layout.addWidget(self._longer_generated_label)
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

        chat_header = QHBoxLayout()
        chat_label = QLabel("Chat")
        chat_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #c0c0e0;")
        chat_header.addWidget(chat_label)
        chat_header.addStretch()
        self._clear_chat_btn = QPushButton("Clear chat")
        self._clear_chat_btn.setStyleSheet("font-size: 12px;")
        self._clear_chat_btn.clicked.connect(self._on_clear_chat)
        chat_header.addWidget(self._clear_chat_btn)
        chat_layout.addLayout(chat_header)

        self._chat_scroll = QScrollArea()
        self._chat_scroll.setWidgetResizable(True)
        self._chat_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self._chat_inner = QWidget()
        self._chat_inner_layout = QVBoxLayout(self._chat_inner)
        self._chat_inner_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._chat_inner_layout.setSpacing(8)
        self._chat_inner_layout.addStretch()
        self._chat_scroll.setWidget(self._chat_inner)
        # rangeChanged fires once the scroll area has recomputed its extent for
        # newly added / re-wrapped content — the right moment to pin to bottom.
        self._chat_scroll.verticalScrollBar().rangeChanged.connect(self._on_chat_range_changed)
        chat_layout.addWidget(self._chat_scroll)

        input_row = QHBoxLayout()
        self._chat_input = QLineEdit()
        self._chat_input.setPlaceholderText("Ask about your chart…")
        self._chat_input.returnPressed.connect(self._on_send)
        # Make the input box 1.5x its natural height
        input_h = int(self._chat_input.sizeHint().height() * 1.5)
        self._chat_input.setFixedHeight(input_h)
        input_row.addWidget(self._chat_input)
        self._send_btn = QPushButton("Send")
        self._send_btn.clicked.connect(self._on_send)
        self._send_btn.setFixedHeight(input_h)  # match the taller input
        input_row.addWidget(self._send_btn)
        chat_layout.addLayout(input_row)

        main_splitter.addWidget(chat_frame)
        main_splitter.setSizes([400, 300])
        root.addWidget(main_splitter)

    # ── Data loading ──────────────────────────────────────────────────────────

    def load(self, user_id: str):
        self._user_id = user_id

        self._ai_settings_worker = ApiWorker(chart_model.get_ai_settings, user_id)
        self._ai_settings_worker.result.connect(self._on_ai_settings)
        self._ai_settings_worker.error.connect(lambda _: None)
        self._ai_settings_worker.start()

        self._history_worker = ApiWorker(api_client.get_chat_history, user_id)
        self._history_worker.result.connect(self._on_chat_history_loaded)
        self._history_worker.error.connect(lambda _: None)
        self._history_worker.start()

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

    def _on_ai_settings(self, settings: dict):
        self._ai_settings = settings
        self._update_provider_label()
        self._try_generate()

    def _try_generate(self):
        # _ai_settings must be in before generating, or StreamWorker would
        # silently fall back to the Ollama defaults for Claude/OpenAI users.
        if (self._natal is not None and self._transits is not None
                and self._windows is not None and self._user is not None
                and self._ai_settings and not self._generated):
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
            self._set_longer_generated_date(result.get("cached_at"))
            self._on_longer_result(result["content"])
        else:
            self._start_longer_llm()

    def _set_longer_generated_date(self, cached_at_iso: str | None = None):
        if cached_at_iso:
            try:
                dt = datetime.fromisoformat(cached_at_iso)
                label = dt.strftime("Generated %-d %b %Y")
            except Exception:
                label = f"Generated {cached_at_iso[:10]}"
        else:
            label = datetime.now().strftime("Generated %-d %b %Y")
        self._longer_generated_label.setText(label)
        self._longer_generated_label.setVisible(True)

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
            self._set_longer_generated_date(None)
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
        # Clear the accumulator so the trailing `finished` signal doesn't cache
        # and display a partial reading over this error.
        self._today_accumulated = ""
        self._today_scroll.set_placeholder(f"Error: {msg}")
        self._today_done = True

    def _on_longer_result(self, text: str):
        self._longer_text = text
        self._longer_scroll.set_text(text)
        self._longer_done = True

    def _on_longer_error(self, msg: str):
        self._longer_accumulated = ""
        self._longer_scroll.set_placeholder(f"Error: {msg}")
        self._longer_done = True

    def _on_regenerate(self):
        if not (self._natal and self._transits and self._windows is not None and self._user):
            return
        # Re-fetch settings off the GUI thread first — the user may have just
        # switched provider/model in Settings.
        self._regen_btn.setEnabled(False)
        self._ai_settings_worker = ApiWorker(chart_model.get_ai_settings, self._user_id)
        self._ai_settings_worker.result.connect(self._on_regen_settings)
        self._ai_settings_worker.error.connect(lambda _: self._regen_btn.setEnabled(True))
        self._ai_settings_worker.start()

    def _on_regen_settings(self, settings: dict):
        self._ai_settings = settings
        self._update_provider_label()
        self._today_text = ""
        self._longer_text = ""
        self._check_cache_then_generate(skip_cache=True)

    # ── Chat ──────────────────────────────────────────────────────────────────

    def _on_chat_history_loaded(self, history: list):
        """Render persisted messages and seed the in-memory history on page load."""
        if not history:
            return
        self._chat_history = [{"role": m["role"], "content": m["content"]} for m in history]
        for m in self._chat_history:
            self._append_chat_bubble(m["content"], role=m["role"])

    def _build_chat_system(self) -> str:
        """Chat system prompt + authoritative chart data + the two prose readings."""
        system = llm_client.CHAT_SYSTEM_PROMPT

        if self._natal is not None and self._transits is not None and self._user is not None:
            payload = llm_client.build_consult_payload(
                self._user, self._natal, self._transits, self._windows or [], "longer_term"
            )
            system += "\n\nCHART DATA (authoritative — ground answers in this):\n\n" + payload

        context_parts = []
        if self._today_text:
            context_parts.append(f"DAILY READING:\n{self._today_text}")
        if self._longer_text:
            context_parts.append(f"LONGER-TERM READING:\n{self._longer_text}")
        if context_parts:
            system += "\n\nCONTEXT — READINGS ALREADY GIVEN TO THE USER:\n\n" + "\n\n".join(context_parts)
        return system

    def _on_send(self):
        text = self._chat_input.text().strip()
        if not text or self._chat_worker is not None or not self._ai_settings:
            return
        self._chat_input.clear()
        self._send_btn.setEnabled(False)
        self._clear_chat_btn.setEnabled(False)  # don't delete a thread mid-reply
        self._append_chat_bubble(text, role="user")
        self._chat_history.append({"role": "user", "content": text})
        self._pending_user_msg = text  # persisted only if the reply succeeds

        # Empty assistant bubble that shows a "Thinking…" animation until the
        # first chunk arrives, then fills in as chunks stream in.
        self._chat_accumulated = ""
        self._streaming_bubble = self._append_chat_bubble("Thinking", role="assistant")
        self._chat_think_step = 0
        self._chat_think_timer.start()

        # Few-shot example primes the model toward short replies; it's sent to the
        # model but kept out of the persisted/displayed history.
        w = StreamWorker(
            self._ai_settings,
            self._build_chat_system(),
            llm_client.CHAT_FEWSHOT + list(self._chat_history),
            think=False,  # chat wants short, direct replies — skip qwen3's reasoning pass
        )
        w.chunk.connect(self._on_chat_chunk)
        w.error.connect(self._on_chat_error)
        w.finished.connect(self._on_chat_stream_done)
        w.start()
        self._chat_worker = w

    def _tick_chat_thinking(self):
        if self._streaming_bubble is None:
            self._chat_think_timer.stop()
            return
        self._chat_think_step = (self._chat_think_step + 1) % 4
        self._streaming_bubble.setText("Thinking" + "." * self._chat_think_step)

    def _on_chat_chunk(self, text: str):
        self._chat_think_timer.stop()  # first content arrived — drop the placeholder
        self._chat_accumulated += text
        if self._streaming_bubble is not None:
            self._streaming_bubble.setText(self._chat_accumulated)
        self._scroll_chat_to_bottom()

    def _scroll_chat_to_bottom(self):
        # Best-effort now, plus arm a deferred scroll: a word-wrapped bubble only
        # gets its true height once resized to the viewport, which fires
        # rangeChanged after this returns — _on_chat_range_changed catches that.
        self._chat_pending_scroll = True
        sb = self._chat_scroll.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _on_chat_range_changed(self, _minimum: int, maximum: int):
        if self._chat_pending_scroll:
            self._chat_pending_scroll = False
            self._chat_scroll.verticalScrollBar().setValue(maximum)

    def _on_chat_stream_done(self):
        self._chat_think_timer.stop()
        bubble, self._streaming_bubble = self._streaming_bubble, None
        self._chat_worker = None
        self._send_btn.setEnabled(True)
        self._clear_chat_btn.setEnabled(True)
        reply = llm_client.trim_to_last_sentence(self._chat_accumulated)
        if reply:
            if bubble is not None:
                bubble.setText(reply)  # replace any mid-sentence cutoff with the clean version
            self._chat_history.append({"role": "assistant", "content": reply})
            self._fire_and_forget(api_client.append_chat_message, self._user_id, "user", self._pending_user_msg)
            self._fire_and_forget(
                api_client.append_chat_message, self._user_id, "assistant", reply
            )
        elif bubble is not None:
            # Stream ended with no content and no error handled below — drop the
            # empty bubble and the unanswered user turn.
            bubble.deleteLater()
            if self._chat_history and self._chat_history[-1]["role"] == "user":
                self._chat_history.pop()

    def _on_chat_error(self, msg: str):
        # Drop the empty assistant bubble and the failed user turn. Clear the
        # accumulator so the trailing `finished` signal is a no-op.
        self._chat_think_timer.stop()
        if self._streaming_bubble is not None:
            self._streaming_bubble.deleteLater()
            self._streaming_bubble = None
        self._chat_accumulated = ""
        self._append_chat_bubble(f"Error: {msg}", role="error")
        if self._chat_history and self._chat_history[-1]["role"] == "user":
            self._chat_history.pop()
        self._chat_worker = None
        self._send_btn.setEnabled(True)
        self._clear_chat_btn.setEnabled(True)

    def _on_clear_chat(self):
        if self._chat_worker is not None:
            return  # a reply is streaming; button is disabled anyway
        if not self._chat_history:
            return  # nothing to clear
        confirm = QMessageBox.question(
            self,
            "Clear chat",
            "Delete the entire chat history for this person? This can't be undone.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return
        self._chat_history = []
        self._clear_chat_bubbles()
        self._fire_and_forget(api_client.clear_chat_history, self._user_id)

    def _clear_chat_bubbles(self):
        """Remove every message bubble, leaving the trailing stretch in place."""
        for i in reversed(range(self._chat_inner_layout.count())):
            w = self._chat_inner_layout.itemAt(i).widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()

    def _append_chat_bubble(self, text: str, role: str) -> QLabel:
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

        self._scroll_chat_to_bottom()
        return bubble

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _update_provider_label(self):
        provider = self._ai_settings.get("ai_provider", "ollama")
        labels = {"ollama": "Ollama", "claude": "Claude", "openai": "ChatGPT"}
        self._provider_label.setText(f"Provider: {labels.get(provider, provider)}")
