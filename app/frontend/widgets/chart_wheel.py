"""The zodiac wheel: painting, hit-testing, and hover/lock signals.

Also home to the chart's shared visual vocabulary (planet glyphs/colors,
sign names, aspect colors) — chart_view and chart_info import from here.
"""
import math
from dataclasses import dataclass

from PyQt6.QtCore import Qt, QRectF, QPointF, pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QFont, QPainterPath
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QFrame, QCheckBox

from app.frontend.models import chart_model

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
    "ASC": "#c8a8ff", "DSC": "#c8a8ff", "MC": "#c8a8ff", "IC": "#c8a8ff",
}

ANGLE_NAMES    = {"ASC", "DSC", "MC", "IC"}
ANGLE_COLORS   = {"ASC": "#c8a8ff", "DSC": "#c8a8ff", "MC": "#c8a8ff", "IC": "#c8a8ff"}
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

ASPECT_COLORS = {
    "conjunction": "#FFD700",
    "sextile":     "#4488ff",
    "square":      "#ff4444",
    "trine":       "#44bb88",
    "opposition":  "#ff8800",
}

# ── Wheel geometry ────────────────────────────────────────────────────────────
CHART_MARGIN_PX      = 24     # px trimmed from min(w,h) before halving to get base radius
SCALE_REF_SIZE       = 900.0  # wheel size (px) at which scale factor = 1.0
SCALE_MIN            = 0.4    # minimum scale (smallest supported window)

# Radius layers — each as a fraction of the layer above it (outermost → inward)
R_COSMOS_FRAC        = 0.87   # cosmos / house_outer  (transit band outer / house band inner)
R_ZODIAC_OUTER_FRAC  = 0.82   # zodiac_outer / cosmos  (ecliptic ring outer edge)
R_ZODIAC_INNER_FRAC  = 0.87   # zodiac_inner / zodiac_outer  (ecliptic ring inner edge)
R_INNER_FRAC         = 0.60   # inner / zodiac_outer  (aspect-web boundary / natal zone inner)
R_HUB_FRAC           = 0.04   # hub / zodiac_outer  (earth dot radius)

# Degree tick inner-edge as fractions of zodiac_inner
TICK_10DEG_FRAC      = 0.955
TICK_5DEG_FRAC       = 0.970
TICK_1DEG_FRAC       = 0.984

TRANSIT_CLUSTER_DEG       = 5.0    # cluster threshold for transit glyphs (tighter than CLUSTER_THRESHOLD_DEG)
CONJUNCTION_ARC_STEP_FRAC = 0.015  # spacing between the three concentric arcs drawn for conjunctions
CONJUNCTION_ARC_COUNT     = 3

# ── Font sizes (pt at scale 1.0) ──────────────────────────────────────────────
HOUSE_NUM_PT      = 24   # house numeral in the outer band
ANGLE_LABEL_PT    = 16   # ASC / DSC / MC / IC labels
CIRCLE_LABEL_PT   = 9    # ring labels ("Natal Planets", "Zodiac", …)
RETROGRADE_PT     = 9    # ℞ superscript
FONT_FLOOR_NORMAL = 8    # minimum rendered pt for most scaled fonts
FONT_FLOOR_SMALL  = 7    # minimum rendered pt for small annotations

# ── Hit radii and label-box sizes (logical px at scale 1.0) ──────────────────
HOUSE_HIT_RADIUS   = 22   # hover-detection radius for house numerals
ANGLE_LABEL_W      = 48
ANGLE_LABEL_H      = 24
HOUSE_LABEL_W      = 60
HOUSE_LABEL_H      = 48
CIRCLE_LABEL_W     = 88
CIRCLE_LABEL_H     = 20
PLANET_HIT_PAD     = 4    # extra px added to glyph half-size for hover detection
CIRCLE_LABEL_ANGLE = 265  # zodiac longitude at which ring labels are drawn

# ── Pen widths ────────────────────────────────────────────────────────────────
PEN_ANGLE_HOVERED  = 2.5
PEN_ANGLE_NORMAL   = 1.5
PEN_PLANET_HOVERED = 2.0
PEN_PLANET_SPOTLIT = 1.5
PEN_ASPECT_ACTIVE  = 1.6   # hover-related aspect chord
PEN_DEFAULT        = 1.0   # normal/idle line weight

# ── Alpha values (0–255) ─────────────────────────────────────────────────────
ALPHA_HOVER_HALO           = 30   # white halo behind a hovered glyph
ALPHA_NATAL_TICK_NORMAL    = 140  # natal planet tick (idle)
ALPHA_NATAL_TICK_DIM       = 50   # natal planet tick (spotlight dims it)
ALPHA_NATAL_GLYPH_DIM      = 70   # natal planet glyph (spotlight dims it)
ALPHA_TRANSIT_TICK_NORMAL  = 100  # transit planet tick (idle)
ALPHA_TRANSIT_TICK_DIM     = 40   # transit planet tick (spotlight dims it)
ALPHA_TRANSIT_GLYPH_NORMAL = 185  # transit planet glyph (idle)
ALPHA_TRANSIT_GLYPH_DIM    = 60   # transit planet glyph (spotlight dims it)
ALPHA_GHOST_NORMAL         = 128  # blue ghost overlay on transit glyph (idle)
ALPHA_GHOST_DIM            = 40   # blue ghost overlay (spotlight dims it)
ALPHA_NATAL_ASP_ACTIVE     = 160  # natal aspect line (no hover)
ALPHA_NATAL_ASP_RELATED    = 220  # natal aspect line (hover-related)
ALPHA_NATAL_ASP_DIM        = 80   # natal aspect line (hover-unrelated)
ALPHA_TRANSIT_ASP_ACTIVE   = 110  # transit-natal aspect line (no hover)
ALPHA_TRANSIT_ASP_RELATED  = 200  # transit-natal / sky aspect line (hover-related)
ALPHA_TRANSIT_ASP_DIM      = 55   # transit-natal / sky aspect line (hover-unrelated)
ALPHA_RETROGRADE           = 230  # ℞ indicator
ALPHA_LABEL_SHADOW         = 200  # drop-shadow behind circle labels

WHEEL_MIN_SIZE = 420

ANGLE_LABEL_NO_HOUSES_FRAC = 0.945  # angle-label radius (fraction of zodiac_inner) when house lines are hidden

# ── Lock indicator ───────────────────────────────────────────────────────────
COLOR_LOCK      = "#00c8c8"   # teal ring + badge
LOCK_RING_PEN_W = 2.5         # pen width for the teal ring
LOCK_GLYPH_PT   = 9           # pt size of 🔒 drawn on wheel

# ── Wheel colors ─────────────────────────────────────────────────────────────
COLOR_BG            = "#0d0d1a"        # background fill
COLOR_RING          = "#3a3a6a"        # rings, dividers, hub
COLOR_INNER_RING    = "#2a2a50"        # inner-boundary ring
COLOR_SIGN_NORMAL   = "#9090cc"        # zodiac sign glyph (idle)
COLOR_SIGN_HOVERED  = "#c8c8ff"        # zodiac sign glyph (hovered)
COLOR_TICK_10DEG    = "#5555aa"        # 10° degree tick
COLOR_TICK_5DEG     = "#44447a"        # 5° degree tick
COLOR_TICK_1DEG     = "#2a2a55"        # 1° degree tick
COLOR_HOUSE_NUMERAL = "#7070a0"        # house numeral text
COLOR_CIRCLE_LABEL  = "#4a4a7a"        # ring label text
COLOR_TRANSIT_GHOST = (120, 150, 255)  # RGB for the blue ghost overlay on transit glyphs
COLOR_RETROGRADE    = (220, 50, 50)    # RGB for the ℞ indicator


def _angle_to_xy(cx, cy, r, longitude_deg, offset_deg=0):
    # offset_deg rotates the whole chart CW visually. To put ASC at the left
    # (screen 9 o'clock = math angle 180°), pass offset_deg = 90 + asc_longitude.
    rad = math.radians(90 - longitude_deg + offset_deg)
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


@dataclass
class _Geometry:
    """Per-paint layout: centre, scale, rotation, and the ring radii."""
    cx: float
    cy: float
    scale: float
    rot: float
    radius_house_outer: float
    radius_cosmos: float
    radius_zodiac_outer: float
    radius_zodiac_inner: float
    radius_inner: float
    radius_natal: float
    radius_hub: float
    outer_rect: QRectF


@dataclass
class _PaintState:
    """Per-paint hover/lock/filter state shared by the paint stages."""
    any_locked: bool
    eff_hov: str
    eff_hov_transit: str
    hov_active: bool
    spotlight_active: bool
    spotlit_natals: set
    spotlit_transits: set
    show_natal: bool
    show_labels: bool
    show_transits: bool
    angles_on: bool
    houses_on: bool


class ZodiacWheel(QWidget):
    planet_hovered  = pyqtSignal(str)   # natal planet name, or "" for none
    transit_hovered = pyqtSignal(str)   # transit planet name, or "" for none
    sign_hovered    = pyqtSignal(str)   # sign name, or "" for none
    house_hovered   = pyqtSignal(int)   # house number 1-12, or 0 for none
    planet_locked   = pyqtSignal(str)   # locked natal name, or "" to unlock
    transit_locked  = pyqtSignal(str)   # locked transit name, or "" to unlock

    def __init__(self, parent=None):
        super().__init__(parent)
        self._chart: chart_model.ChartData | None = None
        self._transits: chart_model.ChartData | None = None
        self._transit_aspects: chart_model.TransitData | None = None
        self._aspects: list[chart_model.Aspect] = []
        self._planet_positions: dict[str, tuple[float, float]] = {}
        self._transit_positions: dict[str, tuple[float, float]] = {}
        self._sign_positions:   dict[str, tuple[float, float]] = {}
        self._house_positions:  dict[int, tuple[float, float]] = {}
        self._hovered:         str = ""
        self._hovered_transit: str = ""
        self._hovered_sign:    str = ""
        self._hovered_house:   int = 0
        self._locked:          str = ""
        self._locked_transit:  str = ""
        self._house_cusps: list[float] | None = None
        self._sky_aspects: list[chart_model.Aspect] = []
        self._scale: float = 1.0  # updated each paint; used by hit testing
        self.setMinimumSize(WHEEL_MIN_SIZE, WHEEL_MIN_SIZE)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMouseTracking(True)

        self.filter_box = QFrame()
        self.filter_box.setStyleSheet("""
            QCheckBox { color: #9090cc; font-size: 12px; padding: 2px 6px; }
            QCheckBox::indicator { width: 13px; height: 13px; }
        """)
        fb_layout = QVBoxLayout(self.filter_box)
        fb_layout.setContentsMargins(6, 6, 6, 6)
        fb_layout.setSpacing(2)
        self._cb_natal           = QCheckBox("Natal Planets")
        self._cb_natal_aspects   = QCheckBox("Natal Aspects")
        self._cb_transits        = QCheckBox("Transit Planets")
        self._cb_transit_aspects = QCheckBox("Transit-Natal")
        self._cb_sky_aspects     = QCheckBox("Transit-Transit")
        self._cb_labels          = QCheckBox("Circle Labels")
        self._cb_houses          = QCheckBox("Houses")
        self._cb_angles          = QCheckBox("Angles")
        self._cb_natal.setChecked(True)
        self._cb_natal_aspects.setChecked(True)
        self._cb_transits.setChecked(True)
        self._cb_transit_aspects.setChecked(False)
        self._cb_sky_aspects.setChecked(False)
        self._cb_labels.setChecked(True)
        self._cb_houses.setChecked(True)
        self._cb_angles.setChecked(True)
        fb_layout.addWidget(self._cb_angles)
        fb_layout.addWidget(self._cb_natal)
        fb_layout.addWidget(self._cb_natal_aspects)
        fb_layout.addWidget(self._cb_transits)
        fb_layout.addWidget(self._cb_houses)
        fb_layout.addWidget(self._cb_labels)
        fb_layout.addWidget(self._cb_transit_aspects)
        fb_layout.addWidget(self._cb_sky_aspects)
        self._cb_natal.toggled.connect(self.update)
        self._cb_natal_aspects.toggled.connect(self.update)
        self._cb_transits.toggled.connect(self.update)
        self._cb_transit_aspects.toggled.connect(self.update)
        self._cb_sky_aspects.toggled.connect(self.update)
        self._cb_labels.toggled.connect(self.update)
        self._cb_houses.toggled.connect(self.update)
        self._cb_angles.toggled.connect(self.update)

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

    def set_sky_aspects(self, aspects: list[chart_model.Aspect]):
        self._sky_aspects = aspects
        self.update()

    @property
    def transits(self) -> chart_model.ChartData | None:
        return self._transits

    @property
    def aspects(self) -> list[chart_model.Aspect]:
        return self._aspects

    @property
    def sky_aspects(self) -> list[chart_model.Aspect]:
        return self._sky_aspects

    @property
    def hovered(self) -> str:
        return self._hovered

    @property
    def hovered_transit(self) -> str:
        return self._hovered_transit

    @property
    def hovered_sign(self) -> str:
        return self._hovered_sign

    @property
    def hovered_house(self) -> int:
        return self._hovered_house

    def set_external_transit_hover(self, name: str):
        if self._locked_transit:
            return
        if name != self._hovered_transit:
            self._hovered_transit = name
            self.transit_hovered.emit(name)
            self.update()

    def mouseMoveEvent(self, event):
        mx, my = event.position().x(), event.position().y()
        s = self._scale

        hit_planet = ""
        for name, (px, py) in self._planet_positions.items():
            if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < (GLYPH_PX / 2 + PLANET_HIT_PAD) * s:
                hit_planet = name
                break

        hit_transit = ""
        if not hit_planet:
            for name, (px, py) in self._transit_positions.items():
                if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < (TRANSIT_GLYPH_PX / 2 + PLANET_HIT_PAD) * s:
                    hit_transit = name
                    break

        hit_sign = ""
        if not hit_planet and not hit_transit:
            for name, (sx, sy) in self._sign_positions.items():
                if math.sqrt((mx - sx) ** 2 + (my - sy) ** 2) < (SIGN_GLYPH_PX / 2) * s:
                    hit_sign = name
                    break

        hit_house = 0
        if not hit_planet and not hit_transit and not hit_sign:
            for hnum, (hx, hy) in self._house_positions.items():
                if math.sqrt((mx - hx) ** 2 + (my - hy) ** 2) < HOUSE_HIT_RADIUS * s:
                    hit_house = hnum
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
        if hit_house != self._hovered_house:
            self._hovered_house = hit_house
            self.house_hovered.emit(hit_house)
            self.update()

    def mousePressEvent(self, event):
        if event.button() != Qt.MouseButton.LeftButton:
            return
        mx, my = event.position().x(), event.position().y()
        s = self._scale

        hit_natal = ""
        for name, (px, py) in self._planet_positions.items():
            half = (GLYPH_PX / 2 + PLANET_HIT_PAD) * s
            if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < half:
                hit_natal = name
                break

        hit_transit = ""
        if not hit_natal:
            for name, (px, py) in self._transit_positions.items():
                half = (TRANSIT_GLYPH_PX / 2 + PLANET_HIT_PAD) * s
                if math.sqrt((mx - px) ** 2 + (my - py) ** 2) < half:
                    hit_transit = name
                    break

        if hit_natal:
            if self._locked == hit_natal:
                self._locked = ""
            else:
                self._locked = hit_natal
                self._locked_transit = ""
            self.planet_locked.emit(self._locked)
        elif hit_transit:
            if self._locked_transit == hit_transit:
                self._locked_transit = ""
            else:
                self._locked_transit = hit_transit
                self._locked = ""
            self.transit_locked.emit(self._locked_transit)
        else:
            if self._locked or self._locked_transit:
                self._locked = ""
                self._locked_transit = ""
                self.planet_locked.emit("")
                self.transit_locked.emit("")
        self.update()

    # ── Painting ──────────────────────────────────────────────────────────────

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)

        g  = self._compute_geometry()
        st = self._compute_paint_state()
        self._scale = g.scale

        self._paint_zodiac_band(painter, g)
        self._paint_sign_glyphs(painter, g, st)
        self._paint_ticks_and_inner_rings(painter, g)

        self._planet_positions.clear()
        if st.houses_on:
            self._paint_house_band(painter, g, st)
        self._paint_angle_axes(painter, g, st)

        self._paint_natal_aspects(painter, g, st)
        self._paint_transit_natal_aspects(painter, g, st)
        self._paint_sky_aspect_lines(painter, g, st)

        if st.show_natal and self._chart:
            self._paint_natal_planets(painter, g, st)
        if st.show_transits and self._transits:
            self._paint_transit_planets(painter, g, st)

        self._paint_hub(painter, g)
        if st.show_labels:
            self._paint_circle_labels(painter, g)

    def _compute_geometry(self) -> _Geometry:
        # Rotate the whole chart so ASC lands at the left (the horizon line is
        # horizontal). When no chart is loaded, fall back to the legacy
        # "Aries at bottom" layout.
        if self._chart and "ASC" in self._chart.positions:
            rot = (90 + self._chart.positions["ASC"].longitude) % 360
        else:
            rot = 0.0

        w, h = self.width(), self.height()
        size = min(w, h) - CHART_MARGIN_PX
        # Reference size (typical fullscreen) — at this size, scale = 1.0.
        # Below, text/glyphs shrink proportionally; above, they stay at current size.
        scale = max(SCALE_MIN, min(1.0, size / SCALE_REF_SIZE))
        cx, cy = w / 2, h / 2
        radius_house_outer  = size / 2                       # outermost edge (house band outer)
        radius_cosmos       = radius_house_outer * R_COSMOS_FRAC       # transit zone outer / house band inner
        radius_zodiac_outer = radius_cosmos * R_ZODIAC_OUTER_FRAC      # outer edge of zodiac band (Ecliptic)
        radius_zodiac_inner = radius_zodiac_outer * R_ZODIAC_INNER_FRAC # inner edge of zodiac band
        radius_inner        = radius_zodiac_outer * R_INNER_FRAC        # inner boundary: aspect web / natal zone
        radius_natal        = (radius_zodiac_inner + radius_inner) / 2  # natal planet zone midpoint
        radius_hub          = radius_zodiac_outer * R_HUB_FRAC          # earth hub

        outer_rect = QRectF(cx - radius_zodiac_outer, cy - radius_zodiac_outer,
                            radius_zodiac_outer * 2, radius_zodiac_outer * 2)
        return _Geometry(
            cx=cx, cy=cy, scale=scale, rot=rot,
            radius_house_outer=radius_house_outer,
            radius_cosmos=radius_cosmos,
            radius_zodiac_outer=radius_zodiac_outer,
            radius_zodiac_inner=radius_zodiac_inner,
            radius_inner=radius_inner,
            radius_natal=radius_natal,
            radius_hub=radius_hub,
            outer_rect=outer_rect,
        )

    def _compute_paint_state(self) -> _PaintState:
        # Effective hover: locked state overrides physical hover for all highlights.
        any_locked      = bool(self._locked or self._locked_transit)
        eff_hov         = self._locked         or self._hovered
        eff_hov_transit = self._locked_transit or self._hovered_transit

        # Spotlight: when a sign or house is hovered, occupants stay bright,
        # everything else dims. Suppressed entirely when any planet is locked.
        spotlight_active = not any_locked and (bool(self._hovered_sign) or bool(self._hovered_house))
        spotlit_natals: set[str] = set()
        spotlit_transits: set[str] = set()
        if spotlight_active:
            cusps = self._chart.house_cusps if self._chart else None

            def _matches(pos) -> bool:
                if self._hovered_sign:
                    return pos.sign == self._hovered_sign
                if self._hovered_house and cusps:
                    return chart_model.get_house_number(pos.longitude, cusps) == self._hovered_house
                return False

            if self._chart:
                for n, p in self._chart.positions.items():
                    if n not in ANGLE_NAMES and _matches(p):
                        spotlit_natals.add(n)
            if self._transits:
                for n, p in self._transits.positions.items():
                    if n not in ANGLE_NAMES and _matches(p):
                        spotlit_transits.add(n)

        return _PaintState(
            any_locked=any_locked,
            eff_hov=eff_hov,
            eff_hov_transit=eff_hov_transit,
            hov_active=bool(eff_hov) or bool(eff_hov_transit),
            spotlight_active=spotlight_active,
            spotlit_natals=spotlit_natals,
            spotlit_transits=spotlit_transits,
            show_natal=self._cb_natal.isChecked(),
            show_labels=self._cb_labels.isChecked(),
            show_transits=self._cb_transits.isChecked(),
            angles_on=self._cb_angles.isChecked(),
            houses_on=self._cb_houses.isChecked() and bool(self._house_cusps),
        )

    def _paint_zodiac_band(self, painter: QPainter, g: _Geometry):
        # Base circle
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor(COLOR_BG)))
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_house_outer, g.radius_house_outer)

        # Cosmos ring (outer chart border)
        painter.setPen(QPen(QColor(COLOR_RING), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_cosmos, g.radius_cosmos)

        # Zodiac band — 12 alternating wedges
        for i in range(12):
            start = -(i * 30 - 90) - g.rot
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(QColor(SIGN_COLORS[i])))
            painter.drawPie(g.outer_rect, int(start * 16), int(30 * 16))

        # Radial dividers across zodiac band
        painter.setPen(QPen(QColor(COLOR_RING), 1))
        for i in range(12):
            x1, y1 = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_inner, i * 30, g.rot)
            x2, y2 = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_outer, i * 30, g.rot)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # Ecliptic ring
        painter.setPen(QPen(QColor(COLOR_RING), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_zodiac_outer, g.radius_zodiac_outer)

    def _paint_sign_glyphs(self, painter: QPainter, g: _Geometry, st: _PaintState):
        glyph_font = QFont()
        glyph_font.setPointSize(max(FONT_FLOOR_NORMAL, round(SIGN_GLYPH_PT * g.scale)))
        painter.setFont(glyph_font)
        label_r = (g.radius_zodiac_outer + g.radius_zodiac_inner) / 2
        sign_px = SIGN_GLYPH_PX * g.scale
        half_sign = sign_px / 2
        self._sign_positions.clear()
        for i, glyph in enumerate(SIGN_GLYPHS):
            name = SIGN_NAMES[i]
            angle = i * 30 + 15
            x, y = _angle_to_xy(g.cx, g.cy, label_r, angle, g.rot)
            self._sign_positions[name] = (x, y)
            show_sign_hov = not st.any_locked and name == self._hovered_sign
            if show_sign_hov:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, 30)))
                painter.drawEllipse(QPointF(x, y), half_sign + 4 * g.scale, half_sign + 4 * g.scale)
            painter.setPen(QPen(QColor(COLOR_SIGN_HOVERED) if show_sign_hov else QColor(COLOR_SIGN_NORMAL)))
            painter.drawText(QRectF(x - half_sign, y - half_sign, sign_px, sign_px),
                             Qt.AlignmentFlag.AlignCenter, glyph)

    def _paint_ticks_and_inner_rings(self, painter: QPainter, g: _Geometry):
        # Inner circle — covers centre of wedges
        painter.setPen(QPen(QColor(COLOR_RING), 1))
        painter.setBrush(QBrush(QColor(COLOR_BG)))
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_zodiac_inner, g.radius_zodiac_inner)

        # Degree ticks on inner edge of zodiac band
        for deg in range(360):
            if deg % 30 == 0:
                continue            # sign boundary already drawn
            tick_outer = g.radius_zodiac_inner
            if deg % 10 == 0:
                tick_inner = g.radius_zodiac_inner * TICK_10DEG_FRAC
                painter.setPen(QPen(QColor(COLOR_TICK_10DEG), 1))
            elif deg % 5 == 0:
                tick_inner = g.radius_zodiac_inner * TICK_5DEG_FRAC
                painter.setPen(QPen(QColor(COLOR_TICK_5DEG), 1))
            else:
                tick_inner = g.radius_zodiac_inner * TICK_1DEG_FRAC
                painter.setPen(QPen(QColor(COLOR_TICK_1DEG), 1))
            x1, y1 = _angle_to_xy(g.cx, g.cy, tick_outer, deg, g.rot)
            x2, y2 = _angle_to_xy(g.cx, g.cy, tick_inner, deg, g.rot)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # House ring border
        painter.setPen(QPen(QColor(COLOR_INNER_RING), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_inner, g.radius_inner)

    def _paint_house_band(self, painter: QPainter, g: _Geometry, st: _PaintState):
        cusps = self._house_cusps
        house_outer_rect = QRectF(g.cx - g.radius_house_outer, g.cy - g.radius_house_outer,
                                  2 * g.radius_house_outer, 2 * g.radius_house_outer)
        cosmos_rect      = QRectF(g.cx - g.radius_cosmos, g.cy - g.radius_cosmos,
                                  2 * g.radius_cosmos,      2 * g.radius_cosmos)
        # Filled annular sectors
        for i, cusp_lon in enumerate(cusps):
            next_cusp   = cusps[(i + 1) % 12]
            sector_span = (next_cusp - cusp_lon) % 360
            qt_start    = cusp_lon - 90 - g.rot
            path = QPainterPath()
            path.arcMoveTo(house_outer_rect, qt_start)
            path.arcTo(house_outer_rect, qt_start, sector_span)
            path.arcTo(cosmos_rect, qt_start + sector_span, -sector_span)
            path.closeSubpath()
            painter.setPen(Qt.PenStyle.NoPen)
            painter.fillPath(path, QBrush(QColor(SIGN_COLORS[i])))

        # Cusp divider lines: cosmos → house_outer
        painter.setPen(QPen(QColor(COLOR_RING), 1))
        for cusp_lon in cusps:
            x1, y1 = _angle_to_xy(g.cx, g.cy, g.radius_cosmos,      cusp_lon, g.rot)
            x2, y2 = _angle_to_xy(g.cx, g.cy, g.radius_house_outer,  cusp_lon, g.rot)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

        # House numerals centred in each sector
        num_font = QFont()
        num_font.setPointSize(max(FONT_FLOOR_NORMAL, round(HOUSE_NUM_PT * g.scale)))
        painter.setFont(num_font)
        label_r_band = (g.radius_cosmos + g.radius_house_outer) / 2
        house_w, house_h = HOUSE_LABEL_W * g.scale, HOUSE_LABEL_H * g.scale
        house_halo = HOUSE_HIT_RADIUS * g.scale
        self._house_positions.clear()
        for i, cusp_lon in enumerate(cusps):
            next_cusp   = cusps[(i + 1) % 12]
            sector_span = (next_cusp - cusp_lon) % 360
            mid_lon     = (cusp_lon + sector_span / 2) % 360
            lx, ly = _angle_to_xy(g.cx, g.cy, label_r_band, mid_lon, g.rot)
            self._house_positions[i + 1] = (lx, ly)
            is_house_hov = not st.any_locked and (i + 1) == self._hovered_house
            if is_house_hov:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, 30)))
                painter.drawEllipse(QPointF(lx, ly), house_halo, house_halo)
            num_color = QColor(COLOR_HOUSE_NUMERAL)
            if is_house_hov:
                num_color = num_color.lighter(160)
            painter.setPen(QPen(num_color))
            painter.drawText(QRectF(lx - house_w / 2, ly - house_h / 2, house_w, house_h),
                             Qt.AlignmentFlag.AlignCenter, HOUSE_NUMERALS[i])

        # Outer ring border
        painter.setPen(QPen(QColor(COLOR_INNER_RING), 1))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_house_outer, g.radius_house_outer)

    def _paint_angle_axes(self, painter: QPainter, g: _Geometry, st: _PaintState):
        # Angle axes (length depends on Houses toggle)
        axis_end      = g.radius_house_outer if st.houses_on else g.radius_zodiac_outer
        angle_label_r = ((g.radius_cosmos + g.radius_house_outer) / 2 if st.houses_on
                         else g.radius_zodiac_inner * ANGLE_LABEL_NO_HOUSES_FRAC)
        lbl_font = QFont()
        lbl_font.setPointSize(max(FONT_FLOOR_NORMAL, round(ANGLE_LABEL_PT * g.scale)))
        lbl_font.setBold(True)
        angle_w, angle_h = ANGLE_LABEL_W * g.scale, ANGLE_LABEL_H * g.scale
        for angle_name in ("ASC", "DSC", "MC", "IC"):
            if not st.angles_on:
                continue
            if not self._chart or angle_name not in self._chart.positions:
                continue
            lon    = self._chart.positions[angle_name].longitude
            color  = QColor(ANGLE_COLORS[angle_name])
            is_hov = angle_name == st.eff_hov
            width  = PEN_ANGLE_HOVERED if is_hov else PEN_ANGLE_NORMAL
            if is_hov:
                color = color.lighter(130)
            else:
                color.setAlpha(200)
            painter.setPen(QPen(color, width))
            x1, y1 = _angle_to_xy(g.cx, g.cy, g.radius_hub, lon, g.rot)
            x2, y2 = _angle_to_xy(g.cx, g.cy, axis_end,     lon, g.rot)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

            lx, ly = _angle_to_xy(g.cx, g.cy, angle_label_r, lon, g.rot)
            self._planet_positions[angle_name] = (lx, ly)
            painter.setFont(lbl_font)
            lbl_color = QColor(ANGLE_COLORS[angle_name])
            if is_hov:
                lbl_color = lbl_color.lighter(130)
            painter.setPen(QPen(lbl_color))
            painter.drawText(QRectF(lx - angle_w / 2, ly - angle_h / 2, angle_w, angle_h),
                             Qt.AlignmentFlag.AlignCenter, angle_name)
            if angle_name == self._locked:
                ring_r = (GLYPH_PX / 2 + PLANET_HIT_PAD) * g.scale
                self._draw_lock_badge(painter, lx, ly, ring_r, angle_w * 3, g.scale)

    def _draw_lock_badge(self, painter: QPainter, x: float, y: float,
                         ring_r: float, text_w: float, scale: float):
        """Teal lock ring + 'LOCKED / Click to unlock' caption under a glyph."""
        painter.setPen(QPen(QColor(COLOR_LOCK), LOCK_RING_PEN_W))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(QPointF(x, y), ring_r, ring_r)
        lock_font = QFont()
        lock_font.setPointSize(max(FONT_FLOOR_SMALL, round(LOCK_GLYPH_PT * scale)))
        painter.setFont(lock_font)
        painter.setPen(QPen(QColor(COLOR_LOCK)))
        y_base = y + ring_r + 2 * scale
        painter.drawText(QRectF(x - text_w / 2, y_base, text_w, 14 * scale),
                         Qt.AlignmentFlag.AlignCenter, "LOCKED")
        painter.drawText(QRectF(x - text_w / 2, y_base + 13 * scale, text_w, 12 * scale),
                         Qt.AlignmentFlag.AlignCenter, "Click to unlock")

    def _paint_natal_aspects(self, painter: QPainter, g: _Geometry, st: _PaintState):
        if not (st.show_natal and self._cb_natal_aspects.isChecked() and self._chart and self._aspects):
            return
        arc_step = g.radius_inner * CONJUNCTION_ARC_STEP_FRAC
        for asp in self._aspects:
            lon1 = self._chart.positions[asp.planet1].longitude
            lon2 = self._chart.positions[asp.planet2].longitude
            color = QColor(ASPECT_COLORS.get(asp.aspect, "#888"))
            if not st.angles_on and (asp.planet1 in ANGLE_NAMES or asp.planet2 in ANGLE_NAMES):
                continue
            related = bool(st.eff_hov) and st.eff_hov in (asp.planet1, asp.planet2)
            if st.hov_active:
                color.setAlpha(ALPHA_NATAL_ASP_RELATED if related else ALPHA_NATAL_ASP_DIM)
            else:
                color.setAlpha(ALPHA_NATAL_ASP_ACTIVE)
            width = PEN_ASPECT_ACTIVE if (st.hov_active and related) else PEN_DEFAULT
            painter.setPen(QPen(color, width))

            if asp.aspect == "conjunction":
                # Three concentric arcs curving along the inner ring
                a1, a2 = min(lon1, lon2), max(lon1, lon2)
                if a2 - a1 > 180:
                    a1, a2 = a2, a1 + 360
                start_qt = a1 - 90 - g.rot
                sweep_qt = a2 - a1
                for k in range(CONJUNCTION_ARC_COUNT):
                    r = g.radius_inner + k * arc_step
                    rect = QRectF(g.cx - r, g.cy - r, 2 * r, 2 * r)
                    path = QPainterPath()
                    path.arcMoveTo(rect, start_qt)
                    path.arcTo(rect, start_qt, sweep_qt)
                    painter.drawPath(path)
            else:
                x1, y1 = _angle_to_xy(g.cx, g.cy, g.radius_inner, lon1, g.rot)
                x2, y2 = _angle_to_xy(g.cx, g.cy, g.radius_inner, lon2, g.rot)
                painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

    def _paint_transit_natal_aspects(self, painter: QPainter, g: _Geometry, st: _PaintState):
        show_all_t_asp       = st.show_transits and self._cb_transit_aspects.isChecked()
        show_hover_t_asp     = st.show_transits and bool(st.eff_hov_transit)
        show_angle_t_asp     = st.show_transits and st.angles_on and st.eff_hov in ANGLE_NAMES
        show_natal_hov_t_asp = st.show_transits and st.show_natal and bool(st.eff_hov) and st.eff_hov not in ANGLE_NAMES
        if not ((show_all_t_asp or show_hover_t_asp or show_angle_t_asp or show_natal_hov_t_asp)
                and self._transit_aspects and self._chart):
            return
        dash_pen = QPen()
        dash_pen.setWidth(1)
        dash_pen.setStyle(Qt.PenStyle.DashLine)
        for t in self._transit_aspects.transits:
            if not show_all_t_asp:
                if show_hover_t_asp and t.transit_planet == st.eff_hov_transit:
                    pass
                elif (show_angle_t_asp or show_natal_hov_t_asp) and t.natal_planet == st.eff_hov:
                    pass
                else:
                    continue
            if t.natal_planet not in self._chart.positions:
                continue
            if not st.angles_on and t.natal_planet in ANGLE_NAMES:
                continue
            if not st.show_natal and t.natal_planet not in ANGLE_NAMES:
                continue
            if not self._transits or t.transit_planet not in self._transits.positions:
                continue
            color = QColor(ASPECT_COLORS.get(t.aspect, "#888"))
            related = (
                (bool(st.eff_hov) and t.natal_planet == st.eff_hov)
                or (bool(st.eff_hov_transit) and t.transit_planet == st.eff_hov_transit)
            )
            if st.hov_active:
                color.setAlpha(ALPHA_TRANSIT_ASP_RELATED if related else ALPHA_TRANSIT_ASP_DIM)
            else:
                color.setAlpha(ALPHA_TRANSIT_ASP_ACTIVE)
            dash_pen.setColor(color)
            painter.setPen(dash_pen)
            t_lon = self._transits.positions[t.transit_planet].longitude
            n_lon = self._chart.positions[t.natal_planet].longitude
            tx, ty = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_outer, t_lon, g.rot)
            n_r    = g.radius_cosmos if t.natal_planet in ANGLE_NAMES else g.radius_inner
            nx, ny = _angle_to_xy(g.cx, g.cy, n_r, n_lon, g.rot)
            painter.drawLine(QPointF(tx, ty), QPointF(nx, ny))

    def _paint_sky_aspect_lines(self, painter: QPainter, g: _Geometry, st: _PaintState):
        show_all_sky = st.show_transits and self._cb_sky_aspects.isChecked()
        show_hover_sky = st.show_transits and bool(st.eff_hov_transit)
        if not ((show_all_sky or show_hover_sky) and self._sky_aspects and self._transits):
            return
        dot_pen = QPen()
        dot_pen.setWidth(1)
        dot_pen.setStyle(Qt.PenStyle.DotLine)
        for asp in self._sky_aspects:
            if not show_all_sky and asp.planet1 != st.eff_hov_transit and asp.planet2 != st.eff_hov_transit:
                continue
            if asp.planet1 not in self._transits.positions or asp.planet2 not in self._transits.positions:
                continue
            color = QColor(ASPECT_COLORS.get(asp.aspect, "#888"))
            related = not st.eff_hov_transit or asp.planet1 == st.eff_hov_transit or asp.planet2 == st.eff_hov_transit
            color.setAlpha(ALPHA_TRANSIT_ASP_RELATED if related else ALPHA_TRANSIT_ASP_DIM)
            dot_pen.setColor(color)
            painter.setPen(dot_pen)
            lon1 = self._transits.positions[asp.planet1].longitude
            lon2 = self._transits.positions[asp.planet2].longitude
            x1, y1 = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_outer, lon1, g.rot)
            x2, y2 = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_outer, lon2, g.rot)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))

    def _paint_natal_planets(self, painter: QPainter, g: _Geometry, st: _PaintState):
        natal_zone = g.radius_zodiac_inner - g.radius_inner
        planet_positions_only = {
            name: pos for name, pos in self._chart.positions.items()
            if name not in ANGLE_NAMES
        }
        planet_radii = _assign_radii(
            planet_positions_only,
            g.radius_natal, g.radius_inner, g.radius_zodiac_inner,
            stack_step=natal_zone * STACK_STEP_FRACTION,
        )
        planet_font = QFont()
        planet_font.setPointSize(max(FONT_FLOOR_NORMAL, round(GLYPH_PT * g.scale)))
        painter.setFont(planet_font)
        glyph_px = GLYPH_PX * g.scale
        half = glyph_px / 2

        # Tick lines — full natal zone width (planets only)
        for name, pos in planet_positions_only.items():
            color = QColor(PLANET_COLORS.get(name, "#ffffff"))
            if name == st.eff_hov:
                color = color.lighter(130)
                painter.setPen(QPen(color, PEN_PLANET_HOVERED))
            elif st.spotlight_active and name in st.spotlit_natals:
                color = color.lighter(130)
                painter.setPen(QPen(color, PEN_PLANET_SPOTLIT))
            elif st.spotlight_active:
                color.setAlpha(ALPHA_NATAL_TICK_DIM)
                painter.setPen(QPen(color, PEN_DEFAULT))
            else:
                color.setAlpha(ALPHA_NATAL_TICK_NORMAL)
                painter.setPen(QPen(color, PEN_DEFAULT))
            tx, ty = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_inner, pos.longitude, g.rot)
            gx, gy = _angle_to_xy(g.cx, g.cy, g.radius_inner,   pos.longitude, g.rot)
            painter.drawLine(QPointF(tx, ty), QPointF(gx, gy))

        for name, pos in planet_positions_only.items():
            glyph = PLANET_GLYPHS.get(name, name[:2])
            gx, gy = _angle_to_xy(g.cx, g.cy, planet_radii[name], pos.longitude, g.rot)
            self._planet_positions[name] = (gx, gy)
            color = QColor(PLANET_COLORS.get(name, "#ffffff"))
            is_hovered = name == st.eff_hov
            is_spotlit = st.spotlight_active and name in st.spotlit_natals
            is_dimmed  = st.spotlight_active and not is_spotlit

            pt_base = GLYPH_PT_OVERRIDE.get(name, GLYPH_PT)
            if pt_base != GLYPH_PT:
                f = QFont()
                f.setPointSize(max(FONT_FLOOR_SMALL, round(pt_base * g.scale)))
                painter.setFont(f)
            else:
                painter.setFont(planet_font)

            if is_hovered:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, ALPHA_HOVER_HALO)))
                painter.drawEllipse(QPointF(gx, gy), half + PLANET_HIT_PAD * g.scale, half + PLANET_HIT_PAD * g.scale)

            if is_dimmed:
                color.setAlpha(ALPHA_NATAL_GLYPH_DIM)
            painter.setPen(QPen(QColor("#ffffff") if (is_hovered or is_spotlit) else color))
            painter.drawText(QRectF(gx - half, gy - half, glyph_px, glyph_px),
                             Qt.AlignmentFlag.AlignCenter, glyph)

            if name == self._locked:
                ring_r = half + PLANET_HIT_PAD * g.scale
                self._draw_lock_badge(painter, gx, gy, ring_r, half * 6, g.scale)

    def _paint_transit_planets(self, painter: QPainter, g: _Geometry, st: _PaintState):
        transit_zone = g.radius_cosmos - g.radius_zodiac_outer
        radius_transit_mid = (g.radius_zodiac_outer + g.radius_cosmos) / 2
        transit_radii = _assign_radii(
            self._transits.positions,
            radius_transit_mid, g.radius_zodiac_outer, g.radius_cosmos,
            stack_step=transit_zone * STACK_STEP_FRACTION,
            cluster_threshold=TRANSIT_CLUSTER_DEG,
        )
        transit_font = QFont()
        transit_font.setPointSize(max(FONT_FLOOR_NORMAL, round(TRANSIT_GLYPH_PT * g.scale)))
        painter.setFont(transit_font)
        transit_px = TRANSIT_GLYPH_PX * g.scale
        half_t = transit_px / 2

        # Tick lines across transit zone
        for name, pos in self._transits.positions.items():
            color = QColor(PLANET_COLORS.get(name, "#ffffff"))
            if name == st.eff_hov_transit:
                color = color.lighter(130)
                painter.setPen(QPen(color, PEN_PLANET_HOVERED))
            elif st.spotlight_active and name in st.spotlit_transits:
                color = color.lighter(130)
                painter.setPen(QPen(color, PEN_PLANET_SPOTLIT))
            elif st.spotlight_active:
                color.setAlpha(ALPHA_TRANSIT_TICK_DIM)
                painter.setPen(QPen(color, PEN_DEFAULT))
            else:
                color.setAlpha(ALPHA_TRANSIT_TICK_NORMAL)
                painter.setPen(QPen(color, PEN_DEFAULT))
            tx, ty = _angle_to_xy(g.cx, g.cy, g.radius_cosmos,       pos.longitude, g.rot)
            gx, gy = _angle_to_xy(g.cx, g.cy, g.radius_zodiac_outer, pos.longitude, g.rot)
            painter.drawLine(QPointF(tx, ty), QPointF(gx, gy))

        # Glyphs — normal color base + blue ghost overlay
        self._transit_positions.clear()
        for name, pos in self._transits.positions.items():
            glyph = PLANET_GLYPHS.get(name, name[:2])
            gx, gy = _angle_to_xy(g.cx, g.cy, transit_radii[name], pos.longitude, g.rot)
            self._transit_positions[name] = (gx, gy)
            color = QColor(PLANET_COLORS.get(name, "#ffffff"))
            is_hovered = name == st.eff_hov_transit
            is_spotlit = st.spotlight_active and name in st.spotlit_transits
            is_dimmed  = st.spotlight_active and not is_spotlit

            pt_base = (GLYPH_PT_OVERRIDE[name] * TRANSIT_GLYPH_PT / GLYPH_PT) if name in GLYPH_PT_OVERRIDE else TRANSIT_GLYPH_PT
            f = QFont()
            f.setPointSize(max(FONT_FLOOR_SMALL, round(pt_base * g.scale)))
            painter.setFont(f)

            if is_hovered:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(QColor(255, 255, 255, ALPHA_HOVER_HALO)))
                painter.drawEllipse(QPointF(gx, gy), half_t + PLANET_HIT_PAD * g.scale, half_t + PLANET_HIT_PAD * g.scale)

            # Base layer — normal planet color
            color.setAlpha(ALPHA_TRANSIT_GLYPH_DIM if is_dimmed else ALPHA_TRANSIT_GLYPH_NORMAL)
            painter.setPen(QPen(QColor("#ffffff") if (is_hovered or is_spotlit) else color))
            painter.drawText(QRectF(gx - half_t, gy - half_t, transit_px, transit_px),
                             Qt.AlignmentFlag.AlignCenter, glyph)

            # Ghost layer — blue on top
            ghost_alpha = ALPHA_GHOST_DIM if is_dimmed else ALPHA_GHOST_NORMAL
            painter.setPen(QPen(QColor(*COLOR_TRANSIT_GHOST, ghost_alpha)))
            painter.drawText(QRectF(gx - half_t, gy - half_t, transit_px, transit_px),
                             Qt.AlignmentFlag.AlignCenter, glyph)

            # Retrograde indicator
            if pos.retrograde and name not in ("North Node", "South Node"):
                rx_font = QFont()
                rx_font.setPointSize(max(FONT_FLOOR_SMALL, round(RETROGRADE_PT * g.scale)))
                painter.setFont(rx_font)
                painter.setPen(QPen(QColor(*COLOR_RETROGRADE, ALPHA_RETROGRADE)))
                painter.drawText(QRectF(gx + half_t - 6 * g.scale, gy - half_t - 2 * g.scale,
                                        16 * g.scale, 14 * g.scale),
                                 Qt.AlignmentFlag.AlignLeft, "℞")

            if name == self._locked_transit:
                ring_r_t = half_t + PLANET_HIT_PAD * g.scale
                self._draw_lock_badge(painter, gx, gy, ring_r_t, half_t * 6, g.scale)

    def _paint_hub(self, painter: QPainter, g: _Geometry):
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor(COLOR_RING)))
        painter.drawEllipse(QPointF(g.cx, g.cy), g.radius_hub, g.radius_hub)

    def _paint_circle_labels(self, painter: QPainter, g: _Geometry):
        # Drawn last — on top of everything
        label_font = QFont()
        label_font.setPointSize(max(FONT_FLOOR_SMALL, round(CIRCLE_LABEL_PT * g.scale)))
        painter.setFont(label_font)
        label_angle = CIRCLE_LABEL_ANGLE
        radius_aspects     = (g.radius_hub + g.radius_inner) / 2
        radius_transit_mid = (g.radius_zodiac_outer + g.radius_cosmos) / 2
        radius_zodiac_mid  = (g.radius_zodiac_inner + g.radius_zodiac_outer) / 2
        radius_house_mid   = (g.radius_cosmos + g.radius_house_outer) / 2
        label_w, label_h = CIRCLE_LABEL_W * g.scale, CIRCLE_LABEL_H * g.scale
        for radius, text, offset in [
            (g.radius_hub,        "Earth",           20),
            (radius_aspects,      "Aspects",          8),
            (g.radius_natal,      "Natal Planets",    0),
            (radius_zodiac_mid,   "Zodiac",           0),
            (radius_transit_mid,  "Transit Planets",  0),
            (radius_house_mid,    "Houses",           0),
        ]:
            lx, ly = _angle_to_xy(g.cx, g.cy, radius + offset, label_angle, g.rot)
            rect = QRectF(lx - label_w / 2, ly - label_h / 2, label_w, label_h)
            painter.setPen(QPen(QColor(0, 0, 0, ALPHA_LABEL_SHADOW)))
            for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                painter.drawText(rect.translated(dx, dy), Qt.AlignmentFlag.AlignCenter, text)
            painter.setPen(QPen(QColor(COLOR_CIRCLE_LABEL)))
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)
