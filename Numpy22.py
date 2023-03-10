# Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np
x = np.arange(21)
print("Original vector : ")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15 : ")
x[(x>=9) & (x<=15)] *= -1
print(x)