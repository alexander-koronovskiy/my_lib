import series as s, processing as p
from diff_module.lorenz_attr import *

# load series
ds = s.load_series(generator='diff_sol',
                   t=[1, 1, 0, 0.1, 0.1, 0.1],
                   f=[f_x, f_y, f_z, f_u, f_v, f_w],
                   pt=1000,
                   dt=0.02)

ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

s_noise = s.load_series(generator='w_noise')
signal = ds[['t']].join(s_noise[['u']]*ds[['u']])

# series processing
profile_u = p.process(function='profile',
                      df=signal,
                      input_col='u',
                      output_col='profile')

dfa1 = p.process(function='dfa1',
                 df=profile_u,
                 input_col='profile',
                 lags_col='dfa_lags',
                 dfa_col='dfa')

p.process(function='compare_graphics',
          df=dfa1,
          first_col='profile',
          second_col='dfa_lags',
          third_col='dfa')
