import numpy as np
from matplotlib import pyplot as plt

featuresSet = ["Original Price (ns)", "Device Age (y)"]
predictLabel = "Updated Price"

#Part 1
def loadData(filename):
    D = np.genfromtxt(filename)
    rows = "problem reading file"   #avoid uninitialized var
    try:
        lastCol = np.size(D,1)-1 #index of last column
        Y = D[:,lastCol]    #Y is the predicated values
        B = D[:,0:lastCol]
        rows = np.size(D,0)
        for i in range(np.size(D,1)-1):   #graphs presentation
            plt.plot(D[:,i], Y, ls= '', marker = 'o')
            plt.xlabel(featuresSet[i])
            plt.ylabel(predictLabel)
        #    plt.show()
        
    finally:
     print("read %s rows" % rows)
    return [B, Y]

