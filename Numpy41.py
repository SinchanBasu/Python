# Write a NumPy program to convert numpy dtypes to native python types.
import numpy as np
print("numpy.float32 to python float")
x = np.float32(0)
print(type(x))
pyval = x.item()
print(type(pyval))