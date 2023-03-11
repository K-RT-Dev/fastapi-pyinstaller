import uvicorn
from  multiprocessing import freeze_support

# So that PyInstaller can correctly execute the uvicorn process, we must make the root file of the compilation executable by Python and then execute the uvicorn process independently from it.
if __name__ == "__main__":
    freeze_support()
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, workers=1)