from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic.main import BaseModel
import os
from api import *

# uvicorn main:app --reload port 8080

ROOT_ENV = os.getcwd()
app = FastAPI()


class FaceNumInputModel(BaseModel):
    input_image : str


@app.get("/facer/check", response_class=HTMLResponse)
def basic(request: Request):
    return "hello minhee22"


@app.post("/facer/num",summary="Get face num in image", description="Get face num in image")
async def face_num(facenuminput: FaceNumInputModel):
    face_num = await face_pose(input_image=facenuminput.input_image)
    return {"face_num": face_num}



