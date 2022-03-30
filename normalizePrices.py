#Part 2
import numpy as np


def normalizePrices(D):
    updatedPrices = np.array(D[:,0]/1000)
    devicesAge = np.array(D[:,1])  
    devicesAge = np.reshape(devicesAge, np.size(devicesAge,0)) #force same dimensions
    return np.column_stack((updatedPrices, devicesAge))
     
#Part 2 helper
def addOnesColumn(D):
    newCol = np.ones((np.size(D,0),1))
    return np.hstack((newCol, D))