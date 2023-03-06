# Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np
v = np.arange(15,55)
print("Original vector : ")
print(v)
print("All values except the first and last of the said vector : ")
print(v[1:-1])