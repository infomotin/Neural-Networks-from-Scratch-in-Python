With a randomly-initialized model, or even a model initialized with more sophisticated
approaches, our goal is to train, or teach, a model over time.

To train a model, we tweak the
weights and biases to improve the model’s accuracy and confidence.
To do this, we calculate how
much error the model has. The loss function , also referred to as the cost function , is the
algorithm that quantifies how wrong a model is. Loss is the measure of this metric. Since loss is
the model’s error, we ideally want it to be 0.
You may wonder why we do not calculate the error of a model based on the argmax accuracy.
Recall our earlier example of confidence: [ 0.22 , 0.6 , 0.18 ] vs [ 0.32 , 0.36 , 0.32 ] .
If the correct class were indeed the middle one (index 1), the model accuracy would be identical
between the two above. But are these two examples really as accurate as each other? They are
not, because accuracy is simply applying an argmax to the output to find the index of the
biggest value. The output of a neural network is actually confidence, and more confidence in

the correct answer is better. Because of this, we strive to increase correct confidence and
decrease misplaced confidence.
