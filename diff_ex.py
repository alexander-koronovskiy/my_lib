import numpy as np


# Equation System
def f_x(x):
    return 2*x[0] + x[1]
def f_y(x):
    return 3*x[0] + x[2]*np.exp(x[2])
def f_t(x):
    return x[2]
