import numpy as np

from predicatedValue import predicatedValue

#Part 4
def computeErrors(Data, Y, Hypothesis):
    m = np.size(Data,0)
    errors = list()
    if m != np.size(Y, 0):
        print("something went wrong- sizes are not equal")
    for i in range(np.size(Data,0)):
        error = (predicatedValue(Data[i,:], Hypothesis))-Y[i]
        errors.append(error)
    errors = np.reshape(np.array(errors),(np.size(errors),1))
    return errors