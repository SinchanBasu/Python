# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:33:31 2021

@author: SINCHAN BASU
"""

'''
Fibonacci sequence:
    0 th fib no = 0
    1 st fib no = 1
    2 nd fib no = 1
    3 rd fib no = 2
    4 th fib no = 3
    5 th fib no = 5
    .....

'''

# To find the nth Fibonacci number

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n= int(input('Enter a non-negative number'))
if n<0:
   print('Fibonacci numbers are undefined for negative numbers')
else:
 print('Fibonacci number at position ' , n , 'is' , fibonacci(n))    
    