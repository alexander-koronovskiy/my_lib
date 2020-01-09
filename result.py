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

line_series = s.load_series(generator='linear', t0=0, t1=10)
line_series.columns = ['t', l_r]


# пример обработки сигналов
result = p.do_processing(handler='profile', df=ds)
print(result.head())

plt.plot(result); plt.show()
