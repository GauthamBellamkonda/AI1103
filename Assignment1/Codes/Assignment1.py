import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

simlen = int(1e7)

#probabilities
prob_hrt_atk = 0.4
prob_hrt_atk_yoga = 0.4*(1-0.3)       #Probability of having a heart attack given that the person does yoga
prob_hrt_atk_drug = 0.4*(1-0.25)      #Probability of having a heart attack given that the person takes the drug

#Using Bernoulli Random Variable
data_bern_yoga = bernoulli.rvs(size = simlen, p = prob_hrt_atk_yoga)      #A bernoulli distribution simulating number of people who do yoga and die of heart attack
data_bern_drug = bernoulli.rvs(size = simlen, p = prob_hrt_atk_drug)      #A bernoulli distribution simulating number of people who took the drug and die of heart attack

#Calculating the number of favourable outcomes
err_ind_yoga = np.nonzero(data_bern_yoga == 1)
err_ind_drug = np.nonzero(data_bern_drug == 1)

#Calculating the probabilities
err_n_yoga = np.size(err_ind_yoga)/simlen
err_n_drug = np.size(err_ind_drug)/simlen

#We use the fact that the probability of a person doing yoga is equal to the probability of the person taking the drug
exp_prob_yoga = err_n_yoga/(err_n_yoga + err_n_drug)                        #experimental probability
the_prob_yoga = prob_hrt_atk_yoga/(prob_hrt_atk_yoga + prob_hrt_atk_drug)   #Theoretical Probability

print("The Experimental Probability is : ",exp_prob_yoga)
print("The Theoretical Probability is : ",the_prob_yoga)
