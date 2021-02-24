# Now that we no longer need to hand-type our data, we should create something similar for our
# various types of neural network layers. So far, we’ve only used what’s called a dense or
# fully-connected layer. These layers are commonly referred to as “dense” layers in papers,
# literature, and code, but you will occasionally see them called fully-connected or “fc” for short in
# code. Our dense layer class will begin with two methods.


# Otimitions
# As previously stated, weights are often initialized randomly for a model, but not always. If you
# wish to load a pre-trained model, you will initialize the parameters to whatever that pretrained
# model finished with. It’s also possible that, even for a new model, you have some other
# initialization rules besides random. For now, we’ll stick with random initialization. Next, we have
# the forward method. When we pass data through a model from beginning to end, this is called a
# forward pass . Just like everything else, however, this is not the only way to do things. You can
# have the data loop back around and do other interesting things. We’ll keep it usual and perform a
# regular forward pass.
import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forword(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


# demo data loade from libray

X, y = spiral_data(samples=100, classes=3)

print(X)

# create an object on Layer_Dense class
dense1 = Layer_Dense(2, 3)
dense1.forword(X)

print(dense1.output[:5])
