# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


added_files = [
         ( 'res\\setting.json', '.')
         ]


a = Analysis([
    'main.py', 
    'softafd\\afd_ggl.py', 
    'softafd\\afd_json.py', 
    'softafd\\afd_helps.py', 
    'softafd\\afd_pandas.py'
    ],
             pathex=['E:\\python\\AFDsoftVK2'],
             binaries=[],
             datas=[('res\\icon.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='soft',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, icon='res\\icon.ico')
