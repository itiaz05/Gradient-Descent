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
    cost_j = []
    iter = 1
    improvement = 0
    [D, Y] = loadData(filename)
    D = normalizePrices(D)
    D = addOnesColumn(D)
    hypothesis = np.zeros(np.size(D,1),dtype=np.float64)
    while iter < max_iter:
        print("------------- iter: %d -----------------" % (iter-1))
        errors = computeErrors(D, Y, hypothesis)
        cost = computeCost(D, Y,hypothesis)
        print("cost for iteration is: %s" % cost)
        cost_j.append(cost)
        gradient = computeGradient(D, errors)
        print("gradient for iteration: %s" % gradient)
        hypothesis = updateHypothesis(hypothesis, alpha, gradient)
        print("updatedHypothesis: %s" % hypothesis)
        print("cost_j[iter]: %s" % cost_j[iter-1])
        if iter>1:  #not first iteration
            print("cost_j[iter-1]: %s" % cost_j[iter-2])
            improvement = cost_j[iter-2]-cost_j[iter-1]
            if improvement<treshold:
                print("Gradient descent terminating after %s iterations. cost hasn't improved." % iter)
                break
        iter += 1
    if iter >= max_iter:
        print("Gradient descent terminating after %s iterations (max_iter)" % iter)
    elif improvement>=treshold:
        print("Gradient descent terminating after %s iterations. Improvement was : %f – below threshold (%d)" % iter, improvement, treshold )

    return [hypothesis, cost_j]

    