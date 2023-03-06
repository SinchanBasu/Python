num=int(input("Enter the original number : "))
sum=0
temp=num
while(temp>0):
    remainder=temp%10
    sum=sum+remainder**3
    temp=temp//10
if(num==sum):
    print(num,"is a Armstrong Number")
else:
    print(num,"is not a Armnstrong Number")
