# Pythia

Desktop astrology app — natal charts, transits, diary, timeline.

## Run

```
uv run python -m app.frontend.main
```

## Test

```
uv run pytest
```

## Dev setup

```
uv sync
```

On first launch, Skyfield will download the ephemeris file (~17MB, one time only). After that the app runs fully offline.
