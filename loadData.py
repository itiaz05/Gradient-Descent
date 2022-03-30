import numpy as np

#Part 1
def loadData(filename):
    D = np.genfromtxt(filename)
    rows = "problem reading file"   #avoid uninitialized var
    try:
        lastCol = np.size(D,1)-1 #index of last column
        Y = D[:,lastCol]    #Y is the predicated values
        B = D[:,0:lastCol]
        rows = np.size(D,0)
    finally:
     print("read %s rows" % rows)
    return [B, Y]

