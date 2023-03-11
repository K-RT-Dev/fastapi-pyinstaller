from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Word"}


@app.get("/get_jpg")
async def get_jpg():
    return FileResponse("img/00.jpg")