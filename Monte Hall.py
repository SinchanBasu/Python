# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:47:03 2021

@author: SINCHAN BASU
"""

import random
doors=[0]*3
goatdoor=[0]*2
swap=0  #No of swap wins
dont_swap=0 #No of dont swap wins
j=0
while(j<10):
  x=random.randint(0,2) #x th door will comprise of BMW
  doors[x]="BMW"
  for i in range(0,3):
     if(i==x):
        continue
     else:
        doors[i]="Goat"
        goatdoor.append(i)
  choice=int(input("Enter your choice"))
  door_open=random.choice(goatdoor) #open a door that comprises of goat
  while (door_open==choice):  #door open shouldn't be equal to choice made by the participant
      door_open=random.choice()       
  ch= input("Do you want to swap? y/n")
  if (ch=='y'):
      if (doors[choice]=='Goat'):
         print("Player wins")
         swap=swap+1
      else:
         print("Player lost")
  else:
      if(doors[choice]=='Goat'):
          print("Player lost")
      else:
          print("Player wins")
          dont_swap=dont_swap+1
  0j=j+1       
        
print(swap) 
print(dont_swap)       