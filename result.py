import series as s
import processing as p
import matplotlib.pyplot as plt

# test signal
df2 = s.load_series(generator='noise_gen', amp=1, pt=1000, type='')
df3 = s.load_series(generator='noise_gen', amp=1, pt=1000, type='')

df = df2.append(df3)\
    .reset_index()\
    .drop(columns=['t', 'index'])

# processing
df = p.process(function='compute_profile', df=df)
res = p.process(function='dfa1', df=df, input_col='profile', q=3)

# visualisation
plt.plot(res['output_lags'], res['output_dfa'],
         res['output_lags'], res['output_dfa_ext'])
plt.show()
