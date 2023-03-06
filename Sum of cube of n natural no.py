n=int(input("Enter a natural number : "))
def cube_sum(n) :
    sum=0
    for i in range(1,n+1):
        sum=sum + (i*i*i)
    return sum
print("The sum of cube of",n,"is : ",cube_sum(n))