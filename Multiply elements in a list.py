from array import *
arr=[]
n=int(input("Enter the length of the list : "))
for i in range(n):
    x=int(input("Enter the elements of the list : "))
    arr.append(x)
print(arr)
result=1
for i in range(1,n+1):
    result=result*i
print(result)