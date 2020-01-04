import load
import matplotlib.pyplot as plt
from diff_ex import *

s = load.load_series(generator='diff_sol', x=[1, -0.2, -0.15], f=[f_x, f_y, f_t], pt=2000, dx=0.05)
plt.plot(s); plt.show()
