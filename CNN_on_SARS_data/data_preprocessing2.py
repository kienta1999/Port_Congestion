import cv2
# import tensorflow as tf
# from tensorflow.keras.utils import image_dataset_from_directory
import numpy as np
import json
import os

X = []
y = []
ship_counts = json.load(open('output.json',))
print(ship_counts[0]['img_tag'])
for file in os.listdir('./LS-SSDD-v1.0-OPEN/JPEGImages_sub'):
    img_tag = file.split('.')[0]
    img_path = os.path.join('./LS-SSDD-v1.0-OPEN/JPEGImages_sub', file)
    image = cv2.imread(img_path)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    X.append(grayscale)
    ship_count = next(filter((lambda x: x['img_tag'] == img_tag), ship_counts))[
        'ship_count']
    y.append(ship_count)
with open('ship_data.npy', 'wb') as f:
    np.save(f, X)
    np.save(f, y)


# with open('ship_data.npy', 'rb') as f:
#     X = np.load(f)
#     y = np.load(f)
# print(X, y)
print("done")
