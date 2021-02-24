import numpy as np
import nnfs
nnfs.init()
# Here, we’re setting weights to be random and biases to be 0. Note that we’re initializing weights
# to be (inputs, neurons), rather than ( neurons, inputs) . We’re doing this ahead instead of
# transposing every time we perform a forward pass, as explained in the previous chapter. Why zero
# biases? In specific scenarios, like with many samples containing values of 0, a bias can ensure
# that a neuron fires initially. It sometimes may be appropriate to initialize the biases to some
# non-zero number, but the most common initialization for biases is 0. However, in these scenarios,
# you may find success in doing things another way. This will vary depending on your use-case and
# is just one of many things you can tweak when trying to improve results. One situation where you
# might want to try something else is with what’s called dead neurons . We haven’t yet covered
# activation functions in practice, but imagine our step function again.

# It’s possible for weights · inputs + biases not to meet the threshold of the step function, which
# means the neuron will output a 0. Alone, this is not a big issue, but it becomes a problem if this
# happens to this neuron for every one of the input samples (it’ll become clear why once we cover
# backpropagation). So then this neuron’s 0 output is the input to another neuron. Any weight
# multiplied by zero will be zero. With an increasing number of neurons outputting 0, more inputs
# to the next neurons will receive these 0s rendering the network essentially non-trainable, or
# “dead.”
# Next, let’s explore np.random.randn and np.zeros in more detail. These methods are
# convenient ways to initialize arrays. np.random.randn produces a Gaussian distribution with a
# mean of 0 and a variance of 1, which means that it’ll generate random numbers, positive and
# negative, centered at 0 and with the mean value close to 0. In general, neural networks work best
# with values between -1 and +1, which we’ll discuss in an upcoming chapter. So this
# np.random.randn generates values around those numbers. We’re going to multiply this
# Gaussian distribution for the weights by 0.01 to generate numbers that are a couple of
# magnitudes smaller. Otherwise, the model will take more time to fit the data during the training
# process as starting values will be disproportionately large compared to the updates being made
# during training. The idea here is to start a model with non-zero values small enough that they
# won’t affect training. This way, we have a bunch of values to begin working with, but hopefully
# none too large or as zeros. You can experiment with values other than 0.01 if you like.
# Finally, the np.random.randn function takes dimension sizes as parameters and creates the
# output array with this shape. The weights here will be the number of inputs for the first dimension
# and the number of neurons for the 2nd dimension. This is similar to our previous made up array of
# weights, just randomly generated. Whenever there’s a function or block of code that you’re not
# sure about, you can always print it out. For example:
# print(np.random.rand(2, 5))
# print(np.zeros((2, 5)))
n_inputs = 2
n_neurons = 5

weights = 0.01 * np.random.randn(n_inputs, n_neurons)
biases = np.zeros((1, n_neurons))

print(weights)
print(biases)
