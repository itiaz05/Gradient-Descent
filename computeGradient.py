import numpy as np


def computeGradient(Data, Errors):
    examplesNumber = np.size(Errors)
    Errors = Errors[:,0]
    gradient = list()
    for i in range(np.size(Data,1)):    #0-features
        gradient.append(np.sum(Data[:,i] * Errors))
        gradient[i] = gradient[i]/examplesNumber
    gradient = np.array(gradient)
    return gradient
        