import logging

# ── Logging ───────────────────────────────────────────────────────────────────
LOG_LEVEL = logging.DEBUG       # logging.INFO or logging.WARNING for quieter output

# ── Backend server ────────────────────────────────────────────────────────────
BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8000
BACKEND_STARTUP_TIMEOUT = 10.0  # seconds to wait for uvicorn on launch
