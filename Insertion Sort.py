def Insertion_Sort(list):
    for i in range(len(list)):
        j=i
        while list[j-1]>list[j] and j>0:
            list[j-1],list[j]=list[j],list[j-1]
            j=j-1
list=[]
a=int(input("Enter how many elements you want to create : "))
for i in range(a):
    x=int(input("Enter the elements : "))
    list.append(x)
print(list)
Insertion_Sort(list)
print("The list in Sorted order is : ",list)