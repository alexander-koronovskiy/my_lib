"""
one-column dataframe
linear, nonlinear, harmonic and solution of differential equation
sequence are produced to aggregator
"""

import random

import numpy as np
import pandas as pd


def diff_sol(t, f, pt=1000, dt=0.02):
    """
    method of differential equation solution
    use: "generator='diff_sol', :params" in () load_series

    :param t: initial conditions [x0, x1,.., xn]
    :param f: diff equations [f_1, f_2,.., f_n]
    :param pt: rows number
    :param dt: Runge-Kutta step
    :return: DataFrame [F_1, F_2,.., F_n] - solution of diff eq
    """
    size = len(f)
    res = []
    t0 = []
    for i in range(pt):
        t0.append(i * dt)
        t = rk4(t, f, size, dt)
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
    u = a * t + b
    return pd.DataFrame(data={"u": u})


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
    u = a * (t + b) ** n + c
    return pd.DataFrame(data={"u": u})


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
    u = a * np.cos(omega * t + theta)
    return pd.DataFrame(data={"u": u})


def do_map(u=[0.1], r=4, points=1000):
    """
    method of logistic map build
    use "generator='do_map', :params" in () load_series

    :param u: init conditional [u0]
    :param r: with velocity param
    :param points: points number
    :return: pandas DataFrame ['t','u'] - points of logistic map
    """
    t = np.linspace(0, points - 1, points)
    for i in range(points):
        u.append(log_map(u[i], r))
    return pd.DataFrame(data={"u": u[:-1]})


def log_map(x, r):
    return r * x * (1 - x)


def noise_gen(amp=1, type="white", pt=1000):
    """
    method of noise series generation
    use "generator='harmonic', :params" in () load_series

    :param amp: series amplitude
    :param type: different types of noise series - white, red, purple
    :param pt: points number
    :return: pandas DataFrame ['t','u'] - noise series
    """

    def smoother(noise):
        if type == "red":
            output = [0.5 * (noise[i] + noise[i + 1]) for i in range(len(noise) - 1)]
        elif type == "purple":
            output = [0.5 * (noise[i] - noise[i + 1]) for i in range(len(noise) - 1)]
        else:
            output = noise[:-1]
        return output

    t = [i for i in range(pt - 1)]
    noise = [random.uniform(-amp, +amp) for i in range(pt)]
    return pd.DataFrame(data={"u": smoother(noise)})


# dyn sys equation ex
# parameters: weak - 0.02, 0.08, 0.095, 0.12; strong - 0.2
EPS = 0.02


# Equation System
def f_x(x):
    return 10 * x[1] - 10 * x[0]


def f_y(x):
    return 40 * x[0] - x[0] * x[2] - x[1]


def f_z(x):
    return x[0] * x[1] - 8 / 3 * x[2]


def f_u(x):
    return 10 * x[4] - 10 * x[3] + EPS * (x[0] - x[3])


def f_v(x):
    return 35 * x[3] - x[3] * x[5] - x[4]


def f_w(x):
    return x[3] * x[4] - 8 / 3 * x[5]


# Runge Kutta Method
def rk4(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x) * hs)
    for i in range(n):
        xk.append(x[i] + k1[i] * 0.5)
    for i in range(n):
        k2.append(fx[i](xk) * hs)
    for i in range(n):
        xk[i] = x[i] + k2[i] * 0.5
    for i in range(n):
        k3.append(fx[i](xk) * hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk) * hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
    return x
