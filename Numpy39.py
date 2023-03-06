# Write a NumPy program to convert a given list into an array, then again convert it into a list. Check initial list and final list are equal or not.
import numpy as np
a = [[1,2],[3,4]]
x = np.array(a)
a2 = x.tolist()
print(a == a2)