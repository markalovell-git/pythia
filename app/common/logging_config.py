import logging
import sys

from app.common.config import LOG_LEVEL


def setup_logging(level: int = LOG_LEVEL):
    fmt = "%(asctime)s %(levelname)-8s %(name)-35s %(message)s"
    datefmt = "%H:%M:%S"

    handlers = [
        logging.StreamHandler(sys.stderr),
        logging.FileHandler("pythia.log", mode="w", encoding="utf-8"),
    ]

    logging.basicConfig(level=level, format=fmt, datefmt=datefmt, handlers=handlers)

    # Quiet noisy third-party libs
    for noisy in ("httpx", "httpcore", "uvicorn", "uvicorn.access", "fastapi"):
        logging.getLogger(noisy).setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
