import numpy as np

with open('ship_data.npy', 'rb') as f:
    X = np.load(f)
    y = np.load(f)
print(X.shape, y.shape)
