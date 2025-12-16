import numpy as np
from preprocess.minmaxscaler import min_max
from preprocess.standardscaler import stdscale

def main():
    x = np.array([1, 2, 3, 4, 5])
    z_minmax = min_max(x)
    z_std = stdscale(x)

    print("Original:", x)
    print("Min-max scaled:", z_minmax)
    print("Standard scaled:", z_std)

if __name__ == "__main__":
    main()


