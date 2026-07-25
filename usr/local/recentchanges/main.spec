# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from pathlib import Path
import PIL
# datas = [('Resources', 'Resources')]
datas = []
binaries = []
hiddenimports = []
# if missing something from pystaller for pyside6 uncomment these two
#tmp_ret = collect_all('PySide6')
#datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

# if getting cannot find shiboken uncomment the two lines below
#tmp_ret = collect_all('shiboken6')
#datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
_pillow_libs_dir = Path(PIL.__file__).resolve().parent.parent / "pillow.libs"
_pillow_lib_bins = []
if _pillow_libs_dir.is_dir():
	_pillow_lib_bins = [(str(p), "pillow.libs") for p in _pillow_libs_dir.glob("*.so*")]
	binaries += _pillow_lib_bins

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'PySide6.QtWebEngine',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtWebEngineCore',
        'PySide6.QtQml',
        'PySide6.QtQuick',
        'PySide6.Qt3DCore',
        'PySide6.Qt3DRender',
        'PySide6.QtBluetooth',
        'PySide6.QtNfc',
        'PySide6.QtPositioning',
        'PySide6.QtSensors',
        'PySide6.QtSerialPort',
        'PySide6.QtCharts',
        'PySide6.QtPrintSupport',
    ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='main',
)
