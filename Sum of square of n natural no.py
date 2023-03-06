n=int(input("Enter a natural number : "))
def square_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum
print("The sum of square of",n,"is : ",square_sum(n))