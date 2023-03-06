# Write a NumPy program to compute the x and y corrdinates for points on a sine curve and plot the points using matplotlib.
import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve.
x = np.arange(0,3*np.pi,0.2)
y = np.sin(x)
print("Plot the points using matplotlib : ")
plt.plot(x,y)
plt.show()