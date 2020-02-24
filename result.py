import random
import matplotlib.pyplot as plt


def smoother(noise, type='red'):
    output = []
    for i in range(len(noise) - 1):
        if type == 'red':
            output.append(0.5 * (noise[i] + noise[i+1]))
        if type == 'purple':
            output.append(0.5 * (noise[i] + noise[i + 1]))
        else:
            output.append(noise[i])
    return output


noise = [random.uniform(-1, +1) for i in range(100)]

white = noise
red = smoother(noise, 'red')

plt.plot(red)
plt.show()
