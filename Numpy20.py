# Write a NumPy program to create a 3x4 array using and iterate over it.
import numpy as np
a = np.arange(10,22).reshape((3,4))
print("Original array : ")
print(a)
print("Each element of the array is : ")
for x in np.nditer(a):
    print(x,end=" ")