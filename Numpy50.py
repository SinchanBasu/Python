import numpy as np
nums = np.arange(16, dtype='int').reshape(-1,4)
print("Original array : ")
print(nums)
print("\nNew array after swapping first and last rows of the said array : ")
nums[[0,-1],:]=nums[[-1,0],:]
print(nums)