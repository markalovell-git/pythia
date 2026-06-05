"""Canonical application entry point.

Used by both the `pythia` console script and the PyInstaller build (via the root
`main.py`), so they cannot diverge. The `--selftest` path is dispatched before
importing the GUI, keeping it free of any Qt/display dependency.
"""
import sys


def main():
    if "--selftest" in sys.argv:
        from app.selftest import run
        sys.exit(run())
    from app.frontend.main import main as gui_main
    gui_main()
