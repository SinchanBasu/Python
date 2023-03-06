# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:19:19 2021

@author: SINCHAN BASU
"""

import string
dict={}
data=""
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("file1.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of File")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data) 
file.close()