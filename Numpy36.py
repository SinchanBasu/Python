# Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.
import numpy as np
import os
x = np.arange(10)
y = np.arange(11,20)
print("Original array : ")
print(x)
print(y)
np.savez('temp_arra.npz',x=x,y=y)
print("Load arrays from the 'temp_arra.npz' file: ")
with np.load('temp_arra.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(x2)
    print(y2)