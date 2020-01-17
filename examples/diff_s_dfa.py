"""
de-trending fluctuation analysis for generated signal
"""

import series as s, processing as p
from diff_module.lorenz_attr import *

# signal generation
ds = s.load_series(generator='diff_sol',
                   t=[1, 1, 1, 0.1, 0.1, 0.1],
                   f=[f_x, f_y, f_z, f_u, f_v, f_w])
ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

# profile computing
series = p.process(function='compute_profile',
                   df=ds,
                   input_col='u',
                   output_col='profile')

# dfa
arr_q = [0, 1, 2, 3, 5]
for i in arr_q:
    series = p.process(function='dfa1',
                       df=series,
                       q=i,
                       l_lags=[5, 10, 20, 50, 100],
                       input_col='profile',
                       dfa_col='q=' + str(i),
                       lags_col='lags')

# visualisation
p.process(function='save_dfa_graphics',
          df=series,
          orig_col='u',
          profile_col='profile',
          dfa_l_col='lags',
          dfa_f_col=['q='+str(j) for j in arr_q],
          series_name='diff_sol')
