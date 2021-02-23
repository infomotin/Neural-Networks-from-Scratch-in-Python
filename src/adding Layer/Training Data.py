from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt
import nnfs
# The nnfs.init() does three things: it sets the random seed to 0 (by the default), creates a
# float32 dtype default, and overrides the original dot product from NumPy. All of these are meant
# to ensure repeatable results for following along.
# The spiral_data function allows us to create a dataset with as many classes as we want. The
# function has parameters to choose the number of classes and the number of points/observations
# per class in the resulting non-linear dataset. For example:

nnfs.init()
X, y = spiral_data(samples=100, classes=3)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='inferno_r')
plt.show()
