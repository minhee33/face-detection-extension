
import os
import os.path
import cv2
import numpy as np
import base64

import insightface
from insightface.app import FaceAnalysis


#################################
#################################
#################################

async def insightface_face_num(app: FaceAnalysis, input_image: str):
    try:
        # app = FaceAnalysis(allowed_modules=['detection']) # enable detection model only
        # app.prepare(ctx_id=0, det_size=(640, 640))
        nparr = np.fromstring(base64.b64decode(input_image), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        faces = app.get(img)
        print(f"{len(faces)}개")
        return len(faces)
    except Exception as e:
        print("==error===")
        print(e)


async def insightface_face_coordinate(app: FaceAnalysis, input_image: str):
    try:
        # app = FaceAnalysis(allowed_modules=['detection']) # enable detection model only
        # app.prepare(ctx_id=0, det_size=(640, 640))
        nparr = np.fromstring(base64.b64decode(input_image), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        faces = app.get(img)
        return faces
    except Exception as e:
        print("==error===")
        print(e)
