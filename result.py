import matplotlib.pyplot as plt
import series as s, processing as p

# загрузка сигналов
ds = s.load_series(generator='diff_sol')
ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

# пример обработки сигналов
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

plt.plot(result[['profile_u', 'approx_profile_u']]); plt.show()
