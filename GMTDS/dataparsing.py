import numpy as np
from PIL import Image
import os
import json
  
data = []
for filename in os.listdir('/Users/tusharmenon/portcongestion'):
    img = Image.open(filename)
    img_as_nparray = np.array(img)
    data.append(img_as_nparray)
data = json.dumps(data)