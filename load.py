import pandas as pd
import numpy as np
import diff_eq_series as ds


# use "generator=linear, x0=start, x1=end, a=,b=, points=" in () load_series
def linear(x0=0, x1=10, a=1, b=0, points=100):
    x = np.linspace(x0, x1, points)
    y = a*x + b
    return pd.DataFrame(data={
        'x': x,
        'y': y
    })


# use "generator=nonlinear, x0=start, x1=end, a=,b=,c=,n=, points=" in () load_series
def nonlinear(x0=0, x1=10, a=1, b=0, c=0, n=3, points=100):
    x = np.linspace(x0, x1, points)
    y = a*(x + b)**n + c
    return pd.DataFrame(data={
        'x': x,
        'y': y
    })


SIGNALS = {
    'linear': linear,
    'nonlinear': nonlinear,
    'lorenz': ds.attr_lorenz,
}


def load_series(path=None, generator=None, **kwargs):
    if generator is not None:
        # generation
        if isinstance(generator, str):
            # get generator function and call it
            f = SIGNALS.get(generator)
            if f is None:
                raise RuntimeError(f'No such generator: {generator}')
            return f(**kwargs)
        elif callable(generator):
            # call generator
            return generator(**kwargs)
        else:
            raise RuntimeError(f'This type of generator is not supported: {type(generator)}')
    elif path is not None:
        return pd.read_csv(path, sep=' ')
    else:
        raise RuntimeError('You should set either path or generator!')
