import load
import matplotlib.pyplot as plt
from diff_ex import *

s = load.load_series(generator='diff_sol', x=[0.1, 0.2, 0.7], f=[f_x, f_y, f_t], pt=1000, dx=0.001)
plt.plot(s); plt.show()
