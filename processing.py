import numpy as np
import matplotlib.pyplot as plt
'''
методы обработки временных рядов такие как:
построение профиля, аппроксимация (на n - участках, a - степень)
фаз синхронизации, фурье-преобразования, АКФ, фильтрации по величине
корреляционный DFA I - датафрейм результата, и его апроксимации
мультифрактальный спектр (DFA III) - датафрейм результата
сохранение датафреймов файл (в отдельной директории)
изображение дф при запуске, в т.ч. трехмерное
сохранение изображений в отдельной директории
'''


# use "function=profile, df=, input_col=, output_col=" in () do_processing
# returns extended pandas DataFrame
# integration of the input_col on output_col
def integrate(df, input_col='u', output_col='profile_u'):
    df[output_col] = (df[input_col]).cumsum()
    return df


# use "function=profile, df=, input_col=, output_col=" in () do_processing
# returns extended pandas DataFrame
# integration without mean of the input_col on output_col
def compute_profile(df, input_col='u', output_col='profile_u'):
    df[output_col] = (df[input_col] - df[input_col].mean()).cumsum()
    return df


# use "function=approx, df=, n=, input_col=, output_col=" in () do_processing
# returns extended pandas DataFrame
# n-order approximation of the input_col on output_col
def approx(df, n=1, input_col='u', output_col='approx_u'):
    t = np.linspace(0.1, 10, len(df[input_col]))
    p = np.polyfit(t, df[input_col], n)
    df[output_col] = np.polyval(p, t)
    return df


def akf():
    pass


def dfa1():
    pass


def dfa3():
    pass


def sync_phase():
    pass


def fourier():
    pass


# use "function=compare_graphs, first_col=, second_col=" in () do_processing
# compare 2 plots in one fig: of the one column in dataframe and another
def compare_graphs(df, first_col, second_col, title1='in', title2='out'):
    f, a = plt.subplots(1, 2)
    a[0].plot(df[first_col])
    a[0].set_title(title1)
    a[1].plot(df[second_col])
    a[1].set_title(title2)
    plt.show()


FUNCTIONS = {
    'integrate': integrate,
    'profile': compute_profile,
    'approx': approx,
    'akf': akf,
    'dfa1': dfa1,
    'dfa3': dfa3,
    'sync_phase': sync_phase,
    'fourier': fourier,
    'compare_graphs': compare_graphs,
}


def process(function=None, **kwargs):
    if function is not None:
        # handler
        if isinstance(function, str):
            # get handler function and call it
            f = FUNCTIONS.get(function)
            if f is None:
                raise RuntimeError(f'No such generator: {function}')
            return f(**kwargs)
        elif callable(function):
            # call handler
            return function(**kwargs)
        else:
            raise RuntimeError(f'This type of generator is not supported: {type(function)}')
    else:
        raise RuntimeError('You should set handler!')
