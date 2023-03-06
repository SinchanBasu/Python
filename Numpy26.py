# Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np
m = np.arange(10,22).reshape((3,4))
print("Original matrix : ")
print(m)
print("Number of rows and columns of the said matrix : ")
print(m.shape)