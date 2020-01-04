import pandas as pd
import matplotlib.pyplot as plt


# Runge Kutta Method
def rk4(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x


# Equation System
def f_x(x):
    return 10*x[1] - 10*x[0]
def f_y(x):
    return 40*x[0] - x[0]*x[2] - x[1]
def f_z(x):
    return x[0]*x[1] - 8/3*x[2]


def lorenz():
    f = [f_x, f_y, f_z]
    x = [1, 1, 0]
    hs = 0.02
    res = []
    for i in range(1000):
        x = rk4(x, f, 3, hs)
        res.append([x[0], x[1], x[2]])
    res = pd.DataFrame(X)
    return res


if __name__ == '__main__':
    s = lorenz()
    print(s[0])
