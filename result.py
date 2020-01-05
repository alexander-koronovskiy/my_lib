import matplotlib.pyplot as plt, numpy as np
import load as load, processing
'''
методы вывода обработанных временных рядов
сохранение получившихся датафреймов результатов файл (в отдельной директории)
изображение при запуске, в т.ч. трехмерное
сохранение изображений в отдельной директории
'''

# загрузка сигналов
ds = load.load_series(generator='diff_sol')
ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']

series1 = load.load_series(generator='w_noise', amp=1)
series1.columns = ['t', 'x']

series2 = load.load_series(generator='harmonic', x0=0, x1=10)
series2.columns = ['t', 'x']


# пример сложения сигналов
signal = ds[['t']].join(series1[['x']]*ds[['x']])


# финальная обработка сигналов
print(f'\nnumber of points: {len(signal)}\n{signal.head()}')
plt.plot(signal[['t']], signal[['x']])
plt.show()
