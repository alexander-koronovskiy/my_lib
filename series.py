"""
pandas DataFrame time series

load methods from file path or functions generator:
linear, power func, harmonic, noise, log map
and solution of differential equation
"""

import pandas as pd
import numpy as np
import random
from diff_module import solver


def diff_sol(t, f, pt=1000, dt=0.02):
    """
    method of differential equation solution
    use: "generator='diff_sol', :params" in () load_series

    :param t: initial conditions [x0, x1,.., xn]
    :param f: diff equations [f_1, f_2,.., f_n]
    :param pt: points number
    :param dt: Runge-Kutta step
    :return: DataFrame [F_1, F_2,.., F_n] - solution of diff eq
    """
    size = len(f)
    res = []
    t0 = []
    for i in range(pt):
        t0.append(i * dt)
        t = solver.rk4(t, f, size, dt)
        res.append([t[j] for j in range(len(t))])
    res = pd.DataFrame(res)
    t0 = pd.DataFrame(t0)
    res.columns = [j + 1 for j in range(len(t))]
    return t0.join(res)


def linear(t0=0, t1=10, a=1, b=0, points=1000):
    """
    method of linear function build
    use "generator='linear', :params" in () load_series

    :param t0: start point
    :param t1: end point
    :param a: coefficient before t
    :param b: additional coefficient
    :param points: points number
    :return: pandas DataFrame ['t','u'] - points of linear func u=a*t+b
    """
    t = np.linspace(t0, t1, points)
    u = a*t + b
    return pd.DataFrame(data={
        't': t,
        'u': u
    })


def nonlinear(t0=0, t1=10, a=1, b=0, c=0, n=3, points=1000):
    """
    method of nonlinear function build
    use "generator='nonlinear', :params" in () load_series

    :param t0: start point
    :param t1: end point
    :param a: coefficient before t
    :param b: additional coefficient within (a*t + b)^n
    :param c: additional coefficient after (a*t + b)^n + c
    :param n: polynomial power
    :param points: points number
    :return: pandas DataFrame ['t','u'] - nonlinear func u=a*(t+b)^n+c
    """
    t = np.linspace(t0, t1, points)
    u = a*(t + b)**n + c
    return pd.DataFrame(data={
        't': t,
        'u': u
    })


def harmonic(t0=0, t1=10, a=1, omega=1, theta=0, points=1000):
    """
    method of harmonic function build
    use "generator='harmonic', :params" in () load_series

    :param t0: start point
    :param t1: end point
    :param a: oscillation amplitude
    :param omega: coefficient before t
    :param theta: initial phase
    :param points: points number
    :return: pandas DataFrame ['t','u'] - points of harmonic func u = a*cos(omega*t+theta)
    """
    t = np.linspace(t0, t1, points)
    u = a*np.cos(omega*t + theta)
    return pd.DataFrame(data={
        't': t,
        'u': u
    })


def do_map(u=[0.1], r=4, points=1000):
    """
    method of logistic map build
    use "generator='do_map', :params" in () load_series

    :param u: init conditional [u0]
    :param r: with velocity param
    :param points: points number
    :return: pandas DataFrame ['t','u'] - points of logistic map
    """
    t = np.linspace(0, points-1, points)
    for i in range(points):
        u.append(log_map(u[i], r))
    return pd.DataFrame(data={
        't': t,
        'u': u[:-1]
    })


def log_map(x, r):
    return r * x * (1 - x)


def noise_gen(amp=1, type='white', pt=1000):
    """
    method of noise series generation
    use "generator='harmonic', :params" in () load_series

    :param amp: series amplitude
    :param type: different types of noise series - white, red, purple
    :param pt: points number
    :return: pandas DataFrame ['t','u'] - noise series
    """
    def smoother(noise):
        if type == 'red':
            output = [0.5 * (noise[i] + noise[i + 1]) for i in range(len(noise) - 1)]
        elif type == 'purple':
            output = [0.5 * (noise[i] - noise[i + 1]) for i in range(len(noise) - 1)]
        else:
            output = noise[:-1]
        return output

    t = [i for i in range(pt - 1)]
    noise = [random.uniform(-amp, +amp) for i in range(pt)]
    return pd.DataFrame(data={
        't': t,
        'u': smoother(noise)
    })


SERIES = {
    'linear': linear,
    'nonlinear': nonlinear,
    'harmonic': harmonic,
    'do_map': do_map,
    'noise_gen': noise_gen,
    'diff_sol': diff_sol,
}


def load_series(path=None, generator=None, **kwargs):
    """
    series generator from file path or function
    from module series use series.load_series()

    :param path: loading series from file
    :param generator: function generator call
    :param kwargs: function :params call
    :return: pandas DataFrame loaded from function or file
    """
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
        with open(path) as file:
            data = pd.DataFrame([line.split() for line in file], dtype='float64')
        return data
        # pd.read_csv(path, sep=' ')
    else:
        raise RuntimeError('You should set either path or generator!')
