from array import *
arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    x=int(input("Enter the elements of the array : "))
    arr.append(x)
print(arr)
pos1=int(input("Enter the first position : "))
pos2=int(input("Enter the second position : "))
def swap_position(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
print("List after swapping : ",swap_position(arr,pos1-1,pos2-1))   