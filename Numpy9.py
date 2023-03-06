# Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
'''
The tolerance values are positive,typically very small numbers. The relative difference (rtol*abs(b)) and the absolute difference atol are added together to comapre against the absolute difference between a and b.
'''
import numpy as np
print("Test if two arrays are element-wise equal within a tolerance : ")
print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
print(np.allclose([11e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
print(np.allclose([1.0,np.nan], [1.0,np.nan]))
print(np.allclose([1.0,np.nan],[1.0,np.nan],equal_nan=True))