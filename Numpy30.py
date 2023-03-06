# Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeroes on the main diagonal.
import numpy as np
x = np.zeros((4,4))
x[::2,1::2] = 1
x[1::2,::2] = 1
print(x)