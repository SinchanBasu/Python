from array import *
arr=array('i',[])
n=int(input("Enter the length of the array : "))
sum=0
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    sum=sum+x
print("The sum of the elements of the array is : ",sum)