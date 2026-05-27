"""Thin httpx-based client for Claude, OpenAI, and Ollama chat APIs.

Also contains build_consult_payload() which assembles the JSON data
sent to the LLM for natal + transit interpretation.
"""

import json
import re
import httpx

from app.frontend.models.chart_model import (
    ChartData, TransitData, TransitWindowResult,
    compute_natal_aspects, get_house_number, format_transit_dates, TransitWindow,
)
from app.frontend.models.user_model import UserDetail

_TIMEOUT = 600.0  # 10 min — local models on CPU can be slow
_OLLAMA_CTX = 8192  # tokens; 4096 default overflows with large payloads
_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)  # strip qwen3 reasoning blocks

# ── System prompts ─────────────────────────────────────────────────────────────

DAILY_SYSTEM_PROMPT = """You are an astrological interpreter generating a daily transit reading.

INPUT CONTRACT
You will receive a JSON payload with these top-level keys:
- natal: the user's birth chart (planets, houses, aspects, meta)
- transits: an array of currently active transits, pre-ranked by significance (higher rank = more important)
- context: moon phase and other slow-moving context
- request: horizon, tone, and experience level

INTERPRETATION RULES
1. Interpret ONLY the transits provided. Do not infer additional aspects, midpoints, or contacts that are not in the input. If you think something is missing, say so rather than inventing it.
2. Use the provided ranking. Lead with the highest-ranked transits; mention lower-ranked ones briefly or group them.
3. Respect the orb. Transits with orb > 3° are background; orb < 1° and applying are the headline. Separating aspects are waning influence — note this when relevant.
4. Distinguish timescales. Fast transits (Moon, Mercury, Venus, Mars, Sun) are about today's texture. Slow transits (Jupiter through Pluto, nodes) are ongoing chapters that today's fast transits activate. Frame accordingly.
5. Anchor to the natal chart. A transit means little without the natal point it touches. Reference the natal planet's sign, house, and condition when interpreting.
6. Honor the Rodden rating. If birth time is unrated, unknown, or C-rated, hedge any interpretation that depends on houses, angles, or the Moon's exact degree.

OUTPUT STRUCTURE
- Opening (2-3 sentences): the day's overall texture, drawing from the top-ranked transit(s) and lunar context.
- Main movements (1-3 short sections): the headline transits, each with what it activates natally and how it might land experientially.
- Background (1 short paragraph): slower transits providing the larger context this day sits inside.
- Practical note (1-2 sentences): something actionable or worth noticing, not prescriptive advice.

TONE
- Match the requested tone (psychological, traditional, evolutionary, or predictive). Default to psychological if unspecified.
- Adjust vocabulary to the requested experience level. For beginners, define terms inline on first use. For intermediate/advanced, use the craft's language without over-explaining.
- Avoid generic horoscope-speak ("today is a powerful day for transformation"). Be specific to THIS chart and THESE transits.
- No predictions of specific events. Describe energetic conditions and likely themes.

CONSTRAINTS
- Do not output JSON unless explicitly requested; produce readable prose.
- Do not list every transit mechanically. Synthesize.
- If transits contradict each other (e.g., expansive Jupiter contact alongside restrictive Saturn contact), name the tension rather than smoothing it over.
"""

LONGVIEW_SYSTEM_PROMPT = """You are an astrological interpreter generating a long-view reading covering weeks to months.

INPUT CONTRACT
You will receive a JSON payload with these top-level keys:
- natal: the user's birth chart
- transits: active and upcoming transits within the requested horizon, pre-ranked
- windows: transit date windows showing when each transit is active (handles retrograde loops)
- context: moon phase and other contextual data
- request: horizon (week / month / quarter / year), tone, and experience level

INTERPRETATION RULES
1. Prioritize slow transits. Saturn, Uranus, Neptune, Pluto, and the nodes carry the arc. Faster transits are noted only when they activate slow-transit degrees or perfect at meaningful points.
2. Build a timeline, not a list. Identify the sequence: what's perfecting first, what stations bring back, what ingresses change the backdrop. Group related transits into chapters.
3. Use exact dates from the input. Reference station dates, exact-aspect dates, and ingress dates when they shape the narrative. Do not invent dates not in the input.
4. Interpret ONLY what is provided. No inferred aspects, no invented transits, no assumed midpoints. Flag gaps if the input seems thin for the requested horizon.
5. Honor the Rodden rating as in the daily prompt.

OUTPUT STRUCTURE
- Headline arc (1 paragraph): the dominant story across the horizon, named by its key transit(s).
- Chapters (2-4 sections, each titled): time-bounded phases within the horizon, each tied to specific transits and dates. Order chronologically.
- Threads to watch (short paragraph): subplots — secondary transits, upcoming activations that will matter later.
- Natal context (1 paragraph): which parts of the natal chart are most engaged across this horizon, and what that tends to mean for this person.

TONE
- Same conventions as the daily prompt: match requested tone, adjust to experience level, avoid generic horoscope language.
- Long-view reads should feel like narrative, not bullet points. The astrology IS the story structure.
- Acknowledge uncertainty. Slow transits describe pressure and theme, not specific outcomes.

CONSTRAINTS
- Do not output JSON unless explicitly requested.
- Do not predict specific events; describe conditions, choices, and likely themes.
- Name tensions and contradictions in the chart rather than resolving them artificially.
"""

CHAT_SYSTEM_PROMPT = """You are an astrological interpreter engaged in a follow-up conversation about a natal and transit reading.

The user has already received two written interpretations: a daily reading and a longer-term reading. These are provided in the context below. Your role is to answer follow-up questions, go deeper on specific transits or natal placements, and help the user understand the astrology at work.

RULES
- Ground every answer in the chart data provided. Do not invent placements, aspects, or transits not present in the context.
- When the user asks about a planet, sign, or aspect not in the data, say so clearly rather than speculating.
- Adjust depth to the question — a "what does this mean?" question deserves a different depth than "how long will this last?"
- Keep responses focused and conversational. You're in a dialogue, not writing another essay.
- Avoid generic horoscope language. Be specific to THIS chart.
"""

# ── Moon phase helper ──────────────────────────────────────────────────────────

_PHASE_NAMES = [
    (0,   "new moon"),
    (45,  "waxing crescent"),
    (90,  "first quarter"),
    (135, "waxing gibbous"),
    (180, "full moon"),
    (225, "waning gibbous"),
    (270, "last quarter"),
    (315, "waning crescent"),
    (360, "new moon"),
]


def _moon_phase(sun_lon: float, moon_lon: float) -> str:
    angle = (moon_lon - sun_lon) % 360
    for boundary, name in reversed(_PHASE_NAMES):
        if angle >= boundary:
            return name
    return "new moon"


# ── Payload builder ────────────────────────────────────────────────────────────

def build_consult_payload(
    user: UserDetail,
    natal: ChartData,
    transit_data: TransitData,
    windows: list[TransitWindowResult],
    horizon: str,  # "today" | "longer_term"
) -> str:
    cusps = natal.house_cusps or []

    # Natal planets
    natal_planets = []
    for planet, pos in natal.positions.items():
        house = get_house_number(pos.longitude, cusps)
        natal_planets.append({
            "planet":     planet,
            "sign":       pos.sign,
            "degree":     round(pos.degree, 2),
            "retrograde": pos.retrograde,
            "house":      house,
        })

    # Natal aspects
    natal_aspects = [
        {"planet1": a.planet1, "planet2": a.planet2, "aspect": a.aspect, "orb": round(a.orb, 2)}
        for a in compute_natal_aspects(natal)
    ]

    # Active transits — major/notable/minor, sorted by peak_score
    filtered = sorted(
        [t for t in transit_data.transits if t.category in ("major", "notable", "minor")],
        key=lambda t: t.peak_score,
        reverse=True,
    )

    transit_list = []
    for t in filtered:
        transit_house = get_house_number(t.transit_position.longitude, cusps)
        natal_house   = get_house_number(t.natal_position.longitude, cusps)
        entry: dict = {
            "transit_planet":  t.transit_planet,
            "natal_planet":    t.natal_planet,
            "aspect":          t.aspect,
            "orb":             round(t.orb, 2),
            "is_applying":     t.is_applying,
            "days_to_exact":   round(t.days_to_exact, 1) if t.days_to_exact is not None else None,
            "rank":            round(t.peak_score, 3),
            "category":        t.category,
            "timescale":       t.timescale,
            "transit_sign":    t.transit_position.sign,
            "transit_degree":  round(t.transit_position.degree, 2),
            "natal_sign":      t.natal_position.sign,
            "natal_degree":    round(t.natal_position.degree, 2),
            "transit_house":   transit_house,
            "natal_house":     natal_house,
        }
        transit_list.append(entry)

    # Moon phase from transit planet positions — find Sun and Moon
    sun_lon  = next((t.transit_position.longitude for t in transit_data.transits if t.transit_planet == "Sun"),  None)
    moon_lon = next((t.transit_position.longitude for t in transit_data.transits if t.transit_planet == "Moon"), None)
    phase = _moon_phase(sun_lon, moon_lon) if sun_lon is not None and moon_lon is not None else "unknown"

    moon_sign = next((t.transit_position.sign for t in transit_data.transits if t.transit_planet == "Moon"), None)

    payload: dict = {
        "natal": {
            "meta": {
                "name":          user.name,
                "birth_datetime": user.birth_datetime,
                "birth_location": user.birth_location,
                "zodiac_system":  natal.zodiac_system,
                "house_system":   natal.house_system,
            },
            "planets": natal_planets,
            "house_cusps": [round(c, 2) for c in cusps],
            "aspects": natal_aspects,
        },
        "transits": transit_list,
        "context": {
            "moon_phase": phase,
            "moon_sign":  moon_sign,
            "date":       transit_data.date,
        },
        "request": {
            "horizon": horizon,
            "tone":    "psychological",
            "level":   "intermediate",
        },
    }

    if horizon == "longer_term" and windows:
        # Only include slow-planet windows — fast planets add tokens without long-view value
        _slow = {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "North Node", "South Node"}
        window_index: dict[str, list[dict]] = {}
        for w in windows:
            if w.transit_planet not in _slow:
                continue
            key = f"{w.transit_planet} {w.aspect} {w.natal_planet}"
            window_index[key] = [{"start": win.start, "end": win.end} for win in w.windows]
        if window_index:
            payload["windows"] = window_index

    return json.dumps(payload, indent=2)


# ── Streaming API ─────────────────────────────────────────────────────────────

def stream_chat(
    provider: str,
    api_key: str,
    model: str,
    base_url: str,
    system: str,
    messages: list[dict],
):
    """Generator that yields text chunks as they arrive. Strips <think> blocks."""
    if provider == "claude":
        yield from _strip_think(_stream_claude(api_key, system, messages))
    elif provider == "openai":
        yield from _strip_think(_stream_openai(api_key, system, messages))
    else:
        yield from _strip_think(_stream_ollama(base_url, model, system, messages))


def _strip_think(chunks):
    """Pass through chunks, discarding ALL <think>...</think> blocks.

    qwen3 sometimes emits a second think block mid-response when it revises
    its answer — without this, both drafts end up concatenated in the output.
    """
    pending = ""
    in_think = False

    for chunk in chunks:
        pending += chunk
        # Process as many complete think-block boundaries as are in the buffer
        while True:
            if not in_think:
                start = pending.find("<think>")
                if start == -1:
                    yield pending
                    pending = ""
                    break
                if start > 0:
                    yield pending[:start]
                pending = pending[start + 7:]
                in_think = True
            else:
                end = pending.find("</think>")
                if end == -1:
                    break  # keep buffering until we see the closing tag
                pending = pending[end + 8:].lstrip("\n")
                in_think = False

    if pending and not in_think:
        yield pending


def _stream_ollama(base_url: str, model: str, system: str, messages: list[dict]):
    url = base_url.rstrip("/") + "/api/chat"
    try:
        with httpx.stream(
            "POST", url,
            json={
                "model":    model,
                "stream":   True,
                "options":  {"num_ctx": _OLLAMA_CTX},
                "messages": [{"role": "system", "content": system}] + messages,
            },
            timeout=_TIMEOUT,
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    content = data.get("message", {}).get("content", "")
                    if content:
                        yield content
                except json.JSONDecodeError:
                    pass
    except httpx.ConnectError:
        raise RuntimeError(f"Cannot connect to Ollama at {base_url}. Is Ollama running?")
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"Ollama error {e.response.status_code}: {e.response.text}") from e


def _stream_claude(api_key: str, system: str, messages: list[dict]):
    if not api_key:
        raise RuntimeError("No Anthropic API key configured. Add one in Settings → AI Interpreter.")
    try:
        with httpx.stream(
            "POST", "https://api.anthropic.com/v1/messages",
            headers={"x-api-key": api_key, "anthropic-version": "2023-06-01",
                     "content-type": "application/json"},
            json={"model": "claude-opus-4-7", "max_tokens": 2048, "stream": True,
                  "system": system, "messages": messages},
            timeout=_TIMEOUT,
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line.startswith("data: "):
                    try:
                        data = json.loads(line[6:])
                        if data.get("type") == "content_block_delta":
                            text = data["delta"].get("text", "")
                            if text:
                                yield text
                    except json.JSONDecodeError:
                        pass
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("error", {}).get("message", "")
        except Exception:
            detail = ""
        raise RuntimeError(f"Anthropic API error {e.response.status_code}: {detail or '(no detail)'}") from e


def _stream_openai(api_key: str, system: str, messages: list[dict]):
    if not api_key:
        raise RuntimeError("No OpenAI API key configured. Add one in Settings → AI Interpreter.")
    try:
        with httpx.stream(
            "POST", "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={"model": "gpt-4o", "stream": True,
                  "messages": [{"role": "system", "content": system}] + messages},
            timeout=_TIMEOUT,
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line.startswith("data: ") and "[DONE]" not in line:
                    try:
                        data = json.loads(line[6:])
                        text = data["choices"][0]["delta"].get("content", "")
                        if text:
                            yield text
                    except (json.JSONDecodeError, KeyError, IndexError):
                        pass
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("error", {}).get("message", "")
        except Exception:
            detail = ""
        raise RuntimeError(f"OpenAI API error {e.response.status_code}: {detail or '(no detail)'}") from e


# ── Non-streaming API callers (used for chat replies) ─────────────────────────

def send_chat(
    provider: str,
    api_key: str,
    model: str,
    base_url: str,
    system: str,
    messages: list[dict],
) -> str:
    if provider == "claude":
        return _send_claude(api_key, system, messages)
    elif provider == "openai":
        return _send_openai(api_key, system, messages)
    else:
        return _send_ollama(base_url, model, system, messages)


def _send_claude(api_key: str, system: str, messages: list[dict]) -> str:
    if not api_key:
        raise RuntimeError("No Anthropic API key configured. Add one in Settings → AI Interpreter.")
    try:
        r = httpx.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key":         api_key,
                "anthropic-version": "2023-06-01",
                "content-type":      "application/json",
            },
            json={
                "model":      "claude-opus-4-7",
                "max_tokens": 2048,
                "system":     system,
                "messages":   messages,
            },
            timeout=_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()["content"][0]["text"]
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("error", {}).get("message", "")
        except Exception:
            detail = ""
        raise RuntimeError(f"Anthropic API error {e.response.status_code}: {detail or '(no detail)'}") from e
    except Exception as e:
        raise RuntimeError(f"Claude request failed: {e}") from e


def _send_openai(api_key: str, system: str, messages: list[dict]) -> str:
    if not api_key:
        raise RuntimeError("No OpenAI API key configured. Add one in Settings → AI Interpreter.")
    try:
        r = httpx.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type":  "application/json",
            },
            json={
                "model":    "gpt-4o",
                "messages": [{"role": "system", "content": system}] + messages,
            },
            timeout=_TIMEOUT,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        try:
            detail = e.response.json().get("error", {}).get("message", "")
        except Exception:
            detail = ""
        raise RuntimeError(f"OpenAI API error {e.response.status_code}: {detail or '(no detail)'}") from e
    except Exception as e:
        raise RuntimeError(f"OpenAI request failed: {e}") from e


def _send_ollama(base_url: str, model: str, system: str, messages: list[dict]) -> str:
    url = base_url.rstrip("/") + "/api/chat"
    try:
        r = httpx.post(
            url,
            json={
                "model":   model,
                "stream":  False,
                "options": {"num_ctx": _OLLAMA_CTX},
                "messages": [{"role": "system", "content": system}] + messages,
            },
            timeout=_TIMEOUT,
        )
        r.raise_for_status()
        content = r.json()["message"]["content"]
        # Strip qwen3-style reasoning blocks before returning the visible answer
        return _THINK_RE.sub("", content).strip()
    except httpx.ConnectError:
        raise RuntimeError(f"Cannot connect to Ollama at {base_url}. Is Ollama running?")
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"Ollama error {e.response.status_code}: {e.response.text}") from e
    except Exception as e:
        raise RuntimeError(f"Ollama request failed: {e}") from e
