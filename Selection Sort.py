def Selection_Sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
nums=[]
a=int(input("Enter how many elements you want to create : "))
for i in range(a):
    x=int(input("Enter the elements : "))
    nums.append(x)
print(nums)
Selection_Sort(nums)
print("The list in sorted order is : ",nums)

