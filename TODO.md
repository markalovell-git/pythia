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

## Packaging & Distribution
- [x] **Toolchain-free AppImage + self-update** — ships as a single self-contained `Pythia-x86_64.AppImage` (PyInstaller → appimagetool), built and published to GitHub Releases by CI on a `vX.Y.Z` tag push. The in-app updater checks the Releases API, prompts, downloads, and swaps in place. (Retired the earlier git-pull/`install.sh` approach.)
- [ ] **Threaded download with a real progress UI** — the in-app update download (`_maybe_update` in `app/frontend/main.py`) currently runs synchronously on the Qt main thread behind a static "Downloading…" `QSplashScreen`, so the ~150 MB AppImage download **freezes the UI** with no live progress and no cancel until it finishes. Finite `httpx` timeouts (connect 10s / read 30s in `updater.apply_update`) already prevent an indefinite hang, so this is UX polish, not a correctness gap — do it if updates ever feel janky. Plan: move the download into a `QThread` worker (reuse the existing `app/frontend/workers/` pattern), stream bytes, and emit progress signals to a `QProgressDialog` showing %/MB plus a Cancel button. `apply_update` already streams in chunks and knows `written` vs the asset's `expected` size, so it can report progress with minimal change; have it accept a progress callback (or split the download into the worker and keep the verify/swap in `updater`).
- [ ] **Centralize theme colors + fix `APP_AUTHOR`** — the dark-theme hex colors (`#0d0d1a`, `#1a1a2e`, `#16213e`, `#aaaaff`, `#e0e0e0`, `#7070aa`, …) are duplicated as string literals across `app/frontend/main.py` (palette + global stylesheet), `app/frontend/widgets/about_dialog.py`, and several other widgets, so re-theming means hunting them down everywhere. Extract a single source — e.g. `app/frontend/theme.py` with named constants (`BG`, `PANEL`, `ACCENT`, `TEXT`, …) and/or a shared QSS string — and reference it from the palette, stylesheet, and per-widget styles. Cosmetic and broad (touches many widgets), so do it as a dedicated pass. While there: `app/common/paths.py` sets `_APP_AUTHOR == _APP_NAME` (`"Pythia"`); harmless on Linux (platformdirs ignores author there) but would nest `Pythia/Pythia/...` on Windows/macOS if ever shipped — give it a distinct author or drop it.

## Consult Chat
- [ ] **Get qwen2.5 to answer more briefly** — the Consult chat still throws walls of text (qwen3 was worse; qwen2.5:14b is better but still over-long, sometimes with markdown headings/emoji despite the prompt forbidding them). Already in place: firm `CHAT_SYSTEM_PROMPT` (brief, no headings/emoji, English-only), `think=False` for the chat Ollama call, anti-loop sampling (`repeat_penalty`/`temperature`/`top_p`), few-shot priming (`CHAT_FEWSHOT`), and `trim_to_last_sentence()` — all in `app/frontend/services/llm_client.py`. The hard `num_predict` cap was removed (chopped replies mid-thought). Next levers to try: (a) shorten the `CHAT_FEWSHOT` example to ~2 sentences (models anchor hard on its length); (b) a brute-force client-side post-processor that strips markdown/emoji and keeps the first ~3–4 sentences (guaranteed brief but lossy); (c) test other local instruct models (mistral-nemo:12b, gemma2:9b, llama3.1:8b); (d) route chat to Claude/OpenAI (Settings → AI Interpreter) which obeys the brevity prompt reliably. Local instruct models have a real ceiling on honoring style/length constraints.

## Code Quality
- [ ] **Discuss: eager view loading at startup** — `MainWindow` instantiates all 6 views and calls `load()` on each at startup, firing parallel API requests even for views the user hasn't visited. Evaluate lazy-loading (create/load a view on first navigation) to speed up startup and avoid unnecessary requests on slow backends.
