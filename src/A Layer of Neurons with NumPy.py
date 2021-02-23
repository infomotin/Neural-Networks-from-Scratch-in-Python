import numpy as np
inputs = [1.2, 2.3, 2.0, 1.9, 2.0]
weight = [
    [0.2, 0.6, 0.20, 1.2, .35],
    [0.3, 0.3, 0.15, 1.0, .5],
    [0.5, 0.6, 0.25, 1.1, .32],
    [0.1, 0.2, 0.5, 1.0, .55],
    [0.6, 0.15, 0.5, 1.4, .15]

]

biao = [2.0, .25, .36, .9, .98]

oputPuts = np.dot(inputs, weight) + biao
print(oputPuts)
