import os
from matplotlib import pyplot as plt
import numpy as np
from gradientDescent import gradientDescent



def main():
    filename = input("please enter a file name ")
    if not os.path.isfile(filename):
        filename = 'smartphone.txt'
    [FinalHypothesis, Costs] = gradientDescent(filename, 0.1, 1000,  0.001)
    #graphs presentation
    iterations = np.arange(len(Costs))
    print(iterations)
    plt.plot(iterations, Costs, ls= '', marker = 'o')
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.show()


main()