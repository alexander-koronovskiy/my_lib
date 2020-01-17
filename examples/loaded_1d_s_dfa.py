"""
de-trending fluctuation analysis for loaded signal
"""

import series as s, processing as p
import os

# access for all time series in the folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
folder = '/neph_filtr'
s_files = os.listdir(BASE_DIR + folder)

# access for origin file
series = s.load_series(path=BASE_DIR + folder + '/' + s_files[1])
series_name = s_files[1][:-4]

# series processing
series.columns = ['u']
series = p.process(function='compute_profile',
                   df=series,
                   input_col='u',
                   output_col='profile')

arr_q = [0, 1, 2, 3, 5]
for i in arr_q:
    series = p.process(function='dfa1',
                       df=series,
                       q=i,
                       l_lags=[2, 4, 5, 10, 15],
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
          series_name=series_name)
