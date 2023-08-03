
from PIL import Image
import os
import os.path
from os import path
import json
from tqdm import tqdm
import cv2
import math
import numpy as np
import base64

import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image


#################################
#################################
#################################

app = FaceAnalysis(allowed_modules=['detection']) # enable detection model only
app.prepare(ctx_id=0, det_size=(640, 640))

async def face_pose(input_image: str):
    try:
        # app = FaceAnalysis(allowed_modules=['detection']) # enable detection model only
        # app.prepare(ctx_id=0, det_size=(640, 640))
        # encoded_data = input_image.split(',')[1]
        nparr = np.fromstring(base64.b64decode(input_image), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        faces = app.get(img)
        print(f"{len(faces)}개")
        return len(faces)
    except Exception as e:
        print("==error===")
        print(e)


