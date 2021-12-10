import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import *
import matplotlib.pyplot as plt
from model_creation import model
from sklearn.utils import resample

with open('ship_data.npy', 'rb') as f:
    X = np.load(f)
    y = np.load(f)

X_minority = X[y != 0]
y_minority = y[y != 0]

X_majority = X[y == 0]
y_majority = y[y == 0]
X_majority_resample, y_majority_resample = resample(X_majority, y_majority, random_state=0, n_samples=(y_minority.shape[0]))

X = np.concatenate((X_minority, X_majority_resample), axis=0)
y = np.concatenate((y_minority, y_majority_resample), axis=0)

data_size, height, width = X.shape
X = X.reshape(data_size, height, width, 1)
y = y.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

print(model.summary())

model.compile(loss=losses.MeanSquaredError(
), optimizer=optimizers.Adam(learning_rate=0.001), metrics=['accuracy'])

model_history = model.fit(X_train, y_train, batch_size=10,
          epochs=30, validation_split = 0.1)

model.save('balanced_CNN.h5')
# # summarize history for accuracy
# plt.plot(model_history.history['accuracy'])
# plt.plot(model_history.history['loss'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig('model_accuracy.png')
# plt.clf()

# plt.plot(model_history.history['val_accuracy'])
# plt.plot(model_history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig('model_loss.png')
# plt.clf()

print('--------------------------------------------------------')
print('evaluate on test set')
loss, acc = model.evaluate(X_test, y_test, verbose=2)
print("Model accuracy on test: {:5.2f}%".format(100 * acc))
print("Model loss on test", loss)
