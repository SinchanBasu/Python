# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:51:33 2021

@author: SINCHAN BASU
"""

'''
Base case or anchor case:
    point where recursion stops
    
fact(3)
==> 3 * fact(2)             ======>3 * 2
     ==> 2 * fact(1)          ===> 2 * 1
         ==> 1 * fact(0)       ===> 1 * 1
            ===> 1
    
'''

def factorial(n):
    product=1
    '''
    Iterative version:
    for i in range(1,n+1):
        product=product*i
        '''
        #Recursive version:
        #fact(n)=n*fact(n-1)
        #fact(0)=1
        
        #Base case
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a positive number: "))
if n<0:
    print('Factorial is not defined on negative numbers')
else:
    f=factorial(n)
    print('Factorial of ' ,n, 'is' , f)
    