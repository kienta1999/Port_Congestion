import matplotlib.pyplot as plt
import numpy as np

accuracies = [0.3302, 0.3530, 0.3794, 0.3949, 0.4373, 0.4556, 0.4576, 0.4129, 0.4570, 0.4705, 0.5094, 0.5062, 0.5044, 0.4957, 0.4873, 0.5086, 0.5057, 0.5021, 0.4946, 0.4849, 0.5014, 0.5294, 0.5097, 0.5060, 0.4794, 0.4581, 0.5025, 0.5013, 0.5013, 0.5097]
epochs = np.arange(1, 31)
plt.plot(epochs, accuracies)
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Accuracy for each Epochs')
plt.savefig('training_result.png')