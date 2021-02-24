In this chapter, we will tackle a few of the activation functions and discuss their roles. We use
different activation functions for different cases, and understanding how they work can help you
properly pick which of them is best for your task.

The activation function is applied to the output
of a neuron (or layer of neurons),
which modifies outputs.

We use activation functions because if
the activation function itself is nonlinear,
doc https://en.wikipedia.org/wiki/Nonlinear_system
https://byjus.com/maths/difference-between-linear-and-nonlinear-equations/

it allows for neural networks with usually two or more
hidden layers to map nonlinear functions.
In general, your neural network will have two types of activation functions.
The first will be the
activation function used in hidden layers,
and the second will be used in the output layer.
Usually,
the activation function used for hidden neurons will be the same for all of them, but it doesn’t
have to.

The Step Activation Function
Recall the purpose this activation function serves is to mimic a neuron “firing” or “not firing”
based on input information. The simplest version of this is a step function. In a single neuron, if
the weights · inputs + bias results in a value greater than 0, the neuron will fire and output a 1;
otherwise, it will output a 0.
Fig 4.01: Step function graph.
This activation

# The Linear Activation Function

A linear function is simply the equation of a line. It will appear as a straight line when graphed,
where y=x and the output value equals the input.

# The Sigmoid Activation Function:

# The Sigmoid Activation Function

# The problem with the step function is it’s not very informative. When we get to training and

network optimizers, you will see that the way an optimizer works is by assessing individual
impacts that weights and biases have on a network’s output. The problem with a step function is
that it’s less clear to the optimizer what these impacts are because there’s very little information
gathered from this function. It’s either on (1) or off (0). It’s hard to tell how “close” this step
function was to activating or deactivating. Maybe it was very close, or maybe it was very far. In
terms of the final output value from the network, it doesn’t matter if it was close to outputting
something else. Thus, when it comes time to optimize weights and biases, it’s easier for the
optimizer if we have activation functions that are more granular and informative.

# The original, more granular, activation function used for neural networks was the Sigmoid

activation function, which looks like:

y = 1/(1 + e^-x)
function return 0 for negative infinity,

# This function returns a value in the range of 0 for negative infinity, through 0.5 for the input of 0,

# and to 1 for positive infinity.
