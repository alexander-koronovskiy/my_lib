import series as s
import processing as p
import numpy as np

# rewriting ../
tp = 'open'
df1 = s.load_series(path='series/' + tp + '.txt')[::100]
df1.to_csv('series/' + tp + '_mod.txt', sep=' ', index=0)

# load
df = s.load_series(path='series/' + tp + '_mod.txt')
df.columns = ['u']

# save signal and profile
df = p.process(function='compute_profile', df=df)
p.process(function='series_fig', df=df, name='output/' + tp)

# dfa build
alpha = []
alpha_ext = []
for i in range(1, 2):
    df = p.process(function='dfa1', df=df, input_col='profile', q=i,
                   l_lags=[25, 50, 100, 500, 1000],
                   dfa_col='dfa_'+str(i), ext_col='dfa_ext_'+str(i))
    alpha.append(round(np.polyfit(df['output_lags'][:5], df['dfa_'+str(i)][:5], 1)[0], 2))
    alpha_ext.append(round(np.polyfit(df['output_lags'][:5], df['dfa_ext_' + str(i)][:5], 1)[0], 2))

# saving result
p.process(function='save_dfa_graphics', df=df,
          st_dfa=alpha[0], ext_dfa=alpha_ext[0], name='output/dfa_' + tp)
df.to_csv('output/dfa_' + tp + '.txt', sep=' ', index=0)
