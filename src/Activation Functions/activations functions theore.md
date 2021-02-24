In this chapter, we will tackle a few of the activation functions and discuss their roles. We use
different activation functions for different cases, and understanding how they work can help you
properly pick which of them is best for your task. The activation function is applied to the output
of a neuron (or layer of neurons), which modifies outputs. We use activation functions because if
the activation function itself is nonlinear, it allows for neural networks with usually two or more
hidden layers to map nonlinear functions. We’ll be showing how this works in this chapter.
In general, your neural network will have two types of activation functions. The first will be the
activation function used in hidden layers, and the second will be used in the output layer. Usually,
the activation function used for hidden neurons will be the same for all of them, but it doesn’t
have to.

The Step Activation Function
Recall the purpose this activation function serves is to mimic a neuron “firing” or “not firing”
based on input information. The simplest version of this is a step function. In a single neuron, if
the weights · inputs + bias results in a value greater than 0, the neuron will fire and output a 1;
otherwise, it will output a 0.
Fig 4.01: Step function graph.
This activation
