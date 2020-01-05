'''
методы загрузки временного ряда по указанному пути из файла
или генерация временного ряда на основе
загружаемых в словарь методов, с помощью функций:
линейной, степенной, гармонической, зашумленных данных,
трансцединтальных (логарифм, экспонента, тангенс)
лог.отображений, а также полученных на основе решений дифф.ур.
с документацией по вызову параметров генератора
'''

import pandas as pd
import numpy as np

# for the differential equations solutions
from diff_module import solver
from diff_module.lorenz_attr import *


# use "generator=diff_sol, x=[], f=[], pt=, dx=" in () load_series
def diff_sol(x=[1, 1, 0, 0.1, 0.1, 0.1], f=[f_x, f_y, f_z, f_u, f_v, f_w], pt=1000, dx=0.02):
    size = len(f)
    res = []
    t0 = []
    for i in range(pt):
        x = solver.rk4(x, f, size, dx)
        t0.append(i*dx)
        res.append([x[j] for j in range(len(x))])
    res = pd.DataFrame(res)
    res.columns = [j + 1 for j in range(len(x))]
    t0 = pd.DataFrame(t0)
    return t0.join(res)


# use "generator=linear, x0=start, x1=end, a=,b=, points=" in () load_series
def linear(x0=0, x1=10, a=1, b=0, points=1000):
    x = np.linspace(x0, x1, points)
    y = a*x + b
    return pd.DataFrame(data={
        'x': x,
        'y': y
    })


# use "generator=nonlinear, x0=start, x1=end, a=,b=,c=,n=, points=" in () load_series
def nonlinear(x0=0, x1=10, a=1, b=0, c=0, n=3, points=1000):
    x = np.linspace(x0, x1, points)
    y = a*(x + b)**n + c
    return pd.DataFrame(data={
        'x': x,
        'y': y
    })


# use "generator=harmonic, x0=start, x1=end, a=, omega=, t0=" in () load_series
def harmonic(x0=0, x1=100, a=1, omega=1, t0=0, points=1000):
    x = np.linspace(x0, x1, points)
    y = a*np.cos(omega*x + t0)
    return pd.DataFrame(data={
        'x': x,
        'y': y
    })


# use "x_arr=[], r=, points=" in () load_series
def do_map(x_arr=[0.1], r=4, points=1000):
    x = np.linspace(0, points-1, points)
    for i in range(points):
        x_arr.append(log_map(x_arr[i], r))
    return pd.DataFrame(data={
        'x': x,
        'y': x_arr[:-1]
    })


def log_map(x, r):
    return r * x * (1 - x)


# use "generator=add_noise, df=, amp=" in () load_series
def add_noise(df=linear(), amp=0.025):
    db = amp*(max(df[df.columns[1]].values) - min(df[df.columns[1]].values))
    noised = np.random.normal(0, db, df[df.columns[1]].values.shape)
    return df[[0]].join(pd.DataFrame(noised + df[df.columns[1]]))


SERIES = {
    'linear': linear,
    'nonlinear': nonlinear,
    'harmonic': harmonic,
    'do_map': do_map,
    'add_noise': add_noise,
    'diff_sol': diff_sol,
}


def load_series(path=None, generator=None, **kwargs):
    if generator is not None:
        # generation
        if isinstance(generator, str):
            # get generator function and call it
            f = SERIES.get(generator)
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
