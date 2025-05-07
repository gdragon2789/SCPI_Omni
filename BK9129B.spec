# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ui\\BK9129B.py'],
    pathex=['D:/Work/Develop/SW/Omnicomm_SCPI'],
    binaries=[],
    datas=[('ui\\Omnicomm_logo.ico', '.'),('ui\\Company_logo.png','.')],
    hiddenimports=['instrument.Power_Supply.BK9129B'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='BK9129B',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ui\\Omnicomm_logo.ico'],
)
