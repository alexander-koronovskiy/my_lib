import load

if __name__ == '__main__':
    s = load.load_series(generator='lorenz')
    import matplotlib.pyplot as plt
    plt.plot(s[1]); plt.show()
