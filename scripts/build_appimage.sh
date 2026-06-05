#!/usr/bin/env bash
#
# Build Pythia as a self-contained Linux AppImage.
#
#   bash scripts/build_appimage.sh
#
# Output: Pythia-x86_64.AppImage in the repo root. Requires uv. Downloads
# appimagetool on first run. No FUSE needed (appimagetool is extracted).
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ARCH="x86_64"
APPDIR="$ROOT/AppDir"
OUTPUT="$ROOT/Pythia-${ARCH}.AppImage"
APPIMAGETOOL="$ROOT/appimagetool-${ARCH}.AppImage"
APPIMAGETOOL_URL="https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-${ARCH}.AppImage"

echo "==> Ensuring dependencies (uv sync)"
uv sync

# The ephemeris is gitignored, so a fresh checkout (e.g. CI) won't have it.
# Skyfield downloads it (~17 MB) into data/ where the spec expects to bundle it.
echo "==> Ensuring ephemeris (data/de421.bsp)"
if [ ! -f data/de421.bsp ]; then
  uv run python -c "from skyfield.api import Loader; Loader('data')('de421.bsp')"
fi

echo "==> Running PyInstaller"
rm -rf build dist        # clean previous freeze output
uv run pyinstaller --noconfirm packaging/pythia.spec

echo "==> Assembling AppDir"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr/bin"
cp -a dist/pythia/. "$APPDIR/usr/bin/"

# Desktop entry (Exec=pythia runs the bundled binary by name).
cp packaging/pythia.desktop "$APPDIR/pythia.desktop"

# Icon (top-level, matching Icon=pythia) + .DirIcon.
cp packaging/pythia.svg "$APPDIR/pythia.svg"
cp packaging/pythia.svg "$APPDIR/.DirIcon"

# AppRun launches the frozen executable.
cat > "$APPDIR/AppRun" <<'EOF'
#!/bin/sh
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/pythia" "$@"
EOF
chmod +x "$APPDIR/AppRun"

echo "==> Fetching appimagetool"
if [ ! -x "$APPIMAGETOOL" ]; then
  curl -fL -o "$APPIMAGETOOL" "$APPIMAGETOOL_URL"
  chmod +x "$APPIMAGETOOL"
fi
# Extract so no FUSE is required (works in CI containers).
rm -rf "$ROOT/squashfs-root"
( cd "$ROOT" && "$APPIMAGETOOL" --appimage-extract >/dev/null )

echo "==> Building AppImage"
rm -f "$OUTPUT"
ARCH="$ARCH" "$ROOT/squashfs-root/AppRun" "$APPDIR" "$OUTPUT"
rm -rf "$ROOT/squashfs-root"

echo
echo "Done: $OUTPUT"
