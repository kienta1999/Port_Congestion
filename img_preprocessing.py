import cv2
# import tensorflow as tf
# from tensorflow.keras.utils import image_dataset_from_directory
import numpy as np
import matplotlib.pyplot as plt
import os


def getImagePath(img_tag):
    return f'./LS-SSDD-v1.0-OPEN/JPEGImages_sub/{img_tag}.jpg'


input_data = []
for file in os.listdir('./LS-SSDD-v1.0-OPEN/JPEGImages_sub'):
    img_path = os.path.join('./LS-SSDD-v1.0-OPEN/JPEGImages_sub', file)
    image = cv2.imread(img_path)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    input_data.append(grayscale)
    print(grayscale)
    break
