# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\ProyectoTesis\\mobileapp'],  # Ajusta la ruta a tu directorio del proyecto
    binaries=[],
    datas=[
        ('C:\\ProyectoTesis\\mobileapp\\Fuentes\\*.ttf', 'Fuentes'),  # Incluye todas las fuentes .ttf en la carpeta 'Fuentes'
        ('C:\\ProyectoTesis\\mobileapp\\Iconos\\*.png', 'Iconos'),    # Incluye todos los iconos .png en la carpeta 'Iconos'
        ('C:\\ProyectoTesis\\mobileapp\\Logos\\*.png', 'Logos'),      # Incluye todos los logos .png en la carpeta 'Logos'
        ('C:\\ProyectoTesis\\mobileapp\\main.kv', '.')  # Incluye main.kv en el directorio raíz del ejecutable
    ],
    hiddenimports=[],
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

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
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
)

