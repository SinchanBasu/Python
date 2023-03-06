pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[]
a=int(input("Enter how many elements you want to create : "))
for i in range(a):
    x=int(input("Enter the elements : "))
    list.append(x)
n=int(input("Enter the value which you want to find : "))
if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")

    