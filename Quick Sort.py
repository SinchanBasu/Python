def Quick_Sort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        Quick_Sort(arr,left,partition_pos-1)
        Quick_Sort(arr,partition_pos+1,right)
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while i<j:
        while i<right and arr[i]<pivot:
         i=i+1
        while j>left and arr[j]>=pivot:
         j=j-1 
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i 
arr=[]
a=int(input("Enter how many elements you want to create : "))
for i in range(a):
    x=int(input("Enter the elements : "))
    arr.append(x)
print(arr)
Quick_Sort(arr,0,len(arr)-1)
print("The lsit in sorted order is : ",arr)
