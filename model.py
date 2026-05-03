import torch
import cv2
import numpy as np

from models import Darknet
from utils.utils import non_max_suppression


def load_model(cfg="yolov3.cfg", weights="yolov3.weights"):
    model = Darknet(cfg)

    # IMPORTANT: use darknet weights, NOT .pth
    model.load_darknet_weights(weights)

    model.eval()
    return model


def predict_image(model, img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (416, 416))
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img) / 255.0

    img = torch.from_numpy(img).float().unsqueeze(0)

    with torch.no_grad():
        pred = model(img)
        pred = non_max_suppression(pred, 0.5, 0.5)

    return str(pred)