# Problem
'''An automobile plant contracted to buy shock absorbers from two suppliers X and Y.X supplies 60%
and Y supplies 40% of the shock absorbers. All shock absorbers are subjected to a quality test.The
ones that pass the quality test are considered reliable. Of X’s shock absorbers, 96% are reliable.
Of Y’s shock absorbers, 72% are reliable. The probability that a randomly chosen shock absorber,
which is found to be reliable, is made by Y
is (A) 0.288 (B) 0.334 (C) 0.667 (D) 0.720'''

# Solution
import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

# Given Data
sample_size = 1000000
prob_X = 0.6
prob_Y = 0.4
prob_R_X = 0.96
prob_R_Y = 0.72

# Simulations using Bernoulli r.v.
sample_X = bernoulli.rvs(size=sample_size, p=prob_X)
sample_Y = bernoulli.rvs(size=sample_size, p=prob_Y)
sample_R_X = bernoulli.rvs(size=sample_size, p=prob_R_X)
sample_R_Y = bernoulli.rvs(size=sample_size, p=prob_R_Y)

# Calculating the number of favourable outcomes
n_X = np.nonzero(sample_X == 1)
n_Y = np.nonzero(sample_Y == 1)
n_R_X = np.nonzero(sample_R_X == 1)
n_R_Y = np.nonzero(sample_R_Y == 1)

# Calculating the probability using Bayes Theorem and Simulation
sim_prob = (np.size(n_R_Y)*np.size(n_Y)) / ((np.size(n_R_X)*np.size(n_X))+(np.size(n_R_Y)*np.size(n_Y)))

print("The probability that a randomly chosen shock absorber,which is found to be reliable, is made by Y is",sim_prob, "(By simulation).")

# Calculating the probability using Bayes Theorem by theory
th_prob = (prob_Y)*(prob_R_Y)/((prob_X)*(prob_R_X)+(prob_Y)*(prob_R_Y))

print("The probability that a randomly chosen shock absorber,which is found to be reliable, is made by Y is",th_prob, "(By theory).")

# Plotting
def ploting_fig():
    x = 0
    plt.bar(x+0, th_prob, color='red', width=0.5, label='Theoretical')
    plt.bar(x+1, sim_prob, color='yellow', width=0.5, label='Simulation')
    plt.ylabel('Probabilities')
    plt.legend()
    plt.show()
ploting_fig()