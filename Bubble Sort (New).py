def Bubble_Sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[]
a=int(input("Enter how many elements you want to create : "))
for i in range(a):
    x=int(input("Enter the elements : "))
    nums.append(x)
print(nums)
Bubble_Sort(nums)
print("The list in sorted order is : ",nums)
