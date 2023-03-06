from array import *
arr=array('i',[])
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    arr.append(x)
print("The array is : ",arr)
arr.reverse()
print("The reverse array is : ",arr)

