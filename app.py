from fastapi import FastAPI, UploadFile, File
import shutil
import cv2
from model import load_model, predict_image

app = FastAPI()

model = load_model()


@app.get("/")
def home():
    
    return {"msg": "YOLOv3 running (clean inference setup)"}


@app.post("/predict")
def predict(file: UploadFile = File(...)):
    file_path = "input.jpg"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_image(model, file_path)

    return {"result": result}