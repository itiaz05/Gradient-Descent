import numpy as np
from computeErrors import computeErrors

#Part 6
def computeCost(Data, Y, Hypothesis):
    errors = computeErrors(Data, Y, Hypothesis)
    examplesNumber = np.size(errors)
    sum = np.sum(errors**2)
    return sum /(2*examplesNumber)