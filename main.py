"""Application entry point.

Used both for `python main.py` and as the PyInstaller build entry. The
`--selftest` path is dispatched before importing the GUI so it stays free of any
Qt/display dependency.
"""
import sys


def main():
    if "--selftest" in sys.argv:
        from app.selftest import run
        sys.exit(run())
    from app.frontend.main import main as gui_main
    gui_main()


if __name__ == "__main__":
    main()
