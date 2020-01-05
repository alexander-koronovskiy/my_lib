'''
методы вывода обработанных временных рядов
сохранение получившихся датафреймов результатов файл (в отдельной директории)
изображение при запуске, в т.ч. трехмерное
сохранение изображений в отдельной директории
'''

import matplotlib.pyplot as plt, numpy as np
import load as load, processing


x = load.load_series(generator='diff_sol')[[0, 1]]
signal = load.load_series(generator='add_noise', df=x, amp=0.02)
plt.plot(signal[[1]]); plt.show()
