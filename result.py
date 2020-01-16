import series as s, processing as p
import os

# access for all time series in the folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
s_files = os.listdir(BASE_DIR + '/neph')
series = s.load_series(path='neph/' + s_files[1])

# series processing
series.columns = ['t', 'u', 'v', 'w']
series = p.process(function='compute_profile',
                   df=series,
                   input_col='u',
                   output_col='profile')

arr_q = [0, 1, 2, 3, 5]
for i in arr_q:
    series = p.process(function='dfa1',
                       df=series,
                       q=i,
                       input_col='profile',
                       dfa_col='q=' + str(i),
                       lags_col='lags')

p.process(function='compare_graphics',
          df=series,
          orig_col='u',
          profile_col='profile',
          dfa_l_col='lags',
          dfa_f_col=['q='+str(j) for j in arr_q])
