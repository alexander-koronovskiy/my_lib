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
def do_profile(df):
    # возврат 2й колонки датафрейма
    # возврат профиля датафрейма в формате df
    return df.head()


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


PROCESSING = {'profile': do_profile,
              'approx': approx,
              'sync_phase': sync_phase,
              'fourier': fourier,
              'akf': akf,
              'dfa1': dfa1,
              'dfa3': dfa3,
}


def do_processing(handler=None, **kwargs):
    if handler is not None:
        # handler
        if isinstance(handler, str):
            # get handler function and call it
            f = PROCESSING.get(handler)
            if f is None:
                raise RuntimeError(f'No such generator: {handler}')
            return f(**kwargs)
        elif callable(handler):
            # call handler
            return handler(**kwargs)
        else:
            raise RuntimeError(f'This type of generator is not supported: {type(handler)}')
    else:
        raise RuntimeError('You should set either path or generator!')
