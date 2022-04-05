import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["PyQt5"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Daily-Task-Planner",
    version="1.0.0",
    description="This software is made for better planning of your entire day.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)