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

The Rectified Linear Activation Function
Fig 4.04: Graph of the ReLU activation function.
The rectified linear activation function is simpler than the sigmoid. It’s quite literally y=x , clipped
at 0 from the negative side. If x is less than or equal to 0 , then y is 0 — otherwise, y is equal to x .
Chapter 4 - Activation Functions - Neural Networks from Scratch in Python
11
This simple yet powerful activation function is the most widely used activation function at the
time of writing for various reasons — mainly speed and efficiency. While the sigmoid activation
function isn’t the most complicated, it’s still much more challenging to compute than the ReLU
activation function. The ReLU activation function is extremely close to being a linear activation
function while remaining nonlinear, due to that bend after 0. This simple property is, however,
very effective.

# The rectified linear activation function is simpler than the sigmoid. It’s quite literally y=x , clipped

# at 0 from the negative side. If x is less than or equal to 0 , then y is 0 — otherwise, y is equal to x .

## Why Use Activation Functions?

Now that we understand what activation functions represent, how some of them look, and what
they return, let’s discuss why we use activation functions in the first place. In most cases, for a
neural network to fit a nonlinear function, we need it to contain two or more hidden layers, and
we need those hidden layers to use a nonlinear activation function.
First off, what’s a nonlinear function? A nonlinear function cannot be represented well by a
straight line, such as a sine function:

While there are certainly problems in life that are linear in nature, for example, trying to figure
out the cost of some number of shirts, and we know the cost of an individual shirt, and that there
are no bulk discounts, then the equation to calculate the price of any number of those products is a
linear equation.

Other problems in life are not so simple, like the price of a home. The number of
factors that come into play,
such as size,
location,
time of year attempting to sell,
number of
rooms,
yard,
neighborhood,
and so on,
makes the pricing of a home a nonlinear equation.
Many of
the more interesting and hard problems of our time are nonlinear. The main attraction for neural
networks has to do with their ability to solve nonlinear problems. First, let’s consider a situation
where neurons have no activation function,

which would be the same as having an activation
function of y=x .
With this linear activation function in a neural network with 2 hidden layers of 8
neurons each, the result of training this model will look like:

4.06: Neural network with linear activation functions in hidden layers attempting to fit
y=sin(x)

# Linear Activation in the Hidden Layers

Now that you can see that this is the case, we still should consider why this is the case. To begin,
let’s revisit the linear activation function of y=x , and let’s consider this on a singular neuron level.
Given values for weights and biases, what will the output be for a neuron with a y=x activation
function? Let’s look at some examples — first, let’s try to update the first weight with a positive
value:

Fig 4.08: Example of output with a neuron using a linear activation function.
As we continue to tweak with weights, updating with a negative number this time:
Fig 4.09: Example of output with a neuron using a linear activation function, updated weight.
Chapter 4 - Activation Functions - Neural Networks from Scratch in Python
14
And updating weights and additionally a bias:
Fig 4.10: Example of output with a neuron using a linear activation function, updated another
weight.
No matter what we do with this neuron’s weights and biases, the output of this neuron will be
perfectly linear to y=x of the activation function. This linear nature will continue throughout the
entire network:
Fig 4.11: A neural network with all linear activation functions.
No matter what we do, however many layers we have, this network can only depict linear
relationships if we use linear activation functions. It should be fairly obvious that this will be the
case as each neuron in each layer acts linearly, so the entire network is a linear function as well.

# ReLU Activation in a Pair of Neurons
