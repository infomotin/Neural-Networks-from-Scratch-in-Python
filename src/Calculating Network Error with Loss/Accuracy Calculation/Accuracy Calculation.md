While loss is a useful metric for optimizing a model, the metric commonly used in practice along
with loss is the accuracy , which describes how often the largest confidence is the correct class
in terms of a fraction. Conveniently, we can reuse existing variable definitions to calculate the
accuracy metric. We will use the argmax values from the softmax outputs and then compare
these to the targets. This is as simple as doing (note that we slightly modified the
softmax_outputs for the purpose of this example):
import numpy as np

# Probabilities of 3 samples

softmax_outputs = np.array([[0.7 , 0.2 , 0.1 ],
[ 0.5 , 0.1 , 0.4 ],
[ 0.02 , 0.9 , 0.08]])

# Target (ground-truth) labels for 3 samples

class_targets = np.array([ 0 , 1 , 1 ])

# Calculate values along second axis (axis of index 1)

predictions = np.argmax(softmax_outputs, axis = 1 )

# If targets are one-hot encoded - convert them

if len (class_targets.shape) == 2 :
class_targets = np.argmax(class_targets, axis = 1 )

# True evaluates to 1; False to 0

accuracy = np.mean(predictions == class_targets)
print ( 'acc:' , accuracy)

> > > acc: 0.6666666666666666
> > > We are also handling one-hot encoded targets by converting them to sparse values using
> > > np.argmax() .
> > > Chapter 5 - Calculating Network Error with Loss - Neural Networks from Scratch in Python
> > > 25
> > > We can add the following to the end of our full script above to calculate its accuracy:

# Calculate accuracy from output of activation2 and targets

# calculate values along first axis

predictions = np.argmax(activation2.output, axis = 1 )
if len (y.shape) == 2 :
y = np.argmax(y, axis = 1 )
accuracy = np.mean(predictions == y)

# Print accuracy

print ( 'acc:' , accuracy)

> > > acc: 0.34
> > > Now that you’ve learned how to perform a forward pass through our network and calculate the
> > > metrics to signal if the model is performing poorly, we will embark on optimization in the next
> > > chapter!
