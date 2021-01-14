import sys, platform, os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter",'subprocess','jinja2','jinja2schema','subprocess','re','time','idlelib','os','traceback','sys','ast','tkcalendar','datetime','json'], 
                    "excludes": [""],
                    }

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
appName = None

if sys.platform == "win32":
    base = "Win32GUI"
    appName = "medpress.exe"

if sys.platform == "linux":
    appName = "medpress"

if sys.platform == "darwin":
    appName = 'medpress'

executable = [
    Executable(
        "main.py",
        base=base,
        targetName=appName,
        icon='icon.ico',
    )
]

setup(  name = "medpress",
        version = "0.1",
        description = "Mazy7c8 application!",
        options = {"build_exe": build_exe_options},
        executables = executable
        )