"""The Chart page: wheel + info column + planet table/info panel.

The wheel itself (painting, hit-testing) lives in chart_wheel.py; the info
panel's HTML builders live in chart_info.py. This module wires them to the
API workers and each other.
"""
from datetime import datetime
from PyQt6.QtCore import Qt, QUrl, QEvent, pyqtSignal
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QSplitter,
    QFrame, QTextBrowser, QHeaderView,
    QListWidget, QListWidgetItem,
)

from app.frontend.models import chart_model, user_model
from app.frontend.workers.api_worker import ApiWorker
from app.frontend.data.interpretations import transit_to_natal_text
from app.frontend.widgets import chart_info
from app.frontend.widgets.chart_wheel import (
    ZodiacWheel, PLANET_GLYPHS, PLANET_COLORS, ANGLE_NAMES, ASPECT_COLORS,
)
from app.frontend.widgets.chart_info import TRANSIT_BADGE_COLORS

# ── UI dimensions (px) ───────────────────────────────────────────────────────
SIDEBAR_MIN        = 340
SIDEBAR_MAX        = 550
SIDEBAR_WIDTH_FRAC = 0.20   # sidebar width as fraction of total window width

INFO_COL_WIDTH     = 255
HEADER_HEIGHT      = 40
STATUS_HEIGHT      = 20
RECALC_BTN_WIDTH   = 110
TABLE_DEGREE_COL_W = 72   # fixed width of the degree column in the planet table

_ASPECT_ABBR = {
    "conjunction": "cnj", "sextile": "sxt", "square": "sqr",
    "trine": "tri", "opposition": "opp",
}

_DETAIL_ROLE = Qt.ItemDataRole.UserRole + 1   # (natal_planet, aspect) tuple


class _TransitList(QListWidget):
    transit_entered = pyqtSignal(str)                # planet name → wheel highlight
    transit_detail  = pyqtSignal(str, str, str)      # transit_planet, natal_planet, aspect
    transit_left    = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.viewport().setMouseTracking(True)
        self.viewport().installEventFilter(self)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                font-size: 12px;
                padding: 0px;
            }
            QListWidget::item { padding: 3px 4px; border-radius: 3px; }
            QListWidget::item:hover { background: #1a1a3a; }
        """)
        self._hovered_name = ""

    def eventFilter(self, obj, event):
        if obj is self.viewport():
            t = event.type()
            if t == QEvent.Type.MouseMove:
                item = self.itemAt(event.pos())
                name = (item.data(Qt.ItemDataRole.UserRole) or "") if item else ""
                if name != self._hovered_name:
                    self._hovered_name = name
                    if name:
                        self.transit_entered.emit(name)
                        detail = item.data(_DETAIL_ROLE)
                        if detail:
                            self.transit_detail.emit(name, detail[0], detail[1])
                    else:
                        self.transit_left.emit()
            elif t == QEvent.Type.Leave:
                if self._hovered_name:
                    self._hovered_name = ""
                    self.transit_left.emit()
        return super().eventFilter(obj, event)


class ChartView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._worker: ApiWorker | None = None
        self._transit_worker: ApiWorker | None = None
        self._transit_aspect_worker: ApiWorker | None = None
        self._transit_windows_worker: ApiWorker | None = None
        self._sky_windows_worker: ApiWorker | None = None
        self._sky_aspect_worker: ApiWorker | None = None
        self._user_worker: ApiWorker | None = None
        self._chart: chart_model.ChartData | None = None
        self._transit_aspects: chart_model.TransitData | None = None
        self._transit_windows: dict[tuple, list[chart_model.TransitWindow]] = {}
        self._sky_windows: dict[tuple, list[chart_model.TransitWindow]] = {}
        self._planet_names: list[str] = []
        self._table_mode: str = "natal"   # "natal" or "transit"
        self._locked_planet: str = ""
        self._locked_transit: str = ""
        self._panel_expanded: set[str] = {"placement"}   # expanded by default
        self._build_ui()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        sidebar_w = max(SIDEBAR_MIN, min(SIDEBAR_MAX, round(self.width() * SIDEBAR_WIDTH_FRAC)))
        wheel_w   = max(0, self.width() - INFO_COL_WIDTH - sidebar_w)
        self._splitter.setSizes([INFO_COL_WIDTH, wheel_w, sidebar_w])

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ── Header bar ────────────────────────────────────────────
        header_bar = QWidget()
        header_bar.setFixedHeight(HEADER_HEIGHT)
        header = QHBoxLayout(header_bar)
        header.setContentsMargins(12, 0, 12, 0)
        self.zodiac_label = QLabel("")
        self.zodiac_label.setStyleSheet("color: #888;")
        self.recalc_btn = QPushButton("Recalculate")
        self.recalc_btn.setFixedWidth(RECALC_BTN_WIDTH)
        self.recalc_btn.clicked.connect(self._on_recalculate)
        header.addStretch()
        header.addWidget(self.zodiac_label)
        header.addSpacing(12)
        header.addWidget(self.recalc_btn)
        layout.addWidget(header_bar)

        # ── Main area ─────────────────────────────────────────────
        self._splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter = self._splitter
        splitter.setChildrenCollapsible(False)

        self.wheel = ZodiacWheel()

        # ── Info column ───────────────────────────────────────────
        info_col = QWidget()
        info_col.setFixedWidth(INFO_COL_WIDTH)
        info_col.setStyleSheet("background: #0d0d1a;")
        ic_layout = QVBoxLayout(info_col)
        ic_layout.setContentsMargins(8, 10, 8, 8)
        ic_layout.setSpacing(8)
        self.title_label = QLabel("Natal Chart")
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #c0c0e0;")
        ic_layout.addWidget(self.title_label)

        _meta_style = "color: #8080aa; font-size: 12px;"
        self.user_name_label = QLabel("")
        self.user_name_label.setStyleSheet(_meta_style)
        self.user_name_label.setWordWrap(True)
        self.user_birth_label = QLabel("")
        self.user_birth_label.setStyleSheet(_meta_style)
        self.user_location_label = QLabel("")
        self.user_location_label.setStyleSheet(_meta_style)
        self.user_location_label.setWordWrap(True)
        ic_layout.addWidget(self.user_name_label)
        ic_layout.addWidget(self.user_birth_label)
        ic_layout.addWidget(self.user_location_label)
        ic_layout.addSpacing(16)

        filter_title = QLabel("Display")
        filter_title.setStyleSheet("font-size: 13px; font-weight: bold; color: #c0c0e0;")
        ic_layout.addWidget(filter_title)
        ic_layout.addWidget(self.wheel.filter_box)
        ic_layout.addSpacing(16)

        transits_title = QLabel("Significant Transits")
        transits_title.setStyleSheet("font-size: 13px; font-weight: bold; color: #c0c0e0;")
        ic_layout.addWidget(transits_title)

        self._transit_list = _TransitList()
        self._transit_list.transit_entered.connect(self.wheel.set_external_transit_hover)
        self._transit_list.transit_detail.connect(self._on_transit_list_detail)
        self._transit_list.transit_left.connect(self._on_transit_list_left)
        ic_layout.addWidget(self._transit_list)

        self._transit_interp = QLabel("")
        self._transit_interp.setWordWrap(True)
        self._transit_interp.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._transit_interp.setStyleSheet(
            "color: #7070a0; font-size: 11px; padding: 4px 4px 0 4px;"
        )
        ic_layout.addWidget(self._transit_interp, stretch=1)

        splitter.addWidget(info_col)

        splitter.addWidget(self.wheel)

        # ── Right sidebar ─────────────────────────────────────────
        sidebar = QWidget()
        sidebar.setMinimumWidth(SIDEBAR_MIN)
        sidebar.setMaximumWidth(SIDEBAR_MAX)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(8, 8, 8, 8)
        sb_layout.setSpacing(0)

        # Planet table — sized to fit content exactly
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Natal Planet", "Sign", "Degree"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(2, TABLE_DEGREE_COL_W)
        self.table.currentCellChanged.connect(lambda row, *_: self._on_row_hover(row))
        sb_layout.addWidget(self.table)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #2a2a50; margin: 8px 0;")
        sb_layout.addWidget(line)

        # Planet info panel
        self.info_panel = QTextBrowser()
        self.info_panel.setOpenLinks(False)
        self.info_panel.anchorClicked.connect(self._on_info_anchor)
        self.info_panel.setStyleSheet("""
            QTextBrowser {
                background: transparent;
                border: none;
                color: #c0c0e0;
                font-size: 14px;
            }
        """)
        self.info_panel.setPlaceholderText("Hover a planet, sign, or house to see details.")
        sb_layout.addWidget(self.info_panel, stretch=1)

        splitter.addWidget(sidebar)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setStretchFactor(2, 0)
        splitter.setSizes([INFO_COL_WIDTH, 10000 - INFO_COL_WIDTH - SIDEBAR_MIN, SIDEBAR_MIN])
        layout.addWidget(splitter, stretch=1)

        self.wheel.planet_hovered.connect(self._on_wheel_hover)
        self.wheel.transit_hovered.connect(self._on_transit_hover)
        self.wheel.sign_hovered.connect(self._on_sign_hover)
        self.wheel.house_hovered.connect(self._on_house_hover)
        self.wheel.planet_locked.connect(self._on_planet_locked)
        self.wheel.transit_locked.connect(self._on_transit_locked)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFixedHeight(STATUS_HEIGHT)
        self.status_label.setStyleSheet("color: #555; font-size: 11px;")
        layout.addWidget(self.status_label)

    def load(self, user_id: str):
        self._user_id = user_id
        self._fetch(chart_model.load_chart)
        self._user_worker = ApiWorker(user_model.get_user, user_id)
        self._user_worker.result.connect(self._on_user)
        self._user_worker.error.connect(lambda _: None)
        self._user_worker.start()

    def _on_user(self, user: user_model.UserDetail | None):
        if not user:
            return
        try:
            dt = datetime.fromisoformat(user.birth_datetime)
            birth_str = dt.strftime("%-d %B %Y")
        except ValueError:
            birth_str = user.birth_datetime
        parts = [p.strip() for p in user.birth_location.split(",")]
        location_str = ", ".join([parts[0], parts[-2], parts[-1]]) if len(parts) >= 3 else user.birth_location
        self.user_name_label.setText(user.name)
        self.user_birth_label.setText(birth_str)
        self.user_location_label.setText(location_str)

    def _on_recalculate(self):
        if self._user_id:
            self._fetch(chart_model.calculate_chart)

    def _fetch(self, fn):
        if not self._user_id:
            return
        self.status_label.setText("Loading…")
        self._worker = ApiWorker(fn, self._user_id)
        self._worker.result.connect(self._on_chart)
        self._worker.error.connect(self._on_error)
        self._worker.start()

    def _fetch_transits(self):
        if not self._user_id:
            return
        for w in (self._transit_worker, self._transit_aspect_worker,
                  self._transit_windows_worker, self._sky_windows_worker,
                  self._sky_aspect_worker):
            if w is not None:
                w.cancel()
        self._transit_worker = ApiWorker(chart_model.load_transit_positions, self._user_id)
        self._transit_worker.result.connect(self._on_transits)
        self._transit_worker.error.connect(lambda _: None)
        self._transit_worker.start()

        self._transit_aspect_worker = ApiWorker(chart_model.load_transits, self._user_id)
        self._transit_aspect_worker.result.connect(self._on_transit_aspects)
        self._transit_aspect_worker.error.connect(lambda _: None)
        self._transit_aspect_worker.start()

        self._transit_windows_worker = ApiWorker(chart_model.load_transit_windows, self._user_id)
        self._transit_windows_worker.result.connect(self._on_transit_windows)
        self._transit_windows_worker.error.connect(lambda _: None)
        self._transit_windows_worker.start()

        self._sky_windows_worker = ApiWorker(chart_model.load_sky_windows, self._user_id)
        self._sky_windows_worker.result.connect(self._on_sky_windows)
        self._sky_windows_worker.error.connect(lambda _: None)
        self._sky_windows_worker.start()

        self._sky_aspect_worker = ApiWorker(chart_model.load_sky_aspects, self._user_id)
        self._sky_aspect_worker.result.connect(self._on_sky_aspects)
        self._sky_aspect_worker.error.connect(lambda _: None)
        self._sky_aspect_worker.start()

    def _on_transit_list_detail(self, transit_planet: str, natal_planet: str, aspect: str):
        self.wheel.set_external_transit_hover(transit_planet)
        text = transit_to_natal_text(transit_planet, natal_planet, aspect)
        self._transit_interp.setText(text or "")

    def _on_transit_list_left(self):
        self.wheel.set_external_transit_hover("")
        self._transit_interp.setText("")

    def _on_transits(self, transits: chart_model.ChartData | None):
        self.wheel.set_transits(transits)

    def _on_transit_aspects(self, data: chart_model.TransitData | None):
        self._transit_aspects = data
        self.wheel.set_transit_aspects(data)
        self._populate_transit_list()

    def _populate_transit_list(self):
        self._transit_list.clear()
        if not self._transit_aspects:
            return
        for t in self._transit_aspects.transits:
            if t.category not in ("major", "notable"):
                continue
            abbr = _ASPECT_ABBR.get(t.aspect, t.aspect[:3])
            if t.days_to_exact is None:
                timing = ""
            elif abs(t.days_to_exact) < 1:
                timing = " · exact"
            elif t.days_to_exact > 0:
                timing = f" · exact in {t.days_to_exact:.0f}d"
            else:
                timing = f" · {abs(t.days_to_exact):.0f}d past exact"
            ws = self._transit_windows.get((t.transit_planet, t.natal_planet, t.aspect), [])
            date_str = chart_model.format_transit_dates(ws)
            line1 = f"{t.transit_planet} {abbr} {t.natal_planet}{timing}"
            text = f"{line1}\n{date_str}" if date_str else line1
            item = QListWidgetItem(text)
            item.setData(Qt.ItemDataRole.UserRole, t.transit_planet)
            item.setData(_DETAIL_ROLE, (t.natal_planet, t.aspect))
            item.setForeground(QColor(TRANSIT_BADGE_COLORS[t.category]))
            self._transit_list.addItem(item)

    def _on_transit_windows(self, results: list[chart_model.TransitWindowResult]):
        self._transit_windows = {
            (r.transit_planet, r.natal_planet, r.aspect): r.windows
            for r in results
        }
        self._populate_transit_list()
        if shown_transit := self._locked_transit or self.wheel.hovered_transit:
            self._show_transit_info(shown_transit)
        if shown_natal := self._locked_planet or self.wheel.hovered:
            self._show_planet_info(shown_natal)

    def _on_sky_windows(self, results: list[chart_model.SkyWindowResult]):
        self._sky_windows = {
            (r.planet1, r.planet2, r.aspect): r.windows
            for r in results
        }
        shown = self._locked_transit or self.wheel.hovered_transit
        if shown:
            self._show_transit_info(shown)

    def _on_sky_aspects(self, aspects: list):
        self.wheel.set_sky_aspects(aspects)

    def _on_chart(self, chart: chart_model.ChartData | None):
        if not chart:
            self.status_label.setText("No chart calculated yet. Press Recalculate.")
            self.wheel.set_chart(None)
            self.table.setRowCount(0)
            return

        self._chart = chart
        self._planet_names = [n for n in chart.positions if n not in ANGLE_NAMES]
        self.status_label.setText("")
        self.zodiac_label.setText(
            f"{chart.zodiac_system.title()} · {chart.house_system.replace('_', ' ').title()}"
        )
        self.wheel.set_chart(chart)
        self._fetch_transits()
        self._populate_table_natal()

    def _populate_table_natal(self):
        if not self._chart:
            return
        self._table_mode = "natal"
        self.table.setHorizontalHeaderLabels(["Natal Planet", "Sign", "Degree"])
        planet_font = QFont()
        planet_font.setPointSize(11)
        planet_rows = [(n, p) for n, p in self._chart.positions.items() if n not in ANGLE_NAMES]
        self.table.setRowCount(len(planet_rows))
        for row, (name, pos) in enumerate(planet_rows):
            glyph = PLANET_GLYPHS.get(name, name)
            item = QTableWidgetItem(f"{glyph}  {name}")
            item.setForeground(QColor(PLANET_COLORS.get(name, "#ffffff")))
            item.setFont(planet_font)
            self.table.setItem(row, 0, item)
            self.table.setItem(row, 1, QTableWidgetItem(pos.sign))
            self.table.setItem(row, 2, QTableWidgetItem(f"  {pos.degree:.2f}°"))
        self._resize_table()

    def _populate_table_transit(self):
        transits = self.wheel.transits
        if not transits:
            return
        self._table_mode = "transit"
        self.table.setHorizontalHeaderLabels(["Transit Planet", "Sign", "Degree"])
        planet_font = QFont()
        planet_font.setPointSize(11)
        self.table.setRowCount(len(transits.positions))
        for row, (name, pos) in enumerate(transits.positions.items()):
            glyph = PLANET_GLYPHS.get(name, name)
            item = QTableWidgetItem(f"{glyph}  {name}")
            item.setForeground(QColor(PLANET_COLORS.get(name, "#ffffff")))
            item.setFont(planet_font)
            self.table.setItem(row, 0, item)
            self.table.setItem(row, 1, QTableWidgetItem(pos.sign))
            self.table.setItem(row, 2, QTableWidgetItem(f"  {pos.degree:.2f}°"))
        self._resize_table()

    def _resize_table(self):
        row_h = self.table.rowHeight(0) if self.table.rowCount() > 0 else 24
        header_h = self.table.horizontalHeader().height()
        self.table.setFixedHeight(row_h * self.table.rowCount() + header_h + 4)

    def _on_wheel_hover(self, name: str):
        if self._locked_planet:
            # Keep natal table visible with the locked planet's row selected.
            if self._table_mode == "transit":
                self._populate_table_natal()
            if self._locked_planet in self._planet_names:
                self.table.selectRow(self._planet_names.index(self._locked_planet))
            return
        if self._locked_transit:
            return  # transit locked — leave table and text alone
        if self._table_mode == "transit" and name:
            self._populate_table_natal()
        if name and name in self._planet_names:
            self.table.selectRow(self._planet_names.index(name))
        else:
            self.table.clearSelection()
        self._show_planet_info(name)

    def _on_row_hover(self, row: int):
        if self._table_mode == "transit":
            return
        if self._locked_planet or self._locked_transit:
            return
        if not self._chart or row < 0 or row >= len(self._planet_names):
            return
        self._show_planet_info(self._planet_names[row])

    def _on_planet_locked(self, name: str):
        self._locked_planet = name
        self._locked_transit = ""
        if name:
            if self._table_mode == "transit":
                self._populate_table_natal()
            if name in self._planet_names:
                self.table.selectRow(self._planet_names.index(name))
            else:
                self.table.clearSelection()  # angle — not in table
            self._show_planet_info(name)
        else:
            # Unlocked — restore to whatever is currently hovered
            hov = self.wheel.hovered
            if hov and hov in self._planet_names:
                self.table.selectRow(self._planet_names.index(hov))
            else:
                self.table.clearSelection()
            self._show_planet_info(hov)

    def _on_transit_locked(self, name: str):
        self._locked_transit = name
        self._locked_planet = ""
        if name:
            self._populate_table_transit()
            transits = self.wheel.transits
            if transits:
                transit_names = list(transits.positions.keys())
                if name in transit_names:
                    self.table.selectRow(transit_names.index(name))
            self._show_transit_info(name)
        else:
            # Unlocked — restore to whatever is currently hovered
            hov = self.wheel.hovered
            if hov and hov in self._planet_names:
                if self._table_mode == "transit":
                    self._populate_table_natal()
                self.table.selectRow(self._planet_names.index(hov))
            else:
                self.table.clearSelection()
            self._show_planet_info(hov)

    def _on_transit_hover(self, name: str):
        if self._locked_transit:
            # Keep transit table visible with the locked planet's row selected.
            if self._table_mode != "transit":
                self._populate_table_transit()
            transits = self.wheel.transits
            if transits:
                transit_names = list(transits.positions.keys())
                if self._locked_transit in transit_names:
                    self.table.selectRow(transit_names.index(self._locked_transit))
            return
        if self._locked_planet:
            return  # natal locked — leave table and text alone
        if name:
            self._populate_table_transit()
            self._show_transit_info(name)
        else:
            if not self.wheel.hovered and not self.wheel.hovered_sign:
                self._show_planet_info("")

    def _on_sign_hover(self, name: str):
        if self._locked_planet or self._locked_transit:
            return
        if name:
            self._show_sign_info(name)
        elif not self.wheel.hovered and not self.wheel.hovered_house and not self.wheel.hovered_transit:
            self._show_planet_info("")

    def _on_house_hover(self, hnum: int):
        if self._locked_planet or self._locked_transit:
            return
        if hnum:
            self._show_house_info(hnum)
        elif not self.wheel.hovered and not self.wheel.hovered_sign and not self.wheel.hovered_transit:
            self._show_planet_info("")

    def _on_info_anchor(self, url: QUrl):
        href = url.toString()
        if not href.startswith("toggle:"):
            return
        section = href[7:]
        if section in self._panel_expanded:
            self._panel_expanded.discard(section)
        else:
            self._panel_expanded.add(section)
        name = self._locked_planet or self.wheel.hovered
        if name:
            self._show_planet_info(name)
        else:
            t = self._locked_transit or self.wheel.hovered_transit
            if t:
                self._show_transit_info(t)

    # ── Info panel (HTML built in chart_info) ─────────────────────────────────

    def _info_ctx(self) -> chart_info.InfoContext:
        return chart_info.InfoContext(
            chart=self._chart,
            transits=self.wheel.transits,
            transit_aspects=self._transit_aspects,
            natal_aspects=self.wheel.aspects,
            sky_aspects=self.wheel.sky_aspects,
            transit_windows=self._transit_windows,
            sky_windows=self._sky_windows,
            expanded=self._panel_expanded,
            locked_planet=self._locked_planet,
            locked_transit=self._locked_transit,
        )

    def _show_planet_info(self, name: str):
        html = chart_info.planet_info_html(self._info_ctx(), name)
        if html is None:
            self.info_panel.setPlaceholderText("Hover a planet, sign, or house to see details.")
            self.info_panel.setHtml("")
        else:
            self.info_panel.setHtml(html)

    def _show_transit_info(self, name: str):
        html = chart_info.transit_info_html(self._info_ctx(), name)
        if html is not None:
            self.info_panel.setHtml(html)

    def _show_house_info(self, hnum: int):
        html = chart_info.house_info_html(self._info_ctx(), hnum)
        if html is not None:
            self.info_panel.setHtml(html)

    def _show_sign_info(self, name: str):
        html = chart_info.sign_info_html(self._info_ctx(), name)
        if html is not None:
            self.info_panel.setHtml(html)

    def _on_error(self, msg: str):
        self.status_label.setText(f"Error: {msg}")
