# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
         ( 'res\\setting.json', '.'),
         ( 'res\\creds.json', '.')
         ]
a = Analysis(['main_eel.py', 
                'backend\\afd_docx.py', 
                'backend\\afd_ggl.py', 
                'backend\\afd_helps.py', 
                'backend\\afd_json.py', 
                'backend\\afd_pandas.py'
                ],
             pathex=['E:\\python\\fill_docs'],
             binaries=[],
             datas=[
                 ('C:\\Users\\PTO88\\.virtualenvs\\fill_docs-RRYzcrO0\\lib\\site-packages\\eel\\eel.js', 'eel'), 
                 ('frontend', 'frontend'), 
                 ('res\\icon.ico', '.')],
             hiddenimports=['bottle_websocket', 'docxtpl', 'colorama', 'cryptography', 'gspread', 'oauth2client', 'pandas'],
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
          name='soft v1.1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, 
          icon='res\\icon.ico'
          )
