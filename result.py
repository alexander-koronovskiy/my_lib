import series as s, processing as p
from diff_module.lorenz_attr import *
import os

# access for all time series in the dir
ns_files = os.listdir(os.path.dirname(__file__) + '/neph')

# load files
series = s.load_series(path='neph/' + ns_files[0])
series.columns = ['t', 'u', 'v', 'w']

# series processing
series = p.process(function='compute_profile',
                   df=series,
                   input_col='u',
                   output_col='profile')

series = p.process(function='dfa1',
                   df=series,
                   input_col='profile',
                   lags_col='dfa',
                   dfa_col='lags')

p.process(function='compare_graphics',
          df=series,
          orig_col='u',
          profile_col='profile',
          dfa_l_col='lags',
          dfa_f_col='dfa')
