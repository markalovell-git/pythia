VALID_ZODIAC_SYSTEMS = {"sidereal", "tropical"}
DEFAULT_ZODIAC_SYSTEM = "sidereal"

VALID_HOUSE_SYSTEMS = {"placidus", "whole_sign"}
DEFAULT_HOUSE_SYSTEM = "placidus"

# Placidus is undefined above ~66.5° latitude (Arctic/Antarctic circles)
PLACIDUS_MAX_LATITUDE = 66.5

# Diary categories: (slug, display name). Slugs are the storage form, joined
# as a pipe-delimited string ("|a|b|") matching the legacy diary.xml format.
DIARY_CATEGORIES: list[tuple[str, str]] = [
    ("spiritual_quest_and_experiences", "Spiritual Quest and experiences"),
    ("doing_in_the_world",              "Doing in the World"),
    ("studies_and_arts",                "Studies and Arts"),
    ("friends_and_relationships",       "Friends and Relationships"),
    ("outing",                          "Outing"),
    ("landmark",                        "Landmark"),
    ("health_and_physical_body",        "Health and Physical Body"),
    ("family",                          "Family"),
    ("adversity_and_windfalls",         "Adversity and Windfalls"),
    ("world",                           "World"),
    ("unsorted",                        "Unsorted"),
]

_CATEGORY_DISPLAY = dict(DIARY_CATEGORIES)


def category_display(slug: str) -> str:
    """Display name for a category slug; unknown slugs (e.g. legacy 'travel')
    fall back to a title-cased version."""
    return _CATEGORY_DISPLAY.get(slug, slug.replace("_", " ").title())


# AI provider defaults — used as DB column defaults and frontend fallbacks
DEFAULT_ANTHROPIC_MODEL = "claude-opus-4-8"
DEFAULT_OPENAI_MODEL    = "gpt-4o"
DEFAULT_OLLAMA_MODEL    = "qwen3:14b"
DEFAULT_OLLAMA_URL      = "http://localhost:11434"
