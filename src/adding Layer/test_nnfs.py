import numpy as np
import nnfs
nnfs.init()

# print(np.random.rand(2, 5))
# print(np.zeros((2, 5)))
n_inputs = 2
n_neurons = 5

weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases = np.zeros((1, n_neurons))

print(weights)
print(biases)
