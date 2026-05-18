import math
import pytest
from app.astrology.scoring import score_transit, categorize, get_timescale, DEFAULT_CONFIG


def _score(tp, np, asp, orb, applying=True, speed=None, house=None, ruler=None):
    return score_transit(tp, np, asp, orb, applying, speed, house, ruler, DEFAULT_CONFIG)


# ── score_transit returns a tuple ────────────────────────────────────────────

def test_returns_tuple_for_valid_transit():
    result = _score("Saturn", "Sun", "conjunction", 2.0)
    assert isinstance(result, tuple) and len(result) == 2


def test_peak_score_gte_current_score():
    result = _score("Saturn", "Sun", "conjunction", 4.0)
    assert result is not None
    current, peak = result
    assert peak >= current


def test_at_orb_zero_current_equals_peak():
    result = _score("Saturn", "Sun", "conjunction", 0.0)
    assert result is not None
    current, peak = result
    assert abs(current - peak) < 1e-6


def test_wide_orb_current_less_than_peak():
    result = _score("Saturn", "Sun", "conjunction", 6.0)
    assert result is not None
    current, peak = result
    assert current < peak


# ── filtering ─────────────────────────────────────────────────────────────────

def test_orb_over_max_returns_none():
    # Max orb for conjunction is 8; Saturn is not a fast planet, so full orb applies
    result = _score("Saturn", "Sun", "conjunction", 9.0)
    assert result is None


def test_unknown_aspect_returns_none():
    result = _score("Saturn", "Sun", "quincunx_unknown", 1.0)
    assert result is None


def test_fast_planet_orb_halving():
    # Moon max orb for conjunction = 8, halved to 4 for fast planets
    # At orb 5, Moon conjunction should be filtered out
    result = _score("Moon", "Sun", "conjunction", 5.0)
    assert result is None


def test_fast_planet_within_halved_orb_passes():
    result = _score("Moon", "Sun", "conjunction", 3.0)
    assert result is not None


def test_slow_planet_at_full_max_orb_passes():
    # Saturn conjunction max orb = 8
    result = _score("Saturn", "Sun", "conjunction", 7.9)
    assert result is not None


# ── applying bonus ────────────────────────────────────────────────────────────

def test_applying_scores_higher_than_separating():
    applying    = _score("Saturn", "Sun", "conjunction", 3.0, applying=True)
    separating  = _score("Saturn", "Sun", "conjunction", 3.0, applying=False)
    assert applying is not None and separating is not None
    assert applying[0] > separating[0]


def test_applying_and_separating_same_peak():
    applying   = _score("Saturn", "Sun", "conjunction", 3.0, applying=True)
    separating = _score("Saturn", "Sun", "conjunction", 3.0, applying=False)
    # peak_score includes the applying_bonus (it's part of base_score)
    # applying peak > separating peak because applying_bonus differs
    assert applying is not None and separating is not None
    assert applying[1] > separating[1]


# ── station bonus ─────────────────────────────────────────────────────────────

def test_stationary_outer_planet_gets_bonus():
    normal  = _score("Saturn", "Sun", "conjunction", 2.0, speed=0.034)  # normal speed
    station = _score("Saturn", "Sun", "conjunction", 2.0, speed=0.001)  # near-stationary
    assert station is not None and normal is not None
    assert station[0] > normal[0]


def test_fast_planet_no_station_bonus():
    # Moon has no entry in normal_speeds, so station bonus stays 1.0
    normal   = _score("Moon", "Sun", "conjunction", 1.0, speed=13.0)
    slowmoon = _score("Moon", "Sun", "conjunction", 1.0, speed=0.001)
    assert normal is not None and slowmoon is not None
    assert abs(normal[0] - slowmoon[0]) < 1e-6


# ── chart ruler bonus ─────────────────────────────────────────────────────────

def test_chart_ruler_natal_point_gets_bonus():
    no_ruler   = _score("Saturn", "Mercury", "conjunction", 2.0, ruler=None)
    with_ruler = _score("Saturn", "Mercury", "conjunction", 2.0, ruler="Mercury")
    assert no_ruler is not None and with_ruler is not None
    assert with_ruler[0] > no_ruler[0]


def test_chart_ruler_bonus_capped_at_1():
    # Sun already has n_weight=1.0; +0.2 must cap at 1.0
    no_ruler   = _score("Saturn", "Sun", "conjunction", 2.0, ruler=None)
    with_ruler = _score("Saturn", "Sun", "conjunction", 2.0, ruler="Sun")
    assert no_ruler is not None and with_ruler is not None
    # Both should have n_weight=1.0 (no_ruler is already at max)
    assert abs(no_ruler[0] - with_ruler[0]) < 1e-6


# ── house bonus ───────────────────────────────────────────────────────────────

def test_angular_house_beats_succedent_beats_cadent():
    angular   = _score("Saturn", "Sun", "conjunction", 2.0, house=1)
    succedent = _score("Saturn", "Sun", "conjunction", 2.0, house=2)
    cadent    = _score("Saturn", "Sun", "conjunction", 2.0, house=3)
    assert angular is not None and succedent is not None and cadent is not None
    assert angular[0] > succedent[0] > cadent[0]


@pytest.mark.parametrize("house", [1, 4, 7, 10])
def test_angular_houses_all_same_bonus(house):
    result = _score("Saturn", "Sun", "conjunction", 2.0, house=house)
    ref    = _score("Saturn", "Sun", "conjunction", 2.0, house=1)
    assert result is not None and ref is not None
    assert abs(result[0] - ref[0]) < 1e-9


def test_no_house_defaults_to_neutral():
    no_house  = _score("Saturn", "Sun", "conjunction", 2.0, house=None)
    succedent = _score("Saturn", "Sun", "conjunction", 2.0, house=2)
    assert no_house is not None and succedent is not None
    assert abs(no_house[0] - succedent[0]) < 1e-9


# ── categorize ────────────────────────────────────────────────────────────────

def test_categorize_major():
    assert categorize(0.70, DEFAULT_CONFIG) == "major"
    assert categorize(0.99, DEFAULT_CONFIG) == "major"


def test_categorize_notable():
    assert categorize(0.40, DEFAULT_CONFIG) == "notable"
    assert categorize(0.69, DEFAULT_CONFIG) == "notable"


def test_categorize_minor():
    assert categorize(0.20, DEFAULT_CONFIG) == "minor"
    assert categorize(0.39, DEFAULT_CONFIG) == "minor"


def test_categorize_background():
    assert categorize(0.0,  DEFAULT_CONFIG) == "background"
    assert categorize(0.19, DEFAULT_CONFIG) == "background"


# ── get_timescale ─────────────────────────────────────────────────────────────

@pytest.mark.parametrize("planet", ["Pluto", "Neptune", "Uranus", "Saturn"])
def test_timescale_long(planet):
    assert get_timescale(planet, DEFAULT_CONFIG) == "long"


@pytest.mark.parametrize("planet", ["Jupiter", "Mars"])
def test_timescale_medium(planet):
    assert get_timescale(planet, DEFAULT_CONFIG) == "medium"


@pytest.mark.parametrize("planet", ["Sun", "Mercury", "Venus"])
def test_timescale_short(planet):
    assert get_timescale(planet, DEFAULT_CONFIG) == "short"


def test_timescale_daily():
    assert get_timescale("Moon", DEFAULT_CONFIG) == "daily"


def test_timescale_other():
    assert get_timescale("Chiron", DEFAULT_CONFIG) == "other"


# ── orb_strength cosine falloff ───────────────────────────────────────────────

def test_orb_strength_decreases_with_orb():
    orb0 = _score("Saturn", "Sun", "conjunction", 0.0)
    orb4 = _score("Saturn", "Sun", "conjunction", 4.0)
    orb8 = _score("Saturn", "Sun", "conjunction", 8.0)
    assert orb0 is not None and orb4 is not None and orb8 is not None
    assert orb0[0] > orb4[0] > orb8[0]


def test_orb_strength_at_max_orb_near_zero():
    result = _score("Saturn", "Sun", "conjunction", 8.0)  # max orb = 8
    assert result is not None
    current, peak = result
    # cos(π/2) = 0, so current_score should be ~0
    assert current < 0.01
    # peak_score should still be full base
    assert peak > 0.1
