import numpy as np
import random
import math
import matplotlib
import matplotlib.pyplot as plt

def MCpi(n_trials):
    points_inside = 0
    for i in range(n_trials):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance < 1:
            points_inside += 1

    return 4*(float(points_inside)/n_trials)


def runExperiments(t_vector):
    pi_vals = []
    for i in t_vector:
        pi_vals.append(MCpi(i))

    return pi_vals



n_trials = 10000
t = np.arange(1, n_trials, 10)
s = runExperiments(t)


fig, ax = plt.subplots()
ax.plot(t, s)
plt.axhline(y=np.pi, color='r', linestyle='-')

ax.set(xlabel='Number of Monte Carlo Trials', ylabel='Estimated Value of Pi',
       title='Monte Carlo Simulation of Pi')
ax.grid()

fig.savefig("/Users/emreyurtbay/Documents/Python/test.png")
plt.show()
