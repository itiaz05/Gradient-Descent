import os
from matplotlib import pyplot as plt
import numpy as np
from gradientDescent import gradientDescent



def main():
    #filename = input("please enter a file name ")
    #if not os.path.isfile(filename):
    filename = 'smartphone.txt'
    alpha = 0.5
    alphaList = []
    hypothesisList = []
    costsList = []
    iter = 0
    iterList = 0
    while True:
        [FinalHypothesis, Costs] = gradientDescent(filename, alpha, 1000,  0.001)
        alphaList.append(alpha)
        costsList.append(Costs[len(Costs)-1])
        hypothesisList.append(FinalHypothesis)
        iter += 1
        alpha -= 0.05
        if iter >= 500:
            break
    
    #graphs presentation
    #iterations = np.arange(len(Costs))
    #plt.plot(iterations, Costs, ls= '', marker = 'o')
    #plt.xlabel("Iteration")
    #plt.ylabel("Cost")
    #plt.show()


main()