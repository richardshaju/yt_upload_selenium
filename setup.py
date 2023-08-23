from cx_Freeze import setup, Executable

setup(
    name="upload",
    version="0.1",
    description="Yt upload",
    executables=[Executable("app.py")]
)
