import matplotlib.pyplot as plt, numpy as np
import series as s, processing as p
'''
методы вывода обработанных временных рядов
сохранение получившихся датафреймов результатов файл (в отдельной директории)
изображение при запуске, в т.ч. трехмерное
сохранение изображений в отдельной директории
'''

# загрузка сигналов
ds = s.load_series(generator='diff_sol')
ds.columns = ['t', 'x', 'y', 'z', 'u', 'v', 'w']
l_r = 'v'

noise_series = s.load_series(generator='w_noise', amp=0.2)
noise_series.columns = ['t', l_r]

line_series = s.load_series(generator='harmonic', x0=0, x1=10)
line_series.columns = ['t', l_r]


# пример получения сложного сигнала
signal = ds[['t']].join(ds[[l_r]] * line_series[[l_r]] * noise_series[[l_r]])


# пример обработки сигналов
result = p.do_processing(handler='profile', df=signal)
print(result)

print(f'\nnumber of points: {len(signal)}\n{signal.head()}')
plt.plot(signal[['t']], signal[[l_r]]); plt.show()
