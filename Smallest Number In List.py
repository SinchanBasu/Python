from array import *
arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    arr.append(x)
print(arr)
min=arr[0]
for i in range(n):
    if(arr[i]<min):
        min=arr[i]
print(min)
