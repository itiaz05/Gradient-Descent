import numpy as np

#Part 7
def updateHypothesis(Hypothesis, alpha, Gradient):
    updatedHypothesis = list()
    for i in range(np.size(Hypothesis)):
        updatedHypothesis.append(Hypothesis[i]-alpha*Gradient[i])
    return np.array(updatedHypothesis)