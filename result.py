import load

if __name__ == '__main__':
    x_series = load.load_series(path='upload/phase drive/0.9_x_eps=0.1.dat')
    y_series = load.load_series(path='upload/phase drive/0.9_y_eps=0.1.dat')

    import matplotlib.pyplot as plt
    plt.plot(x_series[x_series.columns[0]], y_series[y_series.columns[0]])
    plt.show()
