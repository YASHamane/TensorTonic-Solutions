import numpy as np

def sigmoid(x):
    h = np.array(x)
    sig = 1 / (1+(np.exp(-h)))
    return sig