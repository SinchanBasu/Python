from array import *
arr=array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    arr.append(x)
print(arr)
for i in range(n):
    if(arr[0]<arr[n-1]):
        tmp=arr[0]
        arr[0]=arr[n-1]
        arr[n-1]=tmp
print(arr)