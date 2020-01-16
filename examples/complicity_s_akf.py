"""
complex signal generation and processing
"""

import series as s, processing as p
from diff_module.lorenz_attr import *
import matplotlib.pyplot as plt

# signal generation
ds = s.load_series(generator='diff_sol',
                   t=[1, 1, 1, 0.1, 0.1, 0.1],
                   f=[f_x, f_y, f_z, f_u, f_v, f_w])
ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

n_series = s.load_series(generator='do_map')
n_series.columns = ['t', 'u']

l_series = s.load_series(generator='harmonic')
l_series.columns = ['t', 'u']

# new series receiving
ds['result'] = ds['u'] * n_series['u'] * l_series['u']

# akf calculation
ds = p.process(function='akf',
               df=ds,
               input_col='result',
               lags=200)

# visualisation
plt.plot(ds['akf'])
plt.title('complex signal akf')
plt.show()
