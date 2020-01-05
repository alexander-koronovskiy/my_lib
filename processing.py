import numpy as np
'''
методы обработки временных рядов такие как:
построение профиля, аппроксимация (на n - участках, a - степень)
построение фаз системы, фурье-преобразования, АКФ
корреляционный DFA I - датафрейм результата, и его апроксимации
мультифрактальный спектр (DFA III) - датафрейм результата
'''


def do_profile(array):
    p_array = []
    sr = np.mean(array)
    for i in range(len(array)):
        y_array = []
        for j in range(i):
            y_array.append(array[j] - sr)
        p_array.append(sum(y_array))
    return p_array
