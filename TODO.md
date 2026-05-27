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
- [ ] **Constellation overlay on outer ring** — add a toggleable layer that draws the real zodiac constellations around the wheel. Source options:
    - **HYG v3 database** (public domain CSV, ~120k stars with RA/Dec/magnitude/constellation ID). Filter to mag ≤ 5 within the 12 zodiac constellations, convert J2000 RA/Dec → ecliptic longitude/latitude via Skyfield, render stars sized by magnitude. Connect stick figures using Stellarium's `constellationship.fab` (CC-licensed line pairs by HIP number).
    - **Decorative engravings** — Hevelius's *Uranographia* (1690) or Bode's *Uranographia* (1801), both public domain on Wikimedia Commons. Drop one image per sign at the 15° midpoint; purely ornamental, no real positions.
    - **Stellarium constellation art** — CC BY-SA 4.0 modern artwork from their `skycultures/` directory.
    - **NASA Tycho all-sky mosaic** — public domain but equirectangular projection, would need crop+warp to a ring.
    Tradeoffs for HYG approach: constellations span ~30° of ecliptic latitude, so you need a radial band (lat → radius) rather than a single ring, or accept squashed shapes. Also: in tropical mode the real constellation Aries sits ~24° into Pisces sign (precession). Treat the ring as an astronomical reference layer, not aligned to the labeled signs. Probably most natural as the most decorative option (Hevelius engravings per sign) unless we want the astronomy lesson.

## Time & Info Controls
- [ ] **Natal info readout** — show name, birthplace, birthdate/time, lat/lon, and timezone somewhere visible (header bar above the chart or sidebar panel).
- [ ] **Current transits list** — sorted list of active transit-to-natal aspects with orbs. The existing table shows transit *positions*; this should surface the actual aspects.
- [ ] **Current date display** — prominently show the date the displayed transits are computed for (defaults to "now" but changes when scrubbing time).
- [ ] **Play forward / play backward** — buttons that step transits through time (e.g. 1 day per tick, configurable rate). Re-fetches transits at the new date and animates positions.
- [ ] **Custom date input** — a date/time picker or text box to jump transits to any date.

## Code Quality
- [ ] Pull all magic numbers out of `chart_view.py` into a dedicated constants section or `ChartStyle` dataclass (radius fractions, STACK_STEP_FRACTION, CLUSTER_THRESHOLD_DEG, arc_step, glyph sizes, etc.)
- [ ] **Catch Placidus polar-latitude error at signup** — currently the user only finds out their birth latitude is incompatible with Placidus when the chart calculation fails (HTTP 422). Validate the latitude in the signup/user-edit flow and warn up front, offering to switch to Whole Sign automatically.
- [ ] **Discuss: eager view loading at startup** — `MainWindow` instantiates all 6 views and calls `load()` on each at startup, firing parallel API requests even for views the user hasn't visited. Evaluate lazy-loading (create/load a view on first navigation) to speed up startup and avoid unnecessary requests on slow backends.
- [ ] **Audit sensitive data in error messages** — API streaming errors in `llm_client.py` were echoing raw response bodies (now fixed). Audit all remaining `except` blocks across the codebase that construct user-visible or logged error strings from external responses, to confirm no credentials or PII leak through.
