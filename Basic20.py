#  Write a Python program to find the number of zeroes at the end of a factorial of a given positive number.
#  Range of the number(n) : (1<=m<=2*109)
def factendzero(n):
    x=n//5
    y=x
    while x>0:
        x/=5
        y+=int(x)
    return y
print(factendzero(5))
print(factendzero(12))
print(factendzero(100))