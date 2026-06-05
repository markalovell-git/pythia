"""Headless smoke test of the bundled data layer — no Qt, no display.

Run via ``pythia --selftest``. Validates that a packaged build can load the
ephemeris (skyfield + de421.bsp) and resolve a timezone (timezonefinder and its
flatbuffers/h3 data), independent of the GUI. CI uses this as a release gate.
"""
import sys
from datetime import datetime, timezone


def run() -> int:
    try:
        from app.version import get_version
        from app.common import runtime
        from app.astrology.chart import compute_planet_positions

        positions = compute_planet_positions(
            datetime(2000, 1, 1, 12, tzinfo=timezone.utc), "tropical"
        )
        assert "Sun" in positions, "Sun missing from computed positions"

        from timezonefinder import TimezoneFinder
        tz = TimezoneFinder().timezone_at(lat=51.5074, lng=-0.1278)
        assert tz, "timezone lookup returned nothing"

        sign = positions["Sun"]["sign"]
        print(
            f"selftest OK — {get_version()}; Sun in {sign}; tz={tz}; "
            f"self-update={'yes' if runtime.can_self_update() else 'no'}"
        )
        return 0
    except Exception as e:
        print(f"selftest FAILED: {e}", file=sys.stderr)
        return 1
