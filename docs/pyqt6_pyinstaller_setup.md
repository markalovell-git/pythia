# PyQt6 and PyInstaller Setup Guide

## Overview

This guide is for setting up PyQt6 for your astrology app and packaging it into a standalone installer using PyInstaller.

## Step 1: Install PyQt6

To use PyQt6 in your application, first install it via pip:

```bash
pip install PyQt6
```

If you want to use the full set of Qt tools including Qt Designer, also install the `PyQt6-Tools` package:

```bash
pip install PyQt6-Tools
```

## Step 2: Create the PyQt6 App

Once PyQt6 is installed, you can start writing your app. Below is a sample `main.py` file that creates a main window:

```python
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Astrology App")
label = QLabel("Welcome to your Astrology App!", window)
label.move(50, 50)
window.resize(500, 300)
window.show()
sys.exit(app.exec())
```

## Step 3: Install PyInstaller

To package your app into a standalone installer, install PyInstaller:

```bash
pip install pyinstaller
```

## Step 4: Package the App with PyInstaller

Run the following command in the directory that contains your PyQt6 app file (`main.py`):

```bash
pyinstaller --onefile main.py
```

This will create a standalone executable in the `dist/` directory. You can run the file on Windows, macOS, and Linux without needing Python installed.

## Step 5: Add Icons and Customization (Optional)

You can set a custom icon by using the `--icon` flag:

```bash
pyinstaller --onefile --icon=app_icon.ico main.py
```

You can also hide the console window in GUI apps by adding the `--windowed` flag:

```bash
pyinstaller --onefile --windowed main.py
```

## Summary

- **PyQt6**: For creating native desktop apps with 2D visuals
- **PyInstaller**: For creating a distributable `.exe`, `.dmg`, or `.AppImage`
- **Output**: A standalone app that runs on Windows, macOS, and Linux

---

This file can be used to build out your PyQt6 app and package it for deployment. It includes sample code and commands to help you get started.

This documentation file can be ingested by any automated system looking to generate documentation or understand the setup process of your app.