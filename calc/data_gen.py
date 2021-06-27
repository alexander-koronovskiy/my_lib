"""
one-column dataframe
linear, nonlinear, harmonic and solution of differential equation
sequence are produced to aggregator
"""

import numpy as np
import pandas as pd


def diff_sol(t, f, points=10000, dt=0.02):
    """
    method of differential equation solution
    use: "generator='diff_sol', :params" in () load_series

    params info
    t: initial conditions [x0, x1,.., xn]
    f: diff equations [f_1, f_2,.., f_n]
    pt: rows number
    dt: Runge-Kutta step
    """
    size = len(f)
    res = []
    t0 = []
    for i in range(points):
        t0.append(i * dt)
        t = rk4(t, f, size, dt)
        res.append([t[j] for j in range(len(t))])
    res = pd.DataFrame(res)
    t0 = pd.DataFrame(t0)
    res.columns = [j + 1 for j in range(len(t))]
    return t0.join(res)


def linear(points=10000, t0=0, t1=10, a=1, b=0):
    """
    method of linear function build
    use "generator='linear', :params" in () load_series

    params info
    t0: start point
    t1: end point
    a: coefficient before t
    b: additional coefficient
    points: points number
    """
    t = np.linspace(t0, t1, points)
    u = a * t + b
    return pd.DataFrame(data={"u": u})


def nonlinear(points=10000, t0=0, t1=10, a=1, b=0, c=0, n=3):
    """
    method of nonlinear function build
    use "generator='nonlinear', :params" in () load_series

    params info
    t0: start point
    t1: end point
    a: coefficient before t
    b: additional coefficient within (a*t + b)^n
    c: additional coefficient after (a*t + b)^n + c
    n: polynomial power, points: points number
    """
    t = np.linspace(t0, t1, points)
    u = a * (t + b) ** n + c
    return pd.DataFrame(data={"u": u})


def harmonic(points=10000, t0=0, t1=10, a=1, omega=1, theta=0):
    """
    method of harmonic function build
    use "generator='harmonic', :params" in () load_series

    t0: start point
    t1: end point
    a: oscillation amplitude
    omega: coefficient before t
    theta: initial phase, points: points number
    """
    t = np.linspace(t0, t1, points)
    u = a * np.cos(omega * t + theta)
    return pd.DataFrame(data={"u": u})


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


def gauss_noise(points=10000):
    """
    method of harmonic function build
    use "generator='white_noise', :params" in () load_series
    """
    mu, sigma = 0, 1
    u = np.random.normal(mu, sigma, points)
    return pd.DataFrame(data={"u": u})
