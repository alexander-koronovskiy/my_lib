import pandas as pd
import numpy as np
'''
методы обработки временных рядов такие как:
построение профиля, аппроксимация (на n - участках, a - степень)
фаз синхронизации, фурье-преобразования, АКФ, фильтрации по величине
корреляционный DFA I - датафрейм результата, и его апроксимации
мультифрактальный спектр (DFA III) - датафрейм результата
'''


# use "handler=profile, df=" in () do_processing
# returns pandas DataFrame
def compute_profile(df, input_col='u', output_col='profile'):
    df[output_col] = (df[input_col] - df[input_col].mean()).cumsum()
    return df


# use "df=, n=" in () do_processing
# returns pandas DataFrame
def approx():
    pass


def sync_phase():
    pass


def fourier():
    pass


def akf():
    pass


def dfa1():
    pass


def dfa3():
    pass


FUNCTIONS = {
    'profile': compute_profile,
    'approx': approx,
    'sync_phase': sync_phase,
    'fourier': fourier,
    'akf': akf,
    'dfa1': dfa1,
    'dfa3': dfa3,
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
