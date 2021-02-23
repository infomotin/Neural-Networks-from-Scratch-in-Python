inputs = [1.0,1.2,2,2.5,3.0]

weights1 = [0.2,0.3,.09,.6,.25]
weights2 = [0.2,0.3,.09,.6,.25]
weights3 = [0.2,0.3,.09,.6,.25]
weights4 = [0.2,0.3,.09,.6,.25]
weights5 = [0.2,0.3,.09,.6,.25]

bias1 = 1.6
bias2 = 0.2
bias3 = 2.2
bias4 = 1.5
bias5 = 2.2

outputs = [
    inputs[0]*weights1[0] + inputs[1]*weights1[1] +inputs[0]*weights1[0] + inputs[0]*weights1[0] + inputs[0]*weights1[0] + bias1 ,
    inputs[0]*weights2[0] + inputs[0]*weights2[0] +inputs[0]*weights2[0] + inputs[0]*weights2[0] + inputs[0]*weights2[0] + bias2 ,
    inputs[0]*weights3[0] + inputs[0]*weights3[0] +inputs[0]*weights3[0] + inputs[0]*weights3[0] + inputs[0]*weights3[0] + bias3 ,
    inputs[0]*weights4[0] + inputs[0]*weights4[0] +inputs[0]*weights4[0] + inputs[0]*weights4[0] + inputs[0]*weights4[0] + bias4 ,
    inputs[0]*weights5[0] + inputs[0]*weights5[0] +inputs[0]*weights5[0] + inputs[0]*weights5[0] + inputs[0]*weights5[0] + bias5 ,
    
    ]
print(outputs)
    