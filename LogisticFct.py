import numpy as np
import matplotlib.pyplot as plt


def logisticFct(r, x):
    return r * x*(1 - x)


def log_fix(r, start):
    x = start
    for iteration in range(2000):
        x = logisticFct(r, x)
    fix_x = np.zeros(200)
    fix_x[0] = x
    for iteration in range(199):
        fix_x[iteration + 1] = logisticFct(r, fix_x[iteration])
    return fix_x


r_vec = np.linspace(1, 4, 1000)
plot_matrix = np.zeros((200, 1000))
counter = 0

for r in r_vec:
    plot_matrix[:, counter] = log_fix(r, 0.5)
    plt.plot(r_vec[counter] * np.full(200, 1), plot_matrix[:, counter], 'bo', markersize=1)
    counter += 1
plt.title('Fix points with x=0.5 as staring point')
plt.xlabel('r')
plt.ylabel('Fixed point')
plt.show()
