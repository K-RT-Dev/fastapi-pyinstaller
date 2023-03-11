# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = []
hiddenimports += collect_submodules('uvicorn') # We need to add the dependencies of "uvicorn" as "hiddenimports"
hiddenimports += ['app'] # We also need to add the file that initiates FastApi as "hiddenimports", since "main.py" doesn't explicitly import it

# We can add directories with static files here
added_files = [
  ('./img', './img')
]

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Here we should specify the Python packages that we only use for the development process, so they are not included in the final build
exclude = ["pastel", "tomli", "poethepoet"]
a.binaries = [x for x in a.binaries if not x[0].startswith(tuple(exclude))]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FastApiPyInstaller',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
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
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FastApiPyInstaller',
)
