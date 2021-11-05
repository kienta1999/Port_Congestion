import tensorflow as tf
import numpy as np


with open('small_ship_data.npy', 'rb') as f:
    X = np.load(f)
    y = np.load(f)
print(X, y)