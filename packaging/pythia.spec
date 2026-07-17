# PyInstaller spec for Pythia (one-dir build, wrapped into an AppImage).
# Build:  uv run pyinstaller packaging/pythia.spec
from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules

ROOT = Path(SPECPATH).parent  # packaging/ -> repo root

datas = []
binaries = []
hiddenimports = [
    # uvicorn resolves these dynamically; PyInstaller can't see them statically.
    "uvicorn.loops.auto",
    "uvicorn.protocols.http.auto",
    "uvicorn.protocols.websockets.auto",
    "uvicorn.lifespan.on",
    "uvicorn.logging",
    "cffi",  # timezonefinder's C-extension loader
    # keyring discovers backends via entry points — invisible to static analysis
    "keyring.backends.SecretService",
    "keyring.backends.kwallet",
    "keyring.backends.chainer",
    "keyring.backends.fail",
]

datas += collect_data_files("skyfield")        # skyfield's packaged data
datas += collect_data_files("tzdata")          # pure-python tz database
datas += [(str(ROOT / "data" / "de421.bsp"), "data")]  # bundled ephemeris
datas += [(str(ROOT / "packaging" / "pythia.svg"), ".")]  # icon for desktop integration
hiddenimports += collect_submodules("app")     # ensure backend routers are bundled

# timezonefinder is imported lazily (in account_wizard.py), so its dependency
# tree — including flatbuffers and h3 — is invisible to static analysis. Collect
# these packages (data + binaries + submodules) explicitly.
for _pkg in ("timezonefinder", "flatbuffers", "h3"):
    _d, _b, _h = collect_all(_pkg)
    datas += _d
    binaries += _b
    hiddenimports += _h


a = Analysis(
    [str(ROOT / "main.py")],
    pathex=[str(ROOT)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=["tkinter"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="pythia",
    console=False,           # GUI app — no console window
    disable_windowed_traceback=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    name="pythia",
)
