from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic.main import BaseModel
import os
from api import *

# uvicorn main:app --reload

ROOT_ENV = os.getcwd()
app = FastAPI()


class InputImageModel(BaseModel):
    input_image : str


@app.get("/facer/check", response_class=HTMLResponse)
def basic(request: Request):
    return "hello minhee"

@app.post("/facer/num",summary="Get face num in image", description="Get face num in image")
async def post_face_num(faceinput: InputImageModel):
    face_num = await insightface_face_num(input_image=faceinput.input_image)
    return {"face_num": face_num}

@app.post("facer/coordinate",summary="Get face coordinate in image", description="Get face coordinate in image")
async def post_face_coordinate(faceinput: InputImageModel):
    face_coordinate = await insightface_face_coordinate(input_image=faceinput.input_image)
    return {"face_coordinate": face_coordinate}
