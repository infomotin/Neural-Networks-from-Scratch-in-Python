# ReLU activation function
import numpy as np
import math
inputs = [0, 2, -1, 3.3, 4.0, 2.2, -100]
outputs = []
# for i in inputs:
#     if i > 0:
#         outputs.append(i)
#     else:
#         outputs.append(0)
# print(outputs)

# for i in inputs:
#     outputs.append(max(0, i))
# print(outputs)


outputs = np.maximum(0, inputs)
# print(outputs)


Layer_output = [4.8, 1.12, 2.385]

E = math.e

exp_value = []

for output in Layer_output:
    exp_value.append(E**output)
# print(exp_value)

normal_base = sum(exp_value)
mormal_valu = []
for value in exp_value:
    mormal_valu.append(value/normal_base)
print("Normal Value")
print(mormal_valu)


exp_values = np.exp(Layer_output)
mormal_valu = exp_values/np.sum(exp_values)

print(mormal_valu)
