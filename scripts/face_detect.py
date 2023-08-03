import gradio as gr
from modules import devices, lowvram, script_callbacks, shared
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic.main import BaseModel
import os
from src.insightface_detector import *



def mount_face_detect_api(_: gr.Blocks, app: FastAPI):
    @app.get("/facedetector/check", response_class=HTMLResponse)
    def get_check(request: Request):
        return "facedetector is okay"
    
    class InputImageModel(BaseModel):
        input_image : str

    @app.post("/facedetector/num",summary="Get face num in image", description="Get face num in image")
    async def post_face_num(faceinput: InputImageModel):
        face_num = await insightface_face_num(input_image=faceinput.input_image)
        return {"face_num": face_num}

    @app.post("/facedetector/coordinate",summary="Get face coordinate in image", description="Get face coordinate in image")
    async def post_face_coordinate(faceinput: InputImageModel):
        face_coordinate = await insightface_face_coordinate(input_image=faceinput.input_image)
        return {"face_coordinate": face_coordinate}


script_callbacks.on_app_started(mount_face_detect_api)