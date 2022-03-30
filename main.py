from matplotlib import pyplot as plt
import numpy as np
from computeCost import computeCost
from computeErrors import computeErrors
from computeGradient import computeGradient
from loadData import loadData

from normalizePrices import addOnesColumn, normalizePrices


def main():
    [D, Y] = loadData('smartphone.txt')
    for i in range(np.size(D,1)):   #graphs presentation
        plt.plot(D[:,i], Y, ls= '', marker = 'o')
        plt.xlabel(featuresSet[i])
        plt.ylabel(predictLabel)
    #    plt.show()
    D = normalizePrices(D)
    D = addOnesColumn(D)
    errors = computeErrors(D, Y, np.zeros((np.size(D,0),1),dtype=np.float64))
    cost = computeCost(D, Y, np.zeros(3))
    gradient = computeGradient(D, errors)
    print("gradient- %s" % gradient)    


featuresSet = ["Original Price (ns)", "Device Age (y)"]
predictLabel = "Updated Price"
main()