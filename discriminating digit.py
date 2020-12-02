import numpy as np


def tanh(x) :
    return np.tanh(x)

def softmax(x):
    exp = np.exp(x)
    return exp/exp.sum()

dimensions = [28*28,10]
activation = [tanh,softmax]


print(tanh(0.1))
print(softmax([1,2,3,4]))