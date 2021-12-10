import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import *
import matplotlib.pyplot as plt

with open('ship_data.npy', 'rb') as f:
    X = np.load(f)
    y = np.load(f)
data_size, height, width = X.shape
X = X.reshape(data_size, height, width, 1)
y = y.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

input = Input(shape=(800, 800, 1))
x = layers.Conv2D(6, (3, 3), activation='relu', padding='same')(input)
x = layers.BatchNormalization()(x)
# output shape: (800, 800, 6)
x = layers.MaxPooling2D((4, 4), padding='same')(x)
x = layers.BatchNormalization()(x)
# downsize to (200, 200, 6)
x = layers.Conv2D(12, (3, 3), activation='relu', padding='same')(x)
x = layers.BatchNormalization()(x)
# output shape: (200, 200, 12)
x = layers.MaxPooling2D((4, 4), padding='same')(x)
x = layers.BatchNormalization()(x)
# downsize to (50, 50, 12)
x = layers.Conv2D(24, (3, 3), activation='relu', padding='same')(x)
x = layers.BatchNormalization()(x)
# output shape: (50, 50, 24)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.BatchNormalization()(x)
# downsize to (25, 25, 24)
x = layers.Conv2D(48, (3, 3), activation='relu', padding='same')(x)
x = layers.BatchNormalization()(x)
# output shape: (50, 50, 48)
x = layers.MaxPooling2D((2, 2), padding='same')(x)
x = layers.BatchNormalization()(x)
# downsize to (13, 13, 48)

x = layers.Flatten()(x)
# x = layers.Dense(4056, activation='relu')(x)
# x = layers.BatchNormalization()(x)
x = layers.Dense(1024, activation='relu')(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(512, activation='relu')(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(128, activation='relu')(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(64, activation='relu')(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(32, activation='relu')(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(1, activation='relu')(x)


output = activations.relu(x)
model = Model(inputs=input, outputs=output, name="SAR_SHIP_DETECTION")
print(model.summary())

model.compile(loss=losses.MeanSquaredError(
), optimizer=optimizers.Adam(learning_rate=0.001), metrics=['accuracy'])

model_history = model.fit(X_train, y_train, batch_size=10,
          epochs=30, validation_split = 0.1)

model.save('CNN.h5')
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
