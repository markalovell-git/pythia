# Pythia

Desktop astrology app — natal charts, transits, diary, timeline.

## Install (Linux)

Download the latest **`Pythia-x86_64.AppImage`** from the
[Releases page](https://github.com/markalovell-git/pythia/releases/latest),
make it executable, and run it:

```
chmod +x Pythia-x86_64.AppImage
./Pythia-x86_64.AppImage
```

(Or right-click → Properties → "Allow executing file as program", then
double-click.) Nothing else is required — Python, Qt, and the star ephemeris are
all bundled. Some distros need `libfuse2` to run AppImages
(`sudo apt install libfuse2` on Debian/Ubuntu).

On first launch Pythia offers to add itself to your applications menu (so you can
launch and pin it like a normal app); you can toggle this any time under
**Settings → Desktop**. Keep the AppImage somewhere stable — the menu entry
points at it, and updates replace it in place.

User data (database, ephemeris, logs) lives in `~/.local/share/Pythia/`,
separate from the app, so updates never touch it.

## Updates

On launch the AppImage checks the GitHub Releases API for a newer version. If
one exists it prompts before downloading the new AppImage, swaps itself in
place, and relaunches. Decline to keep the current version. Offline or when run
from source, the check is skipped.

## Run from source (development)

```
uv sync
uv run pythia
```

(equivalently `uv run python -m app.frontend.main`)

## Releasing a new version

The AppImage is built and published automatically by CI
(`.github/workflows/release.yml`) when you push a `vX.Y.Z` tag:

```
# edit app/__version__ to the new number, then:
git commit -am "Bump to 0.1.3"
git tag v0.1.3
git push && git push --tags
```

GitHub Actions builds `Pythia-x86_64.AppImage`, smoke-tests it, and attaches it
to the `v0.1.3` Release; installed copies detect the new tag and offer it as an
update. To build the AppImage locally instead: `bash scripts/build_appimage.sh`.

## Test

```
uv run pytest
```

## Dev setup

```
uv sync
```

On first launch, Skyfield will download the ephemeris file (~17MB, one time only). After that the app runs fully offline.

## Auto-restart on code changes

During development, use `watchmedo` to automatically restart the app whenever a `.py` file is saved:

```
uv run watchmedo auto-restart --patterns="*.py" --recursive -- python -m app.frontend.main
```
