import numpy as np
a = [2, 3, 4]
b = [6, 5, 4]

a = np.array([a])
b = np.array([b]).T

print(a)
print(b)

output = np.dot(a, b)
print(output)
