def min_max(x):
    import numpy as np
    z= x-np.min(x)/(np.max(x)-min(x))
    return z
   


