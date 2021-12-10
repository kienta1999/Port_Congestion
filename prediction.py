import tensorflow as tf
from tensorflow.keras import *
import numpy as np
from sklearn.model_selection import train_test_split

model = models.load_model('./CNN.h5')

with open('ship_data.npy', 'rb') as f:
    X = np.load(f)
    y = np.load(f)
data_size, height, width = X.shape
X = X.reshape(data_size, height, width, 1)
y = y.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


print('--------------------------------------------------------')
print('evaluate on test set')
loss, acc = model.evaluate(X_test, y_test, verbose=2)
print("Model accuracy on test: {:5.2f}%".format(100 * acc))
print("Model loss on test", loss)
