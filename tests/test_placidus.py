"""Unit tests for the Placidus house system algorithm and dispatching."""
import math
import pytest
from datetime import datetime, timezone

from app.astrology.chart import (
    compute_natal_chart,
    compute_placidus_cusps,
)


# London 1990-01-01 12:00 UTC — within ephemeris range (1900-2053). Mid-latitude winter chart
# that exercises non-trivial Placidus skew. Manually verified: ASC=Aries 25°, MC=Capricorn 10°.
REF_DT = datetime(1990, 1, 1, 12, 0, tzinfo=timezone.utc)
REF_TZ = "Europe/London"
REF_LAT, REF_LON = 51.5074, -0.1278


def _angle_close(a: float, b: float, tol: float = 0.01) -> bool:
    d = (a - b) % 360
    return min(d, 360 - d) < tol


# ── Placidus happy path ────────────────────────────────────────────────

def test_placidus_anchor_cusps_match_angles():
    """Cusps 1, 4, 7, 10 must equal ASC, IC, DSC, MC for any Placidus chart."""
    positions, cusps = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "placidus",
    )
    assert _angle_close(cusps[0], positions["ASC"]["longitude"])
    assert _angle_close(cusps[3], positions["IC"]["longitude"])
    assert _angle_close(cusps[6], positions["DSC"]["longitude"])
    assert _angle_close(cusps[9], positions["MC"]["longitude"])


def test_placidus_opposite_cusps_are_180_apart():
    positions, cusps = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "placidus",
    )
    for i in range(6):
        assert _angle_close((cusps[i] + 180) % 360, cusps[i + 6])


def test_placidus_cusps_ordered_ccw():
    """Successive cusps (going CCW) must each be at positive angular distance from the previous."""
    positions, cusps = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "placidus",
    )
    total = 0.0
    for i in range(12):
        gap = (cusps[(i + 1) % 12] - cusps[i]) % 360
        assert 0 < gap < 180, f"cusp {i+1}→{i+2} gap = {gap:.2f}° (must be in (0, 180))"
        total += gap
    assert abs(total - 360) < 0.01


# ── Edge cases ─────────────────────────────────────────────────────────

def test_placidus_at_equator_matches_ra_division():
    """At the equator, Placidus puts each intermediate cusp at RAMC + n×30° (in RA)."""
    # 2000-03-20 12:00 UTC is close to vernal equinox; equator + zero longitude
    positions, cusps = compute_natal_chart(
        datetime(2000, 3, 20, 12, 0, tzinfo=timezone.utc),
        "UTC", "tropical", 0.0, 0.0, "placidus",
    )
    # Houses 11 and 12 should be CCW of MC, roughly 30° and 60° in RA (not equal in longitude)
    mc = positions["MC"]["longitude"]
    # Cusp 11 should be ~30° away from MC in RA, which is ~30/cos(ε) ≈ 32° in longitude
    gap_11 = (cusps[10] - mc) % 360
    gap_12 = (cusps[11] - mc) % 360
    assert 29 < gap_11 < 34, f"cusp 11 ~{gap_11:.2f}° from MC (expected ~32°)"
    assert 58 < gap_12 < 64, f"cusp 12 ~{gap_12:.2f}° from MC (expected ~62°)"


def test_placidus_southern_hemisphere():
    """Sydney birth — opposite hemisphere should still produce a valid 12-cusp chart."""
    positions, cusps = compute_natal_chart(
        datetime(1990, 6, 15, 0, 0, tzinfo=timezone.utc),
        "Australia/Sydney", "tropical", -33.86, 151.21, "placidus",
    )
    assert len(cusps) == 12
    # Anchor cusps still match
    assert _angle_close(cusps[0], positions["ASC"]["longitude"])
    assert _angle_close(cusps[9], positions["MC"]["longitude"])
    # Houses sum to 360
    total = sum((cusps[(i + 1) % 12] - cusps[i]) % 360 for i in range(12))
    assert abs(total - 360) < 0.01


def test_placidus_polar_latitude_raises():
    """At |lat| > ~66.5°, Placidus is undefined and must raise ValueError."""
    with pytest.raises(ValueError, match="Placidus"):
        compute_natal_chart(
            datetime(1990, 1, 1, 12, 0, tzinfo=timezone.utc),
            "UTC", "tropical", 80.0, 0.0, "placidus",
        )


def test_placidus_sidereal_offsets_all_cusps_by_ayanamsa():
    """Sidereal Placidus cusps = tropical cusps - ayanamsa (all cusps shifted uniformly)."""
    _, cusps_trop = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "placidus",
    )
    _, cusps_sid = compute_natal_chart(
        REF_DT, REF_TZ, "sidereal",
        REF_LAT, REF_LON, "placidus",
    )
    diffs = [(cusps_trop[i] - cusps_sid[i]) % 360 for i in range(12)]
    # All diffs should be (approximately) the same value — the ayanamsa
    for d in diffs[1:]:
        assert abs(d - diffs[0]) < 0.001
    # Lahiri at 1990: J2000 (23.85°) - 10yr × 0.014°/yr ≈ 23.71°
    assert 23.5 < diffs[0] < 23.9


# ── Dispatch tests ─────────────────────────────────────────────────────

def test_whole_sign_dispatch_produces_30deg_cusps():
    _, cusps = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "whole_sign",
    )
    for c in cusps:
        assert abs(c % 30) < 1e-6, f"Whole Sign cusp not on sign boundary: {c}"


def test_placidus_and_whole_sign_have_same_anchors_but_different_intermediates():
    positions, placidus = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "placidus",
    )
    _, whole_sign = compute_natal_chart(
        REF_DT, REF_TZ, "tropical",
        REF_LAT, REF_LON, "whole_sign",
    )
    # Whole Sign anchors at ASC's sign boundary, Placidus at the exact ASC degree
    asc = positions["ASC"]["longitude"]
    assert _angle_close(placidus[0], asc)
    assert _angle_close(whole_sign[0], asc - asc % 30)
    # Intermediate cusps differ
    assert not _angle_close(placidus[1], whole_sign[1])


# ── Direct unit test of the algorithm ──────────────────────────────────

def test_compute_placidus_cusps_returns_twelve_values():
    cusps = compute_placidus_cusps(
        ramc_deg=280.75, lat_deg=51.5, obliquity_deg=23.44,
        asc_trop=24.94, mc_trop=279.88, ayanamsa=0.0,
    )
    assert len(cusps) == 12
    assert all(0 <= c < 360 for c in cusps)
