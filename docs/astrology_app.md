# Astrology Desktop App Tech Stack Overview

## Overview

This app is a desktop application that:
- Displays your astrological chart (natively on your computer, without web APIs)
- Tracks your transits (approaching and waning)
- Uses Python as the backend, and PyQt6 for the frontend
- Stores data locally, using SQLite, with the ability to move to PostgreSQL later
- Is fully packaged into an installer for use on Windows, macOS, and Linux

## Tech Stack

### Backend (Python)
- **Language**: Python 3.9, 3.10, or newer
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - for backend services if needed, or can be removed for a headless application
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database**: Initially **SQLite**, later **PostgreSQL**

### Frontend (PyQt6)
- **Library**: [PyQt6](https://www.riverbankcomputing.com/software/pyqt6/)
- **UI Design**: Python-based UI, with Qt Designer and PyQt6 tools
- **Graphics**: 2D rendering with `QPainter`, `QGraphicsView`, and `QPixmap`
- **Packaging Tool**: [PyInstaller](https://pyinstaller.org/)

## Development Goals

- **2D Rendering Only**: This app makes full use of 2D graphics, not 3D (unless later upgraded with `QOpenGLWidget`)
- **No Web APIs**: All data, including transits and charts, is computed locally
- **Standalone Installer**: Create a distributable `.exe` (Windows), `.dmg` (macOS), or `.AppImage` (Linux) using PyInstaller

## Next Steps
- Write the PyQt6 code for the application
- Set up SQLAlchemy with SQLite
- Package the app using PyInstaller

---

This file is the first in the project’s documentation set, and can be used by the app or by the codebase to generate further documentation if desired.