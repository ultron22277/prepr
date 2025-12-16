def stdscale(v):
    import numpy as np
    u=(v-np.mean(v))/(np.std(v))
    return u


