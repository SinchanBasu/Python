# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:51:50 2021

@author: SINCHAN BASU
"""

def magic_square(n):
    
    
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
            
    for i in range(n):
        #l = []
        for j in range(n):
           # l.append(0)
         print(magicSquare[i][j], end=" ")
        print()
                   