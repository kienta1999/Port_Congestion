import numpy as np
import cv2

model = models.load_model('./CNN.h5')
width = height = 800

while True:
    print("Enter the path of the image, or quit to end: ")
    path = input()
    if path == 'quit':
        break
    try:
        image = cv2.imread(path)
        image = cv2.resize(image, (height, width))
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayscale = np.array(grayscale).reshape(1, height, width, 1)
        print('There are', round(model.predict(grayscale)[0][0]), 'ships in this image.')
    except:
        print("Invalid path")
        continue
