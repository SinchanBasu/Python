from array import *
arr=array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the value of the array : "))
    arr.append(x)
max=arr[0]
for i in range(n):
    if(arr[i]>max):
        max=arr[i]
        i=i+1
print(max)