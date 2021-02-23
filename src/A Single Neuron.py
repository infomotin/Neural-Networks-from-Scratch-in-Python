inputs = [1,2,3]
weight = [.1,.5,.3]
bias = 2

outputs = (
    inputs[0]*weight[0]+
    inputs[1]*weight[1]+
    inputs[0]*weight[2] + bias
            
)
print(outputs)