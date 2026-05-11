import math
from PyQt6.QtCore import Qt, QRectF, QPointF, pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPainterPath
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QSplitter, QSizePolicy,
    QFrame, QTextBrowser, QHeaderView, QCheckBox,
)

from app.frontend.models import chart_model
from app.frontend.workers.api_worker import ApiWorker

PLANET_GLYPHS = {
    "Sun":        "☉︎", "Moon":      "☽︎", "Mercury":    "☿︎",
    "Venus":      "♀︎", "Mars":      "♂︎", "Jupiter":    "♃︎",
    "Saturn":     "♄︎", "Uranus":    "♅︎", "Neptune":    "♆︎",
    "Pluto":      "⯓",
    "North Node": "☊︎", "South Node": "☋︎",
    "ASC": "Asc", "DSC": "Dsc", "MC": "MC", "IC": "IC",
}

PLANET_COLORS = {
    "Sun": "#FFD700", "Moon": "#C0C0C0", "Mercury": "#cc88ff",
    "Venus": "#FF69B4", "Mars": "#DD1111", "Jupiter": "#FF7A00",
    "Saturn": "#d4be96", "Uranus": "#00CED1", "Neptune": "#4169E1",
    "Pluto": "#C01F6A",
    "North Node": "#90d870", "South Node": "#90d870",
    "ASC": "#e8c85a", "DSC": "#e8c85a", "MC": "#c8a8ff", "IC": "#c8a8ff",
}

ANGLE_NAMES    = {"ASC", "DSC", "MC", "IC"}
ANGLE_COLORS   = {"ASC": "#e8c85a", "DSC": "#e8c85a", "MC": "#c8a8ff", "IC": "#c8a8ff"}
HOUSE_NUMERALS = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"]

# ︎ = variation selector 15: forces text rendering instead of emoji
SIGN_GLYPHS = [s + "︎" for s in ["♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓"]]

SIGN_COLORS = ["#1a1a40", "#141436"] * 6

GLYPH_PT = 34   # planet glyph font size
GLYPH_PX = 44   # approximate rendered pixel size at GLYPH_PT
GLYPH_PT_OVERRIDE = {
    "Pluto":      26,  # ⯓ renders tall; shrink so it fits within GLYPH_PX box
    "North Node": 28,
    "South Node": 28,
}

SIGN_GLYPH_PT = 32  # zodiac sign glyph font size
SIGN_GLYPH_PX = 40  # approximate rendered pixel size at SIGN_GLYPH_PT

TRANSIT_GLYPH_PT = 38  # transit planet glyph font size
TRANSIT_GLYPH_PX = 48  # approximate rendered pixel size at TRANSIT_GLYPH_PT

CLUSTER_THRESHOLD_DEG = 8.0   # planets within this angle form a cluster
STACK_STEP_FRACTION = 0.20    # step as fraction of natal zone width

SIGN_NAMES = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
]

SIGN_INFO = {
    "Aries":       ("Fire · Cardinal",  "Bold, pioneering, impulsive. The initiator — action-first, questions later. Rules self and new beginnings."),
    "Taurus":      ("Earth · Fixed",    "Steady, sensual, stubborn. Builds slowly but endures. Rules beauty, money, and the pleasures of the material world."),
    "Gemini":      ("Air · Mutable",    "Curious, adaptable, restless. The twin mind — thrives on variety and conversation. Rules communication and intellect."),
    "Cancer":      ("Water · Cardinal", "Nurturing, intuitive, protective. The caretaker — deeply feeling, home-oriented. Rules family and emotional security."),
    "Leo":         ("Fire · Fixed",     "Radiant, proud, generous. The performer — wants to shine and be seen. Rules creativity, romance, and self-expression."),
    "Virgo":       ("Earth · Mutable",  "Precise, helpful, discerning. The craftsperson — improves everything it touches. Rules health, service, and daily routine."),
    "Libra":       ("Air · Cardinal",   "Harmonious, fair, indecisive. The diplomat — seeks balance and beauty in all things. Rules relationships and justice."),
    "Scorpio":     ("Water · Fixed",    "Intense, perceptive, transformative. The detective — digs beneath the surface. Rules death, rebirth, and shared resources."),
    "Sagittarius": ("Fire · Mutable",   "Adventurous, philosophical, blunt. The wanderer — seeks meaning across horizons. Rules travel, wisdom, and belief."),
    "Capricorn":   ("Earth · Cardinal", "Ambitious, disciplined, patient. The builder — plays the long game. Rules career, authority, and lasting legacy."),
    "Aquarius":    ("Air · Fixed",      "Innovative, rebellious, detached. The visionary — thinks in systems and futures. Rules community, ideals, and technology."),
    "Pisces":      ("Water · Mutable",  "Dreamy, compassionate, boundless. The mystic — dissolves boundaries and feels everything. Rules spirituality and the unconscious."),
}

ASPECT_COLORS = {
    "conjunction": "#FFD700",
    "sextile":     "#4488ff",
    "square":      "#ff4444",
    "trine":       "#44bb88",
    "opposition":  "#ff8800",
}


def _angle_to_xy(cx, cy, r, longitude_deg):
    rad = math.radians(90 - longitude_deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def _assign_radii(positions: dict, radius_natal: float,
                  radius_inner: float, radius_zodiac_inner: float,
                  stack_step: float,
                  cluster_threshold: float = CLUSTER_THRESHOLD_DEG) -> dict:
    """Return {name: radius} with conjunct planets zigzag-stacked in the natal zone."""
    sorted_planets = sorted(positions.items(), key=lambda x: x[1].longitude)
    radii = {}
    i = 0
    while i < len(sorted_planets):
        cluster = [sorted_planets[i]]
        j = i + 1
        while j < len(sorted_planets):
            if sorted_planets[j][1].longitude - sorted_planets[i][1].longitude <= cluster_threshold:
                cluster.append(sorted_planets[j])
                j += 1
            else:
                break
        offsets = []
        for k in range(len(cluster)):
            if k == 0:
                offsets.append(0)
            elif k % 2 == 1:
                offsets.append(((k + 1) // 2) * stack_step)
            else:
                offsets.append(-(k // 2) * stack_step)
        for (name, _), offset in zip(cluster, offsets):
            r = radius_natal + offset
            r = max(r, radius_inner)
            r = min(r, radius_zodiac_inner)
            radii[name] = r
        i = j
    return radii


class _ZodiacWheel(QWidget):
    planet_hovered  = pyqtSignal(str)   # natal planet name, or "" for none
    transit_hovered = pyqtSignal(str)   # transit planet name, or "" for none
    sign_hovered    = pyqtSignal(str)   # sign name, or "" for none

    def __init__(self, parent=None):
        super().__init__(parent)
        self._chart: chart_model.ChartData | None = None
        self._transits: chart_model.ChartData | None = None
        self._transit_aspects: chart_model.TransitData | None = None
        self._aspects: list[chart_model.NatalAspect] = []
        self._planet_positions: dict[str, tuple[float, float]] = {}
        self._transit_positions: dict[str, tuple[float, float]] = {}
        self._sign_positions:   dict[str, tuple[float, float]] = {}
        self._hovered:         str = ""
        self._hovered_transit: str = ""
        self._hovered_sign:    str = ""
        self._house_cusps: list[float] | None = None
        self.setMinimumSize(420, 420)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMouseTracking(True)

        self._filter_box = QFrame(self)
        self._filter_box.setStyleSheet("""
            QFrame {
                background: rgba(10, 10, 30, 180);
                border: 1px solid #2a2a50;
                border-radius: 6px;
            }
            QCheckBox { color: #9090cc; font-size: 12px; padding: 2px 6px; }
            QCheckBox::indicator { width: 13px; height: 13px; }
        """)
        fb_layout = QVBoxLayout(self._filter_box)
        fb_layout.setContentsMargins(6, 6, 6, 6)
        fb_layout.setSpacing(2)
        self._cb_natal           = QCheckBox("Natal Planets")
        self._cb_natal_aspects   = QCheckBox("Natal Aspects")
        self._cb_transits        = QCheckBox("Transit Planets")
        self._cb_transit_aspects = QCheckBox("Transit Aspects")
        self._cb_hover_aspects   = QCheckBox("Hover Aspects")
        self._cb_labels          = QCheckBox("Circle Labels")
        self._cb_houses          = QCheckBox("Houses")
        self._cb_natal.setChecked(True)
        self._cb_natal_aspects.setChecked(True)
        self._cb_transits.setChecked(True)
        self._cb_transit_aspects.setChecked(False)
        self._cb_hover_aspects.setChecked(True)
        self._cb_labels.setChecked(True)
        self._cb_houses.setChecked(True)
        fb_layout.addWidget(self._cb_natal)
        fb_layout.addWidget(self._cb_natal_aspects)
        fb_layout.addWidget(self._cb_transits)
        fb_layout.addWidget(self._cb_transit_aspects)
        fb_layout.addWidget(self._cb_hover_aspects)
        fb_layout.addWidget(self._cb_labels)
        fb_layout.addWidget(self._cb_houses)
        self._cb_natal.toggled.connect(self.update)
        self._cb_natal_aspects.toggled.connect(self.update)
        self._cb_transits.toggled.connect(self.update)
        self._cb_transit_aspects.toggled.connect(self.update)
        self._cb_hover_aspects.toggled.connect(self.update)
        self._cb_labels.toggled.connect(self.update)
        self._cb_houses.toggled.connect(self.update)
        self._filter_box.adjustSize()
        self._filter_box.move(10, 10)

    def set_chart(self, chart: chart_model.ChartData | None):
        self._chart = chart
        self._aspects = chart_model.compute_natal_aspects(chart) if chart else []
        self._house_cusps = chart.house_cusps if chart else None
        self._planet_positions.clear()
        self.update()

    def set_transits(self, transits: chart_model.ChartData | None):
        self._transits = transits
        self.update()

    def set_transit_aspects(self, data: chart_model.TransitData | None):
        self._transit_aspects = data
        self.update()

    def mouseMoveEvent(self, event):
        mx, my = event.position().x(), event.position().y()

        hit_planet = ""
        for name, (px, py) in self._planet_positions.items():
            if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < GLYPH_PX / 2 + 4:
                hit_planet = name
                break

        hit_transit = ""
        if not hit_planet:
            for name, (px, py) in self._transit_positions.items():
                if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < TRANSIT_GLYPH_PX / 2 + 4:
                    hit_transit = name
                    break

        hit_sign = ""
        if not hit_planet and not hit_transit:
            for name, (sx, sy) in self._sign_positions.items():
                if math.sqrt((mx - sx) ** 2 + (my - sy) ** 2) < SIGN_GLYPH_PX / 2:
                    hit_sign = name
                    break

        if hit_planet != self._hovered:
            self._hovered = hit_planet
            self.planet_hovered.emit(hit_planet)
            self.update()
        if hit_transit != self._hovered_transit:
            self._hovered_transit = hit_transit
            self.transit_hovered.emit(hit_transit)
            self.update()
        if hit_sign != self._hovered_sign:
            self._hovered_sign = hit_sign
            self.sign_hovered.emit(hit_sign)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)

        show_natal  = self._cb_natal.isChecked()
        show_labels = self._cb_labels.isChecked()

        w, h = self.width(), self.height()
        size = min(w, h) - 24
        cx, cy = w / 2, h / 2
        radius_house_outer  = size / 2                       # new outermost edge (house band outer)
        radius_cosmos       = radius_house_outer * 0.87     # transit zone outer / house band inner
        radius_zodiac_outer = radius_cosmos * 0.82          # outer edge of zodiac band (Ecliptic)
        radius_zodiac_inner = radius_zodiac_outer * 0.87    # inner edge of zodiac band
        radius_inner        = radius_zodiac_outer * 0.60    # inner boundary: aspect web / natal zone
        radius_natal        = (radius_zodiac_inner + radius_inner) / 2  # natal planet zone midpoint
        radius_hub          = radius_zodiac_outer * 0.04    # earth hub

        outer_rect = QRectF(cx - radius_zodiac_outer, cy - radius_zodiac_outer,
                            radius_zodiac_outer * 2, radius_zodiac_outer * 2)

        # ── Base circle ───────────────────────────────────────────
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#0d0d1a")))
        painter.drawEllipse(QPointF(cx, cy), radius_house_outer, radius_house_outer)

        # ── Cosmos ring (outer chart border) ──────────────────────
        painter.setPen(QPen(QColor("#3a3a6a"), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), radius_cosmos, radius_cosmos)

        # ── Zodiac band — 12 alternating wedges ───────────────────
        for i in range(12):
            start = -(i * 30 - 90)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(QColor(SIGN_COLORS[i])))
            painter.drawPie(outer_rect, int(start * 16), int(30 * 16))

        # ── Radial dividers across zodiac band ────────────────────
        painter.setPen(QPen(QColor("#3a3a6a"), 1))
        for i in range(12):
            x1, y1 = _angle_to_xy(cx, cy, radius_zodiac_inner, i * 30)
            x2, y2 = _angle_to_xy(cx, cy, radius_zodiac_outer, i * 30)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # ── Ecliptic ring ─────────────────────────────────────────
        painter.setPen(QPen(QColor("#3a3a6a"), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), radius_zodiac_outer, radius_zodiac_outer)

        # ── Sign glyphs ───────────────────────────────────────────
        glyph_font = QFont()
        glyph_font.setPointSize(SIGN_GLYPH_PT)
        painter.setFont(glyph_font)
        label_r = (radius_zodiac_outer + radius_zodiac_inner) / 2
        half_sign = SIGN_GLYPH_PX / 2
        self._sign_positions.clear()
        for i, glyph in enumerate(SIGN_GLYPHS):
            name = SIGN_NAMES[i]
            angle = i * 30 + 15
            x, y = _angle_to_xy(cx, cy, label_r, angle)
            self._sign_positions[name] = (x, y)
            if name == self._hovered_sign:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, 30)))
                painter.drawEllipse(QPointF(x, y), half_sign + 4, half_sign + 4)
            painter.setPen(QPen(QColor("#c8c8ff") if name == self._hovered_sign else QColor("#9090cc")))
            painter.drawText(QRectF(x - half_sign, y - half_sign, SIGN_GLYPH_PX, SIGN_GLYPH_PX),
                             Qt.AlignmentFlag.AlignCenter, glyph)

        # ── Inner circle — covers centre of wedges ────────────────
        painter.setPen(QPen(QColor("#3a3a6a"), 1))
        painter.setBrush(QBrush(QColor("#0d0d1a")))
        painter.drawEllipse(QPointF(cx, cy), radius_zodiac_inner, radius_zodiac_inner)

        # ── Degree ticks on inner edge of zodiac band ─────────────
        for deg in range(360):
            if deg % 30 == 0:
                continue            # sign boundary already drawn
            tick_outer = radius_zodiac_inner
            if deg % 10 == 0:
                tick_inner = radius_zodiac_inner * 0.955
                painter.setPen(QPen(QColor("#5555aa"), 1))
            elif deg % 5 == 0:
                tick_inner = radius_zodiac_inner * 0.970
                painter.setPen(QPen(QColor("#44447a"), 1))
            else:
                tick_inner = radius_zodiac_inner * 0.984
                painter.setPen(QPen(QColor("#2a2a55"), 1))
            x1, y1 = _angle_to_xy(cx, cy, tick_outer, deg)
            x2, y2 = _angle_to_xy(cx, cy, tick_inner, deg)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # ── House ring border ─────────────────────────────────────
        painter.setPen(QPen(QColor("#2a2a50"), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), radius_inner, radius_inner)

        # ── Outer house band + angle axes ─────────────────────────
        self._planet_positions.clear()
        houses_on = self._cb_houses.isChecked() and bool(self._house_cusps)
        if houses_on:
            cusps = self._house_cusps
            house_outer_rect = QRectF(cx - radius_house_outer, cy - radius_house_outer,
                                      2 * radius_house_outer, 2 * radius_house_outer)
            cosmos_rect      = QRectF(cx - radius_cosmos, cy - radius_cosmos,
                                      2 * radius_cosmos,      2 * radius_cosmos)
            HOUSE_COLORS = ["#1a1a40", "#141436"] * 6

            # Filled annular sectors
            for i, cusp_lon in enumerate(cusps):
                next_cusp   = cusps[(i + 1) % 12]
                sector_span = (next_cusp - cusp_lon) % 360
                qt_start    = cusp_lon - 90
                path = QPainterPath()
                path.arcMoveTo(house_outer_rect, qt_start)
                path.arcTo(house_outer_rect, qt_start, sector_span)
                path.arcTo(cosmos_rect, qt_start + sector_span, -sector_span)
                path.closeSubpath()
                painter.setPen(Qt.PenStyle.NoPen)
                painter.fillPath(path, QBrush(QColor(HOUSE_COLORS[i])))

            # Cusp divider lines: cosmos → house_outer
            painter.setPen(QPen(QColor("#3a3a6a"), 1))
            for cusp_lon in cusps:
                x1, y1 = _angle_to_xy(cx, cy, radius_cosmos,      cusp_lon)
                x2, y2 = _angle_to_xy(cx, cy, radius_house_outer,  cusp_lon)
                painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

            # House numerals centred in each sector
            num_font = QFont()
            num_font.setPointSize(8)
            painter.setFont(num_font)
            label_r_band = (radius_cosmos + radius_house_outer) / 2
            for i, cusp_lon in enumerate(cusps):
                next_cusp   = cusps[(i + 1) % 12]
                sector_span = (next_cusp - cusp_lon) % 360
                mid_lon     = (cusp_lon + sector_span / 2) % 360
                lx, ly = _angle_to_xy(cx, cy, label_r_band, mid_lon)
                painter.setPen(QPen(QColor("#7070a0")))
                painter.drawText(QRectF(lx - 10, ly - 8, 20, 16),
                                 Qt.AlignmentFlag.AlignCenter, HOUSE_NUMERALS[i])

            # Outer ring border
            painter.setPen(QPen(QColor("#2a2a50"), 1))
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawEllipse(QPointF(cx, cy), radius_house_outer, radius_house_outer)

        # Angle axes (always visible when chart loaded; length depends on Houses toggle)
        axis_end      = radius_house_outer if houses_on else radius_zodiac_outer
        angle_label_r = (radius_cosmos + radius_house_outer) / 2 if houses_on else radius_zodiac_inner * 0.945
        lbl_font = QFont()
        lbl_font.setPointSize(16)
        lbl_font.setBold(True)
        for angle_name in ("ASC", "DSC", "MC", "IC"):
            if not self._chart or angle_name not in self._chart.positions:
                continue
            lon    = self._chart.positions[angle_name].longitude
            color  = QColor(ANGLE_COLORS[angle_name])
            is_hov = angle_name == self._hovered
            width  = 2.5 if is_hov else 1.5
            if is_hov:
                color = color.lighter(130)
            else:
                color.setAlpha(200)
            painter.setPen(QPen(color, width))
            x1, y1 = _angle_to_xy(cx, cy, radius_hub, lon)
            x2, y2 = _angle_to_xy(cx, cy, axis_end,   lon)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

            lx, ly = _angle_to_xy(cx, cy, angle_label_r, lon)
            self._planet_positions[angle_name] = (lx, ly)
            painter.setFont(lbl_font)
            lbl_color = QColor(ANGLE_COLORS[angle_name])
            if is_hov:
                lbl_color = lbl_color.lighter(130)
            painter.setPen(QPen(lbl_color))
            painter.drawText(QRectF(lx - 24, ly - 12, 48, 24),
                             Qt.AlignmentFlag.AlignCenter, angle_name)

        # ── Aspect lines ──────────────────────────────────────────
        if show_natal and self._cb_natal_aspects.isChecked() and self._chart and self._aspects:
            arc_step = radius_inner * 0.015
            for asp in self._aspects:
                lon1 = self._chart.positions[asp.planet1].longitude
                lon2 = self._chart.positions[asp.planet2].longitude
                color = QColor(ASPECT_COLORS.get(asp.aspect, "#888"))
                color.setAlpha(160)
                painter.setPen(QPen(color, 1.0))

                if asp.aspect == "conjunction":
                    # Three concentric arcs curving along the inner ring
                    a1, a2 = min(lon1, lon2), max(lon1, lon2)
                    if a2 - a1 > 180:
                        a1, a2 = a2, a1 + 360
                    start_qt = a1 - 90
                    sweep_qt = a2 - a1
                    for k in range(3):
                        r = radius_inner + k * arc_step
                        rect = QRectF(cx - r, cy - r, 2 * r, 2 * r)
                        path = QPainterPath()
                        path.arcMoveTo(rect, start_qt)
                        path.arcTo(rect, start_qt, sweep_qt)
                        painter.drawPath(path)
                else:
                    x1, y1 = _angle_to_xy(cx, cy, radius_inner, lon1)
                    x2, y2 = _angle_to_xy(cx, cy, radius_inner, lon2)
                    painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # ── Transit-to-natal aspect lines ────────────────────────
        show_transits_on = self._cb_transits.isChecked()
        show_all_t_asp   = show_transits_on and self._cb_transit_aspects.isChecked()
        show_hover_t_asp = show_transits_on and self._cb_hover_aspects.isChecked() and bool(self._hovered_transit)
        show_angle_t_asp = show_transits_on and self._cb_hover_aspects.isChecked() and self._hovered in ANGLE_NAMES
        if (show_all_t_asp or show_hover_t_asp or show_angle_t_asp) and self._transit_aspects and self._chart:
            dash_pen = QPen()
            dash_pen.setWidth(1)
            dash_pen.setStyle(Qt.PenStyle.DashLine)
            for t in self._transit_aspects.transits:
                if not show_all_t_asp:
                    if show_hover_t_asp and t.transit_planet == self._hovered_transit:
                        pass
                    elif show_angle_t_asp and t.natal_planet == self._hovered:
                        pass
                    else:
                        continue
                if t.natal_planet not in self._chart.positions:
                    continue
                if not self._transits or t.transit_planet not in self._transits.positions:
                    continue
                color = QColor(ASPECT_COLORS.get(t.aspect, "#888"))
                color.setAlpha(110)
                dash_pen.setColor(color)
                painter.setPen(dash_pen)
                t_lon = self._transits.positions[t.transit_planet].longitude
                n_lon = self._chart.positions[t.natal_planet].longitude
                tx, ty = _angle_to_xy(cx, cy, radius_zodiac_outer, t_lon)
                n_r    = radius_cosmos if t.natal_planet in ANGLE_NAMES else radius_inner
                nx, ny = _angle_to_xy(cx, cy, n_r, n_lon)
                painter.drawLine(QPointF(tx, ty), QPointF(nx, ny))

        # ── Planet glyphs ─────────────────────────────────────────
        if show_natal and self._chart:
            natal_zone = radius_zodiac_inner - radius_inner
            planet_positions_only = {
                name: pos for name, pos in self._chart.positions.items()
                if name not in ANGLE_NAMES
            }
            planet_radii = _assign_radii(
                planet_positions_only,
                radius_natal, radius_inner, radius_zodiac_inner,
                stack_step=natal_zone * STACK_STEP_FRACTION,
            )
            planet_font = QFont()
            planet_font.setPointSize(GLYPH_PT)
            painter.setFont(planet_font)
            half = GLYPH_PX / 2

            # Tick lines — full natal zone width (planets only)
            for name, pos in planet_positions_only.items():
                color = QColor(PLANET_COLORS.get(name, "#ffffff"))
                if name == self._hovered:
                    color = color.lighter(130)
                    painter.setPen(QPen(color, 2.0))
                else:
                    color.setAlpha(140)
                    painter.setPen(QPen(color, 1.0))
                tx, ty = _angle_to_xy(cx, cy, radius_zodiac_inner, pos.longitude)
                gx, gy = _angle_to_xy(cx, cy, radius_inner,   pos.longitude)
                painter.drawLine(QPointF(tx, ty), QPointF(gx, gy))

            for name, pos in planet_positions_only.items():
                glyph = PLANET_GLYPHS.get(name, name[:2])
                gx, gy = _angle_to_xy(cx, cy, planet_radii[name], pos.longitude)
                self._planet_positions[name] = (gx, gy)
                color = QColor(PLANET_COLORS.get(name, "#ffffff"))
                is_hovered = name == self._hovered

                pt = GLYPH_PT_OVERRIDE.get(name, GLYPH_PT)
                if pt != GLYPH_PT:
                    f = QFont()
                    f.setPointSize(pt)
                    painter.setFont(f)
                else:
                    painter.setFont(planet_font)

                if is_hovered:
                    painter.setPen(Qt.PenStyle.NoPen)
                    painter.setBrush(QBrush(QColor(255, 255, 255, 30)))
                    painter.drawEllipse(QPointF(gx, gy), half + 4, half + 4)

                painter.setPen(QPen(QColor("#ffffff") if is_hovered else color))
                painter.drawText(QRectF(gx - half, gy - half, GLYPH_PX, GLYPH_PX),
                                 Qt.AlignmentFlag.AlignCenter, glyph)

        # ── Transit planet glyphs ─────────────────────────────────
        show_transits = self._cb_transits.isChecked()
        if show_transits and self._transits:
            transit_zone = radius_cosmos - radius_zodiac_outer
            radius_transit_mid = (radius_zodiac_outer + radius_cosmos) / 2
            transit_radii = _assign_radii(
                self._transits.positions,
                radius_transit_mid, radius_zodiac_outer, radius_cosmos,
                stack_step=transit_zone * STACK_STEP_FRACTION,
                cluster_threshold=5.0,
            )
            transit_font = QFont()
            transit_font.setPointSize(TRANSIT_GLYPH_PT)
            painter.setFont(transit_font)
            half_t = TRANSIT_GLYPH_PX / 2

            # Tick lines across transit zone
            for name, pos in self._transits.positions.items():
                color = QColor(PLANET_COLORS.get(name, "#ffffff"))
                if name == self._hovered_transit:
                    color = color.lighter(130)
                    painter.setPen(QPen(color, 2.0))
                else:
                    color.setAlpha(100)
                    painter.setPen(QPen(color, 1.0))
                tx, ty = _angle_to_xy(cx, cy, radius_cosmos,       pos.longitude)
                gx, gy = _angle_to_xy(cx, cy, radius_zodiac_outer, pos.longitude)
                painter.drawLine(QPointF(tx, ty), QPointF(gx, gy))

            # Glyphs — normal color base + blue ghost overlay
            self._transit_positions.clear()
            for name, pos in self._transits.positions.items():
                glyph = PLANET_GLYPHS.get(name, name[:2])
                gx, gy = _angle_to_xy(cx, cy, transit_radii[name], pos.longitude)
                self._transit_positions[name] = (gx, gy)
                color = QColor(PLANET_COLORS.get(name, "#ffffff"))
                is_hovered = name == self._hovered_transit

                pt = round(GLYPH_PT_OVERRIDE[name] * TRANSIT_GLYPH_PT / GLYPH_PT) if name in GLYPH_PT_OVERRIDE else TRANSIT_GLYPH_PT
                f = QFont()
                f.setPointSize(pt)
                painter.setFont(f)

                if is_hovered:
                    painter.setPen(Qt.PenStyle.NoPen)
                    painter.setBrush(QBrush(QColor(255, 255, 255, 30)))
                    painter.drawEllipse(QPointF(gx, gy), half_t + 4, half_t + 4)

                # Base layer — normal planet color
                color.setAlpha(185)
                painter.setPen(QPen(QColor("#ffffff") if is_hovered else color))
                painter.drawText(QRectF(gx - half_t, gy - half_t, TRANSIT_GLYPH_PX, TRANSIT_GLYPH_PX),
                                 Qt.AlignmentFlag.AlignCenter, glyph)

                # Ghost layer — blue on top
                painter.setPen(QPen(QColor(120, 150, 255, 128)))
                painter.drawText(QRectF(gx - half_t, gy - half_t, TRANSIT_GLYPH_PX, TRANSIT_GLYPH_PX),
                                 Qt.AlignmentFlag.AlignCenter, glyph)

                # Retrograde indicator
                if pos.retrograde and name not in ("North Node", "South Node"):
                    rx_font = QFont()
                    rx_font.setPointSize(9)
                    painter.setFont(rx_font)
                    painter.setPen(QPen(QColor(220, 50, 50, 230)))
                    painter.drawText(QRectF(gx + half_t - 6, gy - half_t - 2, 16, 14),
                                     Qt.AlignmentFlag.AlignLeft, "℞")

        # ── Hub ───────────────────────────────────────────────────
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#3a3a6a")))
        painter.drawEllipse(QPointF(cx, cy), radius_hub, radius_hub)

        # ── Circle labels (drawn last — on top of everything) ─────
        if show_labels:
            label_font = QFont()
            label_font.setPointSize(9)
            painter.setFont(label_font)
            label_angle = 215
            radius_aspects     = (radius_hub + radius_inner) / 2
            radius_transit_mid = (radius_zodiac_outer + radius_cosmos) / 2
            radius_zodiac_mid  = (radius_zodiac_inner + radius_zodiac_outer) / 2
            radius_house_mid   = (radius_cosmos + radius_house_outer) / 2
            for radius, text, offset in [
                (radius_hub,          "Earth",           20),
                (radius_aspects,      "Aspects",          8),
                (radius_natal,        "Natal Planets",    0),
                (radius_zodiac_mid,   "Zodiac",           0),
                (radius_transit_mid,  "Transit Planets",  0),
                (radius_house_mid,    "Houses",           0),
            ]:
                lx, ly = _angle_to_xy(cx, cy, radius + offset, label_angle)
                rect = QRectF(lx - 44, ly - 10, 88, 20)
                painter.setPen(QPen(QColor(0, 0, 0, 200)))
                for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                    painter.drawText(rect.translated(dx, dy), Qt.AlignmentFlag.AlignCenter, text)
                painter.setPen(QPen(QColor("#4a4a7a")))
                painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)


PLANET_INFO = {
    "Sun":     ("Leo",        "Identity, vitality, ego, creative power. The core self — what you radiate and what you're becoming."),
    "Moon":    ("Cancer",     "Emotion, instinct, memory, the subconscious. How you nurture and what makes you feel safe."),
    "Mercury": ("Gemini/Virgo","Communication, intellect, perception, travel. How you think, speak, and process information."),
    "Venus":   ("Taurus/Libra","Love, beauty, pleasure, values, money. What you attract and what you find beautiful."),
    "Mars":    ("Aries",      "Drive, desire, courage, aggression, sexuality. How you take action and assert yourself."),
    "Jupiter": ("Sagittarius","Expansion, luck, wisdom, philosophy, abundance. Where life opens up and growth flows easily."),
    "Saturn":  ("Capricorn",  "Discipline, structure, karma, limitation, time. Where you're tested and where you build lasting things."),
    "Uranus":  ("Aquarius",   "Revolution, innovation, disruption, liberation. Where you break rules and crave freedom."),
    "Neptune": ("Pisces",     "Dreams, illusion, spirituality, compassion, dissolution. Where reality blurs and the mystical enters."),
    "Pluto":      ("Scorpio",    "Transformation, power, death and rebirth, the shadow. Where deep and irreversible change happens."),
    "North Node": ("",           "Your karmic path forward — the direction of growth, destiny, and soul evolution in this lifetime."),
    "South Node": ("",           "Your karmic past — innate gifts carried from prior experience, and patterns to release or transcend."),
    "ASC": ("", "The Ascendant — the degree rising on the eastern horizon at birth. Governs the physical body, outward personality, and how others perceive you."),
    "DSC": ("", "The Descendant — the western horizon, opposite the Ascendant. Governs partnerships, close relationships, and the qualities you seek or project onto others."),
    "MC":  ("", "The Midheaven (Medium Coeli) — the highest point of the ecliptic at birth. Governs career, public reputation, ambition, and your relationship with authority."),
    "IC":  ("", "The Imum Coeli — the lowest point, opposite the Midheaven. Governs home, family, ancestry, psychological roots, and private life."),
}


class ChartView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._worker: ApiWorker | None = None
        self._transit_worker: ApiWorker | None = None
        self._transit_aspect_worker: ApiWorker | None = None
        self._chart: chart_model.ChartData | None = None
        self._aspects: list[chart_model.NatalAspect] = []
        self._transit_aspects: chart_model.TransitData | None = None
        self._planet_names: list[str] = []
        self._table_mode: str = "natal"   # "natal" or "transit"
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # ── Header bar ────────────────────────────────────────────
        header_bar = QWidget()
        header_bar.setFixedHeight(40)
        header = QHBoxLayout(header_bar)
        header.setContentsMargins(12, 0, 12, 0)
        self.title_label = QLabel("Natal Chart")
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.zodiac_label = QLabel("")
        self.zodiac_label.setStyleSheet("color: #888;")
        self.recalc_btn = QPushButton("Recalculate")
        self.recalc_btn.setFixedWidth(110)
        self.recalc_btn.clicked.connect(self._on_recalculate)
        header.addWidget(self.title_label)
        header.addStretch()
        header.addWidget(self.zodiac_label)
        header.addSpacing(12)
        header.addWidget(self.recalc_btn)
        layout.addWidget(header_bar)

        # ── Main area ─────────────────────────────────────────────
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setChildrenCollapsible(False)

        self.wheel = _ZodiacWheel()
        splitter.addWidget(self.wheel)

        # ── Right sidebar ─────────────────────────────────────────
        sidebar = QWidget()
        sidebar.setFixedWidth(340)
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
        self.table.setColumnWidth(2, 72)
        self.table.currentCellChanged.connect(lambda row, *_: self._on_row_hover(row))
        sb_layout.addWidget(self.table)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #2a2a50; margin: 8px 0;")
        sb_layout.addWidget(line)

        # Planet info panel
        self.info_panel = QTextBrowser()
        self.info_panel.setOpenExternalLinks(False)
        self.info_panel.setStyleSheet("""
            QTextBrowser {
                background: transparent;
                border: none;
                color: #c0c0e0;
                font-size: 14px;
            }
        """)
        self.info_panel.setPlaceholderText("Hover a planet or sign to see details.")
        sb_layout.addWidget(self.info_panel, stretch=1)

        splitter.addWidget(sidebar)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)
        layout.addWidget(splitter, stretch=1)

        self.wheel.planet_hovered.connect(self._on_wheel_hover)
        self.wheel.transit_hovered.connect(self._on_transit_hover)
        self.wheel.sign_hovered.connect(self._on_sign_hover)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFixedHeight(20)
        self.status_label.setStyleSheet("color: #555; font-size: 11px;")
        layout.addWidget(self.status_label)

    def load(self, user_id: str):
        self._user_id = user_id
        self._fetch(chart_model.load_chart)

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
        self._transit_worker = ApiWorker(chart_model.load_transit_positions, self._user_id)
        self._transit_worker.result.connect(self._on_transits)
        self._transit_worker.error.connect(lambda _: None)
        self._transit_worker.start()

        self._transit_aspect_worker = ApiWorker(chart_model.load_transits, self._user_id)
        self._transit_aspect_worker.result.connect(self._on_transit_aspects)
        self._transit_aspect_worker.error.connect(lambda _: None)
        self._transit_aspect_worker.start()

    def _on_transits(self, transits: chart_model.ChartData | None):
        self.wheel.set_transits(transits)

    def _on_transit_aspects(self, data: chart_model.TransitData | None):
        self._transit_aspects = data
        self.wheel.set_transit_aspects(data)

    def _on_chart(self, chart: chart_model.ChartData | None):
        if not chart:
            self.status_label.setText("No chart calculated yet. Press Recalculate.")
            self.wheel.set_chart(None)
            self.table.setRowCount(0)
            return

        self._chart = chart
        self._aspects = chart_model.compute_natal_aspects(chart)
        self._planet_names = [n for n in chart.positions if n not in ANGLE_NAMES]
        self.status_label.setText("")
        self.zodiac_label.setText(f"Zodiac: {chart.zodiac_system.title()}")
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
        transits = self.wheel._transits
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
        if self._table_mode == "transit" and name:
            self._populate_table_natal()
        if name and name in self._planet_names:
            row = self._planet_names.index(name)
            self.table.selectRow(row)
        else:
            self.table.clearSelection()
        self._show_planet_info(name)

    def _on_row_hover(self, row: int):
        if self._table_mode == "transit":
            return
        if not self._chart or row < 0 or row >= len(self._planet_names):
            return
        self._show_planet_info(self._planet_names[row])

    def _show_planet_info(self, name: str):
        if not name or not self._chart or name not in self._chart.positions:
            self.info_panel.setPlaceholderText("Hover a planet or sign to see details.")
            self.info_panel.setHtml("")
            return
        pos = self._chart.positions[name]
        glyph = PLANET_GLYPHS.get(name, name)
        color = PLANET_COLORS.get(name, "#ffffff")
        ruling, description = PLANET_INFO.get(name, ("", ""))
        is_angle = name in ANGLE_NAMES

        my_aspects = [a for a in self._aspects if a.planet1 == name or a.planet2 == name]
        aspect_lines = ""
        for a in my_aspects:
            other = a.planet2 if a.planet1 == name else a.planet1
            asp_color = ASPECT_COLORS.get(a.aspect, "#888")
            aspect_lines += (
                f'<span style="color:{asp_color}">■</span> '
                f'{a.aspect.title()} {other} '
                f'<span style="color:#555">(orb {a.orb:.1f}°)</span><br>'
            )

        transit_aspect_lines = ""
        if is_angle and self._transit_aspects:
            for t in self._transit_aspects.transits:
                if t.natal_planet != name:
                    continue
                asp_color = ASPECT_COLORS.get(t.aspect, "#888")
                transit_aspect_lines += (
                    f'<span style="color:{asp_color}">╌</span> '
                    f'{t.aspect.title()} transit {t.transit_planet} '
                    f'<span style="color:#555">(orb {t.orb:.1f}°)</span><br>'
                )

        degree_line = f"{pos.sign} {pos.degree:.2f}°"
        if self._chart.house_cusps:
            h = chart_model.get_house_number(pos.longitude, self._chart.house_cusps)
            if h:
                degree_line += f" &nbsp;·&nbsp; House {HOUSE_NUMERALS[h - 1]}"
        if ruling:
            degree_line += f" &nbsp;·&nbsp; rules {ruling}"

        retrograde_tag = "" if is_angle or not pos.retrograde or name in ("North Node", "South Node") else \
            "<p style='color:#cc3333; margin:0 0 4px 0; font-size:11px; letter-spacing:1px;'>℞ RETROGRADE</p>"
        category_tag = (
            "<p style='color:#886633; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;'>NATAL ANGLE</p>"
            if is_angle else
            "<p style='color:#445588; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;'>NATAL PLANET</p>"
        )

        html = f"""
        <p style="font-size:24px; color:{color}; margin:0 0 4px 0;">{glyph} {name}</p>
        <p style="color:#7070a0; margin:0 0 4px 0; font-size:13px;">{degree_line}</p>
        {retrograde_tag}{category_tag}
        <p style="color:#a0a0c0; margin:0 0 14px 0; font-size:14px; line-height:1.6;">
            {description}
        </p>
        {"<p style='color:#666; font-size:13px; margin:0 0 6px 0;'>Natal aspects:</p>" if aspect_lines else ""}
        <p style="font-size:13px; line-height:2.0; margin:0;">{aspect_lines}</p>
        {"<p style='color:#666; font-size:13px; margin:0 0 6px 0;'>Transit aspects:</p>" if transit_aspect_lines else ""}
        <p style="font-size:13px; line-height:2.0; margin:0;">{transit_aspect_lines}</p>
        """
        self.info_panel.setHtml(html)

    def _on_transit_hover(self, name: str):
        if name:
            self._populate_table_transit()
            self._show_transit_info(name)
        else:
            if not self.wheel._hovered and not self.wheel._hovered_sign:
                self._show_planet_info("")

    def _show_transit_info(self, name: str):
        if not name or not self.wheel._transits or name not in self.wheel._transits.positions:
            return
        pos = self.wheel._transits.positions[name]
        glyph = PLANET_GLYPHS.get(name, name)
        color = PLANET_COLORS.get(name, "#ffffff")
        _, description = PLANET_INFO.get(name, ("", ""))

        aspect_lines = ""
        if self._transit_aspects:
            my_transits = [t for t in self._transit_aspects.transits if t.transit_planet == name]
            for t in my_transits:
                asp_color = ASPECT_COLORS.get(t.aspect, "#888")
                aspect_lines += (
                    f'<span style="color:{asp_color}">■</span> '
                    f'{t.aspect.title()} natal {t.natal_planet} '
                    f'<span style="color:#555">(orb {t.orb:.1f}°)</span><br>'
                )

        html = f"""
        <p style="font-size:24px; color:{color}; margin:0 0 4px 0;">{glyph} <b>{name}</b></p>
        <p style="color:#7070a0; margin:0 0 4px 0; font-size:13px;">{pos.sign} {pos.degree:.2f}°{f" &nbsp;·&nbsp; House {HOUSE_NUMERALS[chart_model.get_house_number(pos.longitude, self._chart.house_cusps) - 1]}" if self._chart and self._chart.house_cusps else ""}</p>
        {"<p style='color:#cc3333; margin:0 0 4px 0; font-size:11px; letter-spacing:1px;'>℞ RETROGRADE</p>" if pos.retrograde and name not in ("North Node", "South Node") else ""}
        <p style="color:#4466aa; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;">TRANSIT PLANET</p>
        <p style="color:#a0a0c0; margin:0 0 14px 0; font-size:14px; line-height:1.6;">
            {description}
        </p>
        {"<p style='color:#666; font-size:13px; margin:0 0 6px 0;'>Active transits:</p>" if aspect_lines else ""}
        <p style="font-size:13px; line-height:2.0; margin:0;">{aspect_lines}</p>
        """
        self.info_panel.setHtml(html)

    def _on_sign_hover(self, name: str):
        if name:
            self._show_sign_info(name)
        elif not self.wheel._hovered:
            self._show_planet_info("")

    def _show_sign_info(self, name: str):
        if not name:
            return
        glyph = SIGN_GLYPHS[SIGN_NAMES.index(name)]
        element, description = SIGN_INFO.get(name, ("", ""))
        html = f"""
        <p style="font-size:24px; color:#9090cc; margin:0 0 4px 0;">{glyph} <b>{name}</b></p>
        <p style="color:#7070a0; margin:0 0 10px 0; font-size:13px;">{element}</p>
        <p style="color:#a0a0c0; margin:0 0 14px 0; font-size:14px; line-height:1.6;">
            {description}
        </p>
        """
        self.info_panel.setHtml(html)

    def _on_error(self, msg: str):
        self.status_label.setText(f"Error: {msg}")
