import series as s
import processing as p
import numpy as np
import matplotlib.pyplot as plt

# test signal
df2 = s.load_series(generator='noise_gen', amp=1, pt=1000, type='')
df3 = s.load_series(generator='noise_gen', amp=1, pt=1000, type='')

df = df2.append(df3)\
    .reset_index()\
    .drop(columns=['t', 'index'])

# processing
df = p.process(function='compute_profile', df=df)

for i in range(5):
    df = p.process(function='dfa1', df=df, input_col='profile', q=i, l_lags=[3, 10, 30, 100, 300],
                   dfa_col='dfa_'+str(i), ext_col='dfa_ext_'+str(i))

alpha = np.polyfit(df['output_lags'][:5], df['dfa_1'][:5], 1)[0]
print(alpha)

# visualisation
plt.plot(df['output_lags'], df['dfa_1'],
         df['output_lags'], df['dfa_2'],
         df['output_lags'], df['dfa_3'],
         df['output_lags'], df['dfa_4'])
plt.show()
