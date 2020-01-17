import series as s, processing as p
import os

# access for all time series in the folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
folder = '/neph'
s_files = os.listdir(BASE_DIR + folder)

for i in range(len(s_files)):

    # access for origin file
    series = s.load_series(path=BASE_DIR + folder + '/' + s_files[i])
    series_name = s_files[i][:-4]

    # series profile build
    series.columns = ['t', 'u', 'v', 'w']
    series = p.process(function='compute_profile',
                       df=series,
                       input_col='w',
                       output_col='profile')

    # series dfa build
    arr_q = [0, 1, 2, 3, 5]
    for j in arr_q:
        series = p.process(function='dfa1',
                           df=series,
                           q=j,
                           input_col='profile',
                           dfa_col='q=' + str(j),
                           lags_col='lags')

    # save results
    p.process(function='save_dfa_graphics',
              df=series,
              orig_col='u',
              profile_col='profile',
              dfa_l_col='lags',
              dfa_f_col=['q='+str(j) for j in arr_q],
              series_name=BASE_DIR + folder + '_result/4_col_' + series_name)

    p.process(function='save_df',
              df=series,
              series_name=BASE_DIR + folder + '_result/4_col_' + series_name)
