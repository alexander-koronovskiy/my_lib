'''
методы вывода обработанных временных рядов
сохранение получившихся датафреймов результатов файл (в отдельной директории)
изображение при запуске, в т.ч. трехмерное
сохранение изображений в отдельной директории
'''

import load, processing
import matplotlib.pyplot as plt

s = load.load_series(generator='noised_linear', x0=2, x1=5, points=100, noise_amp=0.02)
plt.plot(s[s.columns[0]], s[s.columns[1]]); plt.show()
print(s)
