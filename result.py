import series as s, processing as p
from diff_module.lorenz_attr import *

# load series
ds = s.load_series(generator='diff_sol',
                   t=[1, 1, 0, 0.1, 0.1, 0.1],
                   f=[f_x, f_y, f_z, f_u, f_v, f_w],
                   pt=1000,
                   dt=0.02)

ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

# series processing
profile_u = p.process(function='profile',
                      df=ds,
                      input_col='u',
                      output_col='profile_u')

result = p.process(function='approx',
                   df=profile_u,
                   n=3,
                   input_col='profile_u',
                   output_col='approx_profile_u')

p.process(function='compare_graphs',
          df=result,
          first_col='u',
          second_col='profile_u')

# test docstrings
print(s.__doc__)
print(s.diff_sol.__doc__)
print(p.compute_profile.__doc__)
