# Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line without spaces between them.
def degrees(num):
    ans = True
    n,tempn, i = 2,2,2
    while ans:
        if str(tempn) in num:
            i += 1
            tempn = pow(n,i)
        else:
            ans = False
    return i-1
print(degrees("2481632"))
print(degrees("248163264"))