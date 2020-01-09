import pandas as pd
import numpy as np
from diff_module import solver
from diff_module.lorenz_attr import *
'''
методы загрузки временного ряда по указанному пути из файла
или генерация временного ряда на основе
загружаемых в словарь методов, с помощью функций:
линейной, степенной, гармонической, шума, лог.отображений, 
а также полученных на основе решений дифф.ур.
с документацией по вызову параметров генератора
'''


# use "generator=diff_sol, x=[], f=[], pt=, dx=" in () load_series
# returns pandas DataFrame
def diff_sol(x=[1, 1, 0, 0.1, 0.1, 0.1], f=[f_x, f_y, f_z, f_u, f_v, f_w], pt=1000, dx=0.02):
    size = len(f)
    res = []
    t0 = []
    for i in range(pt):
        t0.append(i * dx)
        x = solver.rk4(x, f, size, dx)
        res.append([x[j] for j in range(len(x))])
    res = pd.DataFrame(res)
    t0 = pd.DataFrame(t0)
    res.columns = [j + 1 for j in range(len(x))]
    return t0.join(res)


# use "generator=linear, t0=start, t1=end, a=,b=, points=" in () load_series
# returns pandas DataFrame
def linear(t0=0, t1=10, a=1, b=0, points=1000):
    t = np.linspace(t0, t1, points)
    x = a*t + b
    return pd.DataFrame(data={
        't': t,
        'x': x
    })


# use "generator=nonlinear, t0=start, t1=end, a=,b=,c=,n=, points=" in () load_series
# returns pandas DataFrame
def nonlinear(t0=0, t1=10, a=1, b=0, c=0, n=3, points=1000):
    t = np.linspace(t0, t1, points)
    x = a*(t + b)**n + c
    return pd.DataFrame(data={
        't': t,
        'x': x
    })


# use "generator=harmonic, t0=start, t1=end, a=, omega=, t0=" in () load_series
# returns pandas DataFrame
def harmonic(t0=0, t1=10, a=1, omega=1, theta=0, points=1000):
    t = np.linspace(t0, t1, points)
    x = a*np.cos(omega*t + t0)
    return pd.DataFrame(data={
        't': t,
        'x': x
    })


# use "generator=do_map, x_arr=[], r=, points=" in () load_series
# returns pandas DataFrame
def do_map(x_arr=[0.1], r=4, points=1000):
    t = np.linspace(0, points-1, points)
    for i in range(points):
        x_arr.append(log_map(x_arr[i], r))
    return pd.DataFrame(data={
        't': t,
        'x': x_arr[:-1]
    })


def log_map(x, r):
    return r * x * (1 - x)


# use "generator=w_noise, r=, points=" in () load_series
# returns pandas DataFrame
def w_noise(mean=0, std=1, amp=1, points=1000):
    t = np.linspace(0, points - 1, points)
    x_arr = amp*np.random.normal(mean, std, size=points)
    return pd.DataFrame(data={
        't': t,
        'x': x_arr
    })


SERIES = {
    'linear': linear,
    'nonlinear': nonlinear,
    'harmonic': harmonic,
    'do_map': do_map,
    'w_noise': w_noise,
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
