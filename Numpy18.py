# Write a NumPy program to generate an array of 15 random numbers from a satbdard normal distribution.
import numpy as np
rand_num  = np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution : ")
print(rand_num)