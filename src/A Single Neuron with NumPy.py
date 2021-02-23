import numpy as np
inputs =  [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.3, 0.56, 0.12]
bias = 2.3
outputs = np.dot(inputs,weights) + bias
print(outputs)