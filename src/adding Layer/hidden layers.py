import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2., 5., - 1., 2],
          [- 1.5, 2.7, 3.3, - 0.8]]
weights = [[0.2, 0.8, - 0.5, 1],
           [0.5, - 0.91, 0.26, - 0.5],
           [- 0.26, - 0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
# 2nd layer
weights2 = [[0.1, - 0.14, 0.5],
            [- 0.5, 0.12, - 0.33],
            [- 0.44, 0.73, - 0.13]]
biases2 = [- 1, 2, - 0.5]

# 3rd layer
weights3 = [[0.1, - 0.14, 0.5],
            [- 0.55, 0.12, - 0.31],
            [- 0.44, 0.43, - 0.13]]
biases3 = [- 1.3, 2.2, - 0.7]

# //output1 layer

layer1_output = np.dot(inputs, np.array(weights).T)+biases
print(layer1_output)
# 2nd layer output
Second_layer_output = np.dot(layer1_output, np.array(weights2).T)+biases2
print(Second_layer_output)

# 3rd layer output
therad_layerOutput = np.dot(Second_layer_output, np.array(weights3).T)+biases3
print("therad_layerOutput")
print(therad_layerOutput)
