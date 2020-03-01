import series as s
import processing as p
import numpy as np

# test signal
tp = 'white'
df = s.load_series(generator='noise_gen', amp=1, pt=2000, type=tp).drop(columns='t')
df.to_csv('input/' + tp + '.txt', sep=' ', index=0)

# save signal and profile
df = p.process(function='compute_profile', df=df)
p.process(function='series_fig', df=df, name='input/' + tp)

# dfa build
alpha = []
alpha_ext = []
for i in range(6):
    df = p.process(function='dfa1', df=df, input_col='profile', q=i,
                   l_lags=[10, 20, 40, 80, 160],
                   dfa_col='dfa_'+str(i), ext_col='dfa_ext_'+str(i))
    alpha.append(np.polyfit(df['output_lags'][:5], df['dfa_'+str(i)][:5], 1)[0])
    alpha_ext.append(np.polyfit(df['output_lags'][:5], df['dfa_ext_' + str(i)][:5], 1)[0])

# saving result
p.process(function='save_dfa_graphics', df=df,
          st_dfa=alpha, ext_dfa=alpha_ext, name='output/dfa_' + tp)
df.to_csv('output/dfa_' + tp + '.txt', sep=' ', index=0)
