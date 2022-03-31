import numpy as np
from loadData import loadData
from computeCost import computeCost
from computeErrors import computeErrors
from computeGradient import computeGradient
from normalizePrices import addOnesColumn, normalizePrices
from updateHypothesis import updateHypothesis

def gradientDescent(filename, alpha, max_iter, treshold):
    if not alpha in locals():
        alpha = 0.1
    if not max_iter in locals():
        max_iter = 1000
    if not treshold in locals():
        treshold = 0.001
    
    #initialize:
    cost = np.inf
    Costs = []
    iter = 1
    improvement = 0

    [D, Y] = loadData(filename)
    D = normalizePrices(D)
    D = addOnesColumn(D)
    hypothesis = np.zeros(np.size(D,1),dtype=np.float64)
    while iter < max_iter:
        errors = computeErrors(D, Y, hypothesis)
        cost = computeCost(D, Y,hypothesis)
        Costs.append(cost)
        gradient = computeGradient(D, errors)
        hypothesis = updateHypothesis(hypothesis, alpha, gradient)
        if iter>1:  #not first iteration
            improvement = Costs[iter-2]-Costs[iter-1]
            if improvement<treshold:
                print("Gradient descent terminating after %s iterations. cost hasn't improved." % iter)
                break
        iter += 1
    if iter >= max_iter:
        print("Gradient descent terminating after %s iterations (max_iter)" % iter)
    elif improvement>=treshold:
        print("Gradient descent terminating after %s iterations. Improvement was : %f – below threshold (%d)" % iter, improvement, treshold )

    return [hypothesis, Costs]

    