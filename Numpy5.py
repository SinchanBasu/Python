# Write a Numpy program to test a given array element-wise for finiteness (not infinity or not a Number)
import numpy as np
a = np.array([1,0,np.nan,np.inf])
print("Original array : ")
print(a)
print("Test a given array element-wise for finiteness : ")
print(np.isfinite(a))
