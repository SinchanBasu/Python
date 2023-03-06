# Write a NumPy program to save a given array to a binary file.
import numpy as np
import os
a = np.arange(20)
np.save('temp_arra.npy',a)
print("Check if 'temp_arra.py' exists or not?")
if os.path.exists('temp_arra.npy'):
    x2 = np.load('temp_arra.npy')
    print(np.array_equal(a,x2))