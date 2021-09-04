import sys
import os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':  # for GUI app
    base = 'Win32GUI'

exe = Executable(script='pyBrowserSelection.py',
                 base=base)


opts = {
    'build': {
        'build_exe': 'dist',
    },
    'build_exe': {
        'optimize': '2',
    },
    'install_exe': {
        'install_dir':
            os.environ['HOMEPATH'] + r'\AppData\Local\pyBrowserSelection\bin',
    },
}


setup(name='pyBrowserSelection',
      version='0.1',
      options=opts,
      executables=[exe])
