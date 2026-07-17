"""HTML builders for the chart page's info panel (right sidebar).

Pure presentation: every function takes an InfoContext snapshot of the chart
data plus the name being shown, and returns HTML (or None when there is
nothing to show). ChartView owns the QTextBrowser and the expand/collapse
state; these functions never touch widgets.
"""
from dataclasses import dataclass, field

from app.frontend.models import chart_model
from app.frontend.data.interpretations import (
    natal_aspect_text, planet_in_sign_text, planet_in_house_text,
    transit_in_sign_text, sky_aspect_text, transit_to_natal_text,
)
from app.frontend.widgets.chart_wheel import (
    PLANET_GLYPHS, PLANET_COLORS, ANGLE_NAMES, HOUSE_NUMERALS,
    SIGN_GLYPHS, SIGN_NAMES, ASPECT_COLORS, COLOR_LOCK,
)

TRANSIT_BADGE_COLORS = {
    "major":      "#ffd700",
    "notable":    "#44bb88",
    "minor":      "#7070a0",
    "background": "#444444",
}

COLOR_TRANSIT_TAG = "#5fd6e0"   # "· transit" marker in occupant lists

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

HOUSE_INFO = {
    1:  ("Self · Identity",         "The rising mask. Body, persona, first impressions, the way you arrive in a room."),
    2:  ("Possessions · Values",    "Money, belongings, talents, and what you consider yours. The seat of self-worth."),
    3:  ("Communication · Mind",    "Daily talk, siblings, neighbors, short trips, learning by doing. The mind in motion."),
    4:  ("Home · Roots",            "Family, ancestry, the inner sanctuary. Where you come from and where you retreat."),
    5:  ("Creativity · Romance",    "Play, romance, children, performance. The joy of making something just because you can."),
    6:  ("Work · Routine",          "Daily labor, service, habits, health. The unglamorous shape your days take."),
    7:  ("Partnership · Others",    "One-on-one relationships, marriage, contracts, the people who mirror you back."),
    8:  ("Transformation · Shared", "Sex, death, debt, inheritance, occult depths. What you share and what you surrender."),
    9:  ("Wisdom · Horizons",       "Higher learning, long journeys, foreign cultures, philosophy. The search for meaning."),
    10: ("Career · Reputation",     "Public life, calling, authority, legacy. What the world remembers you for."),
    11: ("Community · Ideals",      "Friends, networks, groups, hopes for the future. The wider tribe."),
    12: ("Unconscious · Surrender", "Solitude, hidden things, dreams, dissolution. Where the self thins out."),
}


@dataclass
class InfoContext:
    """Snapshot of the chart page's data that the HTML builders read from."""
    chart: chart_model.ChartData | None = None
    transits: chart_model.ChartData | None = None            # transit positions
    transit_aspects: chart_model.TransitData | None = None   # scored transit-to-natal aspects
    natal_aspects: list = field(default_factory=list)
    sky_aspects: list = field(default_factory=list)
    transit_windows: dict = field(default_factory=dict)      # (transit, natal, aspect) -> windows
    sky_windows: dict = field(default_factory=dict)          # (p1, p2, aspect) -> windows
    expanded: set = field(default_factory=set)               # expanded section keys
    locked_planet: str = ""
    locked_transit: str = ""


def section_header(expanded: set, key: str, label: str) -> str:
    arrow = "▼" if key in expanded else "▶"
    return (
        f"<p style='margin:8px 0 4px 0;'>"
        f"<a href='toggle:{key}' style='color:#7070a0; text-decoration:none; font-size:13px;'>"
        f"{arrow} {label}</a></p>"
    )


def _interp_html(interp: str) -> str:
    if not interp:
        return ""
    return (
        f"<p style='color:#5a5a7a; font-size:12px; line-height:1.5; margin:0 0 6px 16px;'>"
        f"{interp}</p>"
    )


def _date_span(windows) -> str:
    if not windows:
        return ""
    return (
        f' <span style="color:#667799; font-size:11px;">'
        f'{chart_model.format_transit_dates(windows)}</span>'
    )


def _badge(t) -> str:
    badge_clr = TRANSIT_BADGE_COLORS.get(t.category, "#888")
    return (
        f' <span style="color:{badge_clr}; font-size:10px;">'
        f'[{t.category} · {t.peak_score:.2f}]</span>'
    )


def _exact_tag(t) -> str:
    if t.days_to_exact is None:
        return ""
    if t.days_to_exact > 0:
        return f' <span style="color:#556677; font-size:10px;">exact in {t.days_to_exact:.0f}d</span>'
    return f' <span style="color:#556677; font-size:10px;">exact {abs(t.days_to_exact):.0f}d ago</span>'


def _lock_badge() -> str:
    return f"<p style='color:{COLOR_LOCK}; font-size:11px; margin:0 0 8px 0;'>🔒 Locked · click to unlock</p>"


def planet_info_html(ctx: InfoContext, name: str) -> str | None:
    """Info panel HTML for a natal planet or angle; None when there is nothing to show."""
    if not name or not ctx.chart or name not in ctx.chart.positions:
        return None
    pos = ctx.chart.positions[name]
    glyph = PLANET_GLYPHS.get(name, name)
    color = PLANET_COLORS.get(name, "#ffffff")
    ruling, description = PLANET_INFO.get(name, ("", ""))
    is_angle = name in ANGLE_NAMES

    # ── Header meta ─────────────────────────────────────────────────────
    degree_line = f"{pos.sign} {pos.degree:.2f}°"
    house_num: int | None = None
    if ctx.chart.house_cusps:
        house_num = chart_model.get_house_number(pos.longitude, ctx.chart.house_cusps)
        if house_num:
            degree_line += f" &nbsp;·&nbsp; House {HOUSE_NUMERALS[house_num - 1]}"
    if ruling:
        degree_line += f" &nbsp;·&nbsp; rules {ruling}"

    lock_badge = _lock_badge() if name == ctx.locked_planet else ""
    retrograde_tag = "" if is_angle or not pos.retrograde or name in ("North Node", "South Node") else \
        "<p style='color:#cc3333; margin:0 0 4px 0; font-size:11px; letter-spacing:1px;'>℞ RETROGRADE</p>"
    category_tag = (
        "<p style='color:#886633; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;'>NATAL ANGLE</p>"
        if is_angle else
        "<p style='color:#445588; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;'>NATAL PLANET</p>"
    )

    # ── Placement section ────────────────────────────────────────────────
    placement_content = ""
    if "placement" in ctx.expanded:
        sign_interp = planet_in_sign_text(name, pos.sign)
        if sign_interp:
            placement_content += (
                f"<p style='font-size:12px; margin:2px 0 2px 12px;'>"
                f"<i>in {pos.sign}:</i></p>"
                f"<p style='color:#5a5a7a; font-size:12px; line-height:1.5; margin:0 0 6px 12px;'>"
                f"{sign_interp}</p>"
            )
        if house_num and not is_angle:
            house_interp = planet_in_house_text(name, house_num)
            if house_interp:
                placement_content += (
                    f"<p style='font-size:12px; margin:2px 0 2px 12px;'>"
                    f"<i>in House {HOUSE_NUMERALS[house_num - 1]}:</i></p>"
                    f"<p style='color:#5a5a7a; font-size:12px; line-height:1.5; margin:0 0 4px 12px;'>"
                    f"{house_interp}</p>"
                )

    # ── Natal aspects section ────────────────────────────────────────────
    my_aspects = [a for a in ctx.natal_aspects if a.planet1 == name or a.planet2 == name]

    aspects_content = ""
    if "natal_aspects" in ctx.expanded:
        for a in my_aspects:
            other = a.planet2 if a.planet1 == name else a.planet1
            asp_color = ASPECT_COLORS.get(a.aspect, "#888")
            aspects_content += (
                f"<p style='font-size:13px; line-height:1.8; margin:0 0 0 12px;'>"
                f'<span style="color:{asp_color}">■</span> '
                f'{a.aspect.title()} {other} '
                f'<span style="color:#555">(orb {a.orb:.1f}°)</span></p>'
                f"{_interp_html(natal_aspect_text(name, other, a.aspect))}"
            )

    # ── Active transits section ──────────────────────────────────────────
    active_transit_items = []
    if ctx.transit_aspects:
        for t in ctx.transit_aspects.transits:
            if t.natal_planet != name:
                continue
            asp_color = ASPECT_COLORS.get(t.aspect, "#888")
            ws = ctx.transit_windows.get((t.transit_planet, name, t.aspect), [])
            active_transit_items.append(
                f"<p style='font-size:13px; line-height:1.8; margin:0;'>"
                f'<span style="color:{asp_color}">■</span> '
                f'Transit {t.transit_planet} {t.aspect.title()} '
                f'<span style="color:#555">(orb {t.orb:.1f}°)</span>'
                f'{_date_span(ws)}{_badge(t)}{_exact_tag(t)}</p>'
                + _interp_html(transit_to_natal_text(t.transit_planet, name, t.aspect))
            )

    active_transit_section = ""
    if active_transit_items:
        active_transit_section = section_header(
            ctx.expanded, "active_transits", f"Active Transits ({len(active_transit_items)})"
        )
        if "active_transits" in ctx.expanded:
            active_transit_section += "".join(active_transit_items)

    placement_block = ""
    if not is_angle:
        placement_block = section_header(ctx.expanded, "placement", "Placement") + placement_content

    return (
        f"{lock_badge}"
        f"<p style='font-size:24px; color:{color}; margin:0 0 4px 0;'>{glyph} {name}</p>"
        f"<p style='color:#7070a0; margin:0 0 4px 0; font-size:13px;'>{degree_line}</p>"
        f"{retrograde_tag}{category_tag}"
        f"<p style='color:#a0a0c0; margin:0 0 12px 0; font-size:14px; line-height:1.6;'>{description}</p>"
        f"{placement_block}"
        f"{section_header(ctx.expanded, 'natal_aspects', f'Natal Aspects ({len(my_aspects)})')}"
        f"{aspects_content}"
        f"{active_transit_section}"
    )


def transit_info_html(ctx: InfoContext, name: str) -> str | None:
    """Info panel HTML for a transit planet; None when there is nothing to show."""
    if not name or not ctx.transits or name not in ctx.transits.positions:
        return None
    pos = ctx.transits.positions[name]
    glyph = PLANET_GLYPHS.get(name, name)
    color = PLANET_COLORS.get(name, "#ffffff")
    _, description = PLANET_INFO.get(name, ("", ""))

    house_str = ""
    h = None
    if ctx.chart and ctx.chart.house_cusps:
        h = chart_model.get_house_number(pos.longitude, ctx.chart.house_cusps)
        if h:
            house_str = f" &nbsp;·&nbsp; House {HOUSE_NUMERALS[h - 1]}"

    placement_content = ""
    sign_blurb = transit_in_sign_text(name, pos.sign)
    placement_content += (
        f"<p style='font-size:12px; margin:2px 0 2px 12px;'>"
        f"<i>in {pos.sign}:</i></p>"
    )
    if sign_blurb:
        placement_content += (
            f"<p style='color:#5a5a7a; font-size:12px; line-height:1.5; margin:0 0 6px 12px;'>"
            f"{sign_blurb}</p>"
        )
    if h:
        placement_content += (
            f"<p style='font-size:12px; margin:2px 0 8px 12px;'>"
            f"<i>in House {HOUSE_NUMERALS[h - 1]}:</i></p>"
        )

    transit_items = []
    if ctx.transit_aspects:
        for t in ctx.transit_aspects.transits:
            if t.transit_planet != name:
                continue
            asp_color = ASPECT_COLORS.get(t.aspect, "#888")
            ws = ctx.transit_windows.get((name, t.natal_planet, t.aspect), [])
            transit_items.append(
                f"<p style='font-size:13px; line-height:1.8; margin:0;'>"
                f'<span style="color:{asp_color}">■</span> '
                f'{t.aspect.title()} natal {t.natal_planet} '
                f'<span style="color:#555">(orb {t.orb:.1f}°)</span>'
                f'{_date_span(ws)}{_badge(t)}{_exact_tag(t)}</p>'
                + _interp_html(transit_to_natal_text(name, t.natal_planet, t.aspect))
            )

    sky_items = []
    for asp in ctx.sky_aspects:
        if asp.planet1 == name:
            other = asp.planet2
        elif asp.planet2 == name:
            other = asp.planet1
        else:
            continue
        asp_color = ASPECT_COLORS.get(asp.aspect, "#888")
        ws = ctx.sky_windows.get((asp.planet1, asp.planet2, asp.aspect), [])
        sky_items.append(
            f"<p style='font-size:13px; line-height:1.8; margin:0;'>"
            f'<span style="color:{asp_color}">·</span> '
            f'{asp.aspect.title()} transit {other} '
            f'<span style="color:#555">(orb {asp.orb:.1f}°)</span>'
            f'{_date_span(ws)}</p>'
            + _interp_html(sky_aspect_text(name, other, asp.aspect))
        )

    lock_badge = _lock_badge() if name == ctx.locked_transit else ""

    placement_section = section_header(ctx.expanded, "placement", "Placement")
    if "placement" in ctx.expanded:
        placement_section += placement_content

    transit_section = ""
    if transit_items:
        transit_section = section_header(ctx.expanded, "active_transits", f"Active Transits ({len(transit_items)})")
        if "active_transits" in ctx.expanded:
            transit_section += "".join(transit_items)

    sky_section = ""
    if sky_items:
        sky_section = section_header(ctx.expanded, "sky_aspects", f"Sky Aspects ({len(sky_items)})")
        if "sky_aspects" in ctx.expanded:
            sky_section += "".join(sky_items)

    return (
        f"{lock_badge}"
        f"<p style='font-size:24px; color:{color}; margin:0 0 4px 0;'>{glyph} <b>{name}</b></p>"
        f"<p style='color:#7070a0; margin:0 0 4px 0; font-size:13px;'>{pos.sign} {pos.degree:.2f}°{house_str}</p>"
        + (f"<p style='color:#cc3333; margin:0 0 4px 0; font-size:11px; letter-spacing:1px;'>℞ RETROGRADE</p>" if pos.retrograde and name not in ("North Node", "South Node") else "")
        + f"<p style='color:#4466aa; margin:0 0 10px 0; font-size:11px; letter-spacing:1px;'>TRANSIT PLANET</p>"
        f"<p style='color:#a0a0c0; margin:0 0 8px 0; font-size:14px; line-height:1.6;'>{description}</p>"
        f"{placement_section}"
        f"{transit_section}"
        f"{sky_section}"
    )


def house_info_html(ctx: InfoContext, hnum: int) -> str | None:
    if not hnum:
        return None
    numeral = HOUSE_NUMERALS[hnum - 1]
    subtitle, description = HOUSE_INFO.get(hnum, ("", ""))
    cusps = ctx.chart.house_cusps if ctx.chart else None

    def in_house(_name, pos, _is_transit):
        if not cusps:
            return False
        return chart_model.get_house_number(pos.longitude, cusps) == hnum

    occupants = _occupants_html(ctx, in_house)
    return f"""
    <p style="font-size:24px; color:#9090cc; margin:0 0 4px 0;"><b>House {numeral}</b></p>
    <p style="color:#7070a0; margin:0 0 10px 0; font-size:13px;">{subtitle}</p>
    <p style="color:#a0a0c0; margin:0 0 14px 0; font-size:14px; line-height:1.6;">
        {description}
    </p>
    {occupants}
    """


def sign_info_html(ctx: InfoContext, name: str) -> str | None:
    if not name:
        return None
    glyph = SIGN_GLYPHS[SIGN_NAMES.index(name)]
    element, description = SIGN_INFO.get(name, ("", ""))

    def in_sign(_name, pos, _is_transit):
        return pos.sign == name

    occupants = _occupants_html(
        ctx, in_sign,
        interp_fn=lambda pname, _pos: planet_in_sign_text(pname, name),
    )
    return f"""
    <p style="font-size:24px; color:#9090cc; margin:0 0 4px 0;">{glyph} <b>{name}</b></p>
    <p style="color:#7070a0; margin:0 0 10px 0; font-size:13px;">{element}</p>
    <p style="color:#a0a0c0; margin:0 0 14px 0; font-size:14px; line-height:1.6;">
        {description}
    </p>
    {occupants}
    """


def _occupants_html(ctx: InfoContext, predicate, interp_fn=None) -> str:
    rows = []
    if ctx.chart:
        for name, pos in ctx.chart.positions.items():
            if name in ANGLE_NAMES:
                continue
            if predicate(name, pos, False):
                rows.append((name, pos, False))
    if ctx.transits:
        for name, pos in ctx.transits.positions.items():
            if name in ANGLE_NAMES:
                continue
            if predicate(name, pos, True):
                rows.append((name, pos, True))
    if not rows:
        return ""
    blocks = ""
    for name, pos, is_transit in rows:
        glyph = PLANET_GLYPHS.get(name, name[:2])
        color = PLANET_COLORS.get(name, "#ffffff")
        tag = f" <span style='color:{COLOR_TRANSIT_TAG}; font-weight:600;'>· transit</span>" if is_transit else ""
        blocks += (
            f"<p style='font-size:13px; line-height:1.8; margin:0;'>"
            f'<span style="color:{color}; font-size:18px;">{glyph}</span> '
            f'{name} '
            f'<span style="color:#555">{pos.sign} {pos.degree:.1f}°</span>{tag}</p>'
        )
        if interp_fn and not is_transit:
            interp = interp_fn(name, pos)
            if interp:
                blocks += (
                    f"<p style='color:#5a5a7a; font-size:12px; line-height:1.5;"
                    f" margin:0 0 8px 12px;'>{interp}</p>"
                )
    return (
        "<p style='color:#666; font-size:13px; margin:8px 0 4px 0;'>Occupants:</p>"
        + blocks
    )
