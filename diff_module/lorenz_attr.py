# dyn sys relation parameter
# weak - 0.02, 0.08, 0.095, 0.12; strong - 0.2
EPS = 0.02

# Equation System
def f_x(x):
    return 10*x[1] - 10*x[0]
def f_y(x):
    return 40*x[0] - x[0]*x[2] - x[1]
def f_z(x):
    return x[0]*x[1] - 8/3*x[2]
def f_u(x):
    return 10*x[4] - 10*x[3] + EPS*(x[0] - x[3])
def f_v(x):
    return 35*x[3] - x[3]*x[5] - x[4]
def f_w(x):
    return x[3]*x[4] - 8/3*x[5]
