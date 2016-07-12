import numpy as np

# Transforms a list of scores into probabilities which
# add up to one. Softmax is often used as a last layer
# for classification.
def softmax(scores):
	return np.exp(scores) / np.sum(np.exp(scores))
