from array import *
arr=array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    arr.append(x)
for i in range(n):
    if(arr[i]==arr[i+1]):
        i=i+1
        print("True")
    else:
        print("False")