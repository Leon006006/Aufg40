import numpy as np
import matplotlib.pyplot as plt


def logisticFct(reproduction_factor, x):
    return reproduction_factor * x * (1 - x)


def log_fix(reproduction_factor, start_pop):
    """
    :param reproduction_factor: Reproduction factor r for logistic function
    :param start_pop: Starting population
    :return: Points 2000 to 2200 of the Iteration
    """
    x = start_pop
    # Compute first 2000 steps
    # Fixed points should be reached
    for iteration in range(2000):
        x = logisticFct(reproduction_factor, x)

    # Compute next "fix_p" steps for plot
    fix_x = np.zeros(fix_p)
    fix_x[0] = x
    for iteration in range(fix_p-1):
        fix_x[iteration + 1] = logisticFct(reproduction_factor, fix_x[iteration])
    return fix_x


# Initialize Constants
fix_p = 200
count_r = 300
r_start = 2.9
r_end = 4
x_start = 0.5

r_vec = np.linspace(r_start, r_end, count_r)
plot_matrix = np.zeros((fix_p, count_r))

# Iterate over different reproduction values r
counter = 0
for r in r_vec:
    plot_matrix[:, counter] = log_fix(r, x_start)
    plt.plot(r_vec[counter] * np.full(fix_p, 1), plot_matrix[:, counter], 'bo', markersize=1)
    counter += 1

# PLot Data
plt.title('Fix points with x=0.5 as staring point')
plt.xlabel('r')
plt.ylabel('Fixed point')
plt.show()
