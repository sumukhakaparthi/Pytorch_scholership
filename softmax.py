import numpy as np

# Function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    sum = 0
    soft = []
    for i in range(len(L)):
        sum += np.exp(L[i])
    for i in range(len(L)):
        soft.append(np.exp(L[i]) / sum) 
    return soft
