# Write a NumPy program to create a two-dimensional array of specified format.
import numpy as np
print("Create an array of shape (15,10) : ")
print("Command-1")
print(np.arange(1,151).reshape(15,10))
print("Command-2")
print(np.arange(1,151).reshape(-1,10))
print("\nCommand-3")
print(np.arange(1,151).reshape(15,-1))