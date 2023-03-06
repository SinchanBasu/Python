pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid
            else:
                u=mid

list=[]
a=int(input("Enter how many elements you want to create : "))
print("Enter the list in sorted order : ")
for i in range(a):
    x=int(input("Enter the elements : "))
    list.append(x)
n=int(input("Enter the value which you want to find : "))
if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")
