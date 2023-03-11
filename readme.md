### Introduction

Basic example of using [PyInstaller](https://pyinstaller.org/) to compile a server based on [FastAPI](https://fastapi.tiangolo.com/). For use cases where we need to create a local server simply by running an *.exe*.

The project uses [Poetry](https://python-poetry.org/) to create a Python environment.

The resulting server generates two GET endpoints on *localhost:8000*. The first one is *"/"* which returns a "Hello World". The second one is *"/get_jpg"* which returns a static file embedded in the compiled server.

The trick to be able to use a compiled server using PyInstaller is: 
1. Add *uvicorn* and the *.py* file that starts FastAPI as "hiddenimports" in the *.spec*.
2. Make the generated *.exe* execute a Python function that then runs a *uvicorn* process. PyInstaller cannot directly execute a process with *uvicorn*.
3. Use *freeze_support()* to avoid falling into recursive process problems.

The example includes adding a static file to the compiled server in the *.spec* file.

Solution based on [this](https://github.com/iancleary/pyinstaller-fastapi) repository and [this](https://stackoverflow.com/questions/65438069/uvicorn-and-fastapi-with-pyinstaller-problem-when-uvicorn-workers1) Stackoverflow thread.

### Instructions

0. Make sure to have Python 3.9 installed (other versions may cause conflicts).
1. Install [Poetry](https://python-poetry.org/) if you don't have it.
2. Validate that it is correctly installed using: `poetry -v`
3. Create and activate the environment with: `poetry shell`
4. Install dependencies with: `poetry install`
5. Run the program with Python to validate its functionality: `python main.py`. Make sure there is a response from *localhost:8000* and *localhost:8000/get_jpg*
6. Create the build using: `pyinstaller FastApiPyInstaller.spec`
7. The build can be found in directory */dist*. To run the program, click on "FastApiPyInstaller.exe"

This compilation will result in a folder with an approximate weight of 20mb. If we compress the folder using WinRar, we can achieve a weight of 9.5mb.