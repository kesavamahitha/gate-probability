import numpy as np
from scipy.stats import bernoulli

sample_size=100000

#given probabilities
prob_zero = 9/10
prob_transition = 1/8

error = 0

#Simulations using Bernoulli r.v.
sample_zero= bernoulli.rvs(size= sample_size, p = prob_zero)
sample_transition= bernoulli.rvs(size= sample_size, p = prob_transition)

for i in range(sample_size):
  if sample_transition[i]==0 and sample_zero[i] ==0:
    error+=1
  elif sample_transition[i]==0 and sample_zero[i] ==1:
    error+=1

calc_prob_error = error/sample_size

prob_error = prob_zero*(1-prob_transition) + (1-prob_zero)*(1-prob_transition)
print("Probability of error by simulations: ",calc_prob_error,"while theoretical value is:",prob_error)
