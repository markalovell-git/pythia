VALID_ZODIAC_SYSTEMS = {"sidereal", "tropical"}
DEFAULT_ZODIAC_SYSTEM = "sidereal"

VALID_HOUSE_SYSTEMS = {"placidus", "whole_sign"}
DEFAULT_HOUSE_SYSTEM = "placidus"

# Placidus is undefined above ~66.5° latitude (Arctic/Antarctic circles)
PLACIDUS_MAX_LATITUDE = 66.5

# AI provider defaults — used as DB column defaults and frontend fallbacks
DEFAULT_ANTHROPIC_MODEL = "claude-opus-4-8"
DEFAULT_OPENAI_MODEL    = "gpt-4o"
DEFAULT_OLLAMA_MODEL    = "qwen3:14b"
DEFAULT_OLLAMA_URL      = "http://localhost:11434"
