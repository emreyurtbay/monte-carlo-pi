import numpy as np
import random
import math
import matplotlib
import matplotlib.pyplot as plt

def MCpi(n_trials):
    '''
    Runs a single Monte Carlo simulation to generate a estimation of pi.

    Imagine a Square with side length 1, and a Quarter of a circle inscribed in it,
    with a "radius" of 1. The area of the square is 1, and the area of quarter circle is
    pi/4. So the ratio of area between the quarter circle and the entire square is pi/4 / 1,
    or pi/4. This means the ratio of the number of randomly generated points that land inside the quarter 
    circle over the number of randomly generated points inside the entire square is pi/4. If we multiply
    this ratio by 4, we have an approximation for pi

    N_trails: Number of Points to Generate
    '''
    points_inside = 0
    for i in range(n_trials):

        # Generate a Random Point
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        # Is the point inside or outside the circle
        if distance < 1:
            points_inside += 1
    
    # Estimate for pi
    return 4*(float(points_inside)/n_trials)


def runExperiments(t_vector):
    '''
    Returns a series of pi predictions, given a vector of values telling
    how many trials to run per simulation
    '''
    pi_vals = []
    for i in t_vector:
        pi_vals.append(MCpi(i))

    return pi_vals


# Simulations
n_trials_final = 10000
t = np.arange(1, n_trials_final, 10)
s = runExperiments(t)

# Plot Visualization
fig, ax = plt.subplots()
ax.plot(t, s)
plt.axhline(y=np.pi, color='r', linestyle='-')

ax.set(xlabel='Number of Monte Carlo Trials', ylabel='Estimated Value of Pi',
       title='Monte Carlo Simulation of Pi')
ax.grid()

fig.savefig("/Users/emreyurtbay/Documents/Python/test.png")
plt.show()
