import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

# dens layer


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.outputs = np.dot(inputs, self.weights) + self.biases


class Activation_RuLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activations_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs-np.max(inputs, axis=1, keepdims=True))

        probabilities = exp_values/np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilities


X, y = spiral_data(samples=100, classes=3)

des1 = Layer_Dense(2, 3)

act1 = Activation_RuLU()

des2 = Layer_Dense(3, 3)

act2 = Activations_Softmax()

des1.forward(X)

act1.forward(des1.outputs)

des2.forward(act1.output)

act2.forward(des2.outputs)

print(act2.output[:5])
