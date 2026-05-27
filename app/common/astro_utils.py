def house_number(longitude: float, cusps: list[float] | None) -> int | None:
    """Return 1-based house number for a longitude given 12 house cusps, or None."""
    if not cusps or len(cusps) != 12:
        return None
    for i in range(12):
        start = cusps[i]
        end = cusps[(i + 1) % 12]
        if end > start:
            if start <= longitude < end:
                return i + 1
        else:
            if longitude >= start or longitude < end:
                return i + 1
    return 1
