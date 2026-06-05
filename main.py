"""Application entry point.

Used both for `python main.py` and as the PyInstaller build entry.
"""
from app.frontend.main import main

if __name__ == "__main__":
    main()
