inputs = [1.0,1.2,-2,2.5,3.0]

weight = [
    [0.1,0.3,.09,.6,.25],
    [0.2,0.8,.09,.6,.20],
    [0.9,0.2,.09,.5,.25],
    [0.2,0.3,.07,.6,.29],
    [0.5,0.3,.09,.6,.27]
    ]

bias = [1.6,
 0.2,
 2.2,
 1.5,
2.2]

layer_output = []
for neuron_wight,neuron_bias in zip(weight,bias):
    neuron_output = 0
    for n_input,weight in zip(inputs,neuron_wight):
        neuron_output += n_input*weight

    neuron_output+=neuron_bias
    layer_output.append(neuron_output)
print(layer_output)
