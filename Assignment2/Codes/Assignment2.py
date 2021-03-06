import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Doing the experiment 1e7 times
simlen=int(1e7)

sample_size = 52        #As there are 52 cards in a deck
event_size = 4          #As there are 4 Aces in a deck
prob_Ace = event_size/sample_size

#Simulation using bernoulli r.v
data_bern_Ace = bernoulli.rvs(size = simlen, p = prob_Ace)

#Number of Favourable outcomes
err_ind_Ace = np.nonzero(data_bern_Ace == 1)
err_ind_Not_Ace = np.nonzero(data_bern_Ace == 0)

#Calculating the probability
exp_prob_Ace = np.size(err_ind_Ace)/simlen
exp_prob_Not_Ace = np.size(err_ind_Not_Ace)/simlen
#Printing theoretical and experimental probability
print("Theoretical Probability of getting an Ace = ", prob_Ace)
print("Experimental Probability of getting an Ace = ", exp_prob_Ace)

print("Theoretical Probabilty of not getting an Ace = ", 1 - prob_Ace)
print("Experimental Probability of not getting an Ace = ", exp_prob_Not_Ace)
