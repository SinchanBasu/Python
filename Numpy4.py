# Write a Numpy program to test whether any of the elements of a given array is non-zero.
import numpy as np
x = np.array([1,0,0,0])
print("Original array : ")
print(x)
print("Test whether any of the elements of a given array is non-zero : ")
print(np.any(x))
x = np.array([0,0,0,0])
print("Original array : ")
print(x)
print("Test whether any of the elements of a given array is non-zero : ")
print(np.any(x))