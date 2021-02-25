# ReLU activation function

inputs = [0, 2, -1, 3.3, 4.0, 2.2, -100]
outputs = []
for i in inputs:
    if i > 0:
        outputs.append(i)
    else:
        outputs.append(0)
print(outputs)
