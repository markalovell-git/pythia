# TODO

## Chart Points to Add
- [ ] North and South Nodes
- [ ] Ascendant (ASC) and Descendant (DSC)
- [ ] IC (Imum Coeli) and MC (Midheaven)

## Aspect Web
- [ ] **Aspect symbols at line midpoints** — draw the standard aspect glyph (☌ conjunction, ☍ opposition, △ trine, □ square, ⚹ sextile) at the midpoint of each aspect line in the web
- [ ] **Aspect symbols on transit-to-natal lines** — same glyphs at midpoints of the dashed transit aspect lines
- [ ] **Aspect symbol key** — a legend panel or overlay mapping each symbol to its name and meaning

## Animations
- [ ] **Hover glow pulse** on planets/signs — `QTimer` driving a sine-wave alpha value
- [ ] **Hover glow effect** — tried multi-layer bloom (redrawing glyph at larger sizes with decreasing alpha); wasn't striking enough. Needs a different approach — maybe `QGraphicsEffect`, offscreen render + blur, or something else entirely.
- [ ] **Chart load fade-in** — opacity animating from 0 to 1 when chart data arrives
- [ ] **Smooth ring reveal** — rings drawing in sequentially on load
- [ ] **Transit planet entry** — when transits are added, planets arc into position

## Maybe Consider
- [ ] **Aspect line hover tooltips** — mouse-over an aspect line (or conjunction arc) shows a description of that pairing's meaning. Hit detection needs distance-from-segment math (~5-8px tolerance; arcs can be tested radially). Content options: (a) static lookup table of planet-pair themes × aspect type, (b) live Claude API call per hover (richer but laggy), or (c) hybrid — pre-written planet-pair themes templated with aspect language. Validate UX with static table first, then optionally upgrade to live generation.

## Code Quality
- [ ] Pull all magic numbers out of `chart_view.py` into a dedicated constants section or `ChartStyle` dataclass (radius fractions, STACK_STEP_FRACTION, CLUSTER_THRESHOLD_DEG, arc_step, glyph sizes, etc.)
