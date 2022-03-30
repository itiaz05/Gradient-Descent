#Part 3
import numpy as np


def predicatedValue(Example, Hypothesis):
    return np.sum(Example * Hypothesis)