import pandas as pd
import random
import matplotlib.pyplot as plt


def noise_gen(amp=1, type='white', pt=1000):
    def smoother(noise):
        if type == 'red':
            output = [0.5 * (noise[i] + noise[i + 1]) for i in range(len(noise) - 1)]
        elif type == 'purple':
            output = [0.5 * (noise[i] - noise[i + 1]) for i in range(len(noise) - 1)]
        else:
            output = noise
        return output

    t = [i for i in range(pt - 1)]
    noise = [random.uniform(-amp, +amp) for i in range(pt)]
    white = noise
    print(type)
    return pd.DataFrame(data={
        't': t,
        'u': smoother(noise)
    })


df2 = noise_gen(1, 'red')
df3 = noise_gen(1, 'purple')

df = df2.append(df3)\
    .reset_index()\
    .drop(columns=['t', 'index'])

plt.plot(df)
plt.show()
