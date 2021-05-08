# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:09:19 2020

@author: shyam

Guessing game
"""
#guessing game
secretword="anime"
guess=""
count=0
limit=3
over= False
while guess != secretword and not over:
    if count<limit:
        guess=input("Enter guess: ")
        count +=1
    else:
        over=True
if over:        
    print("you lose!")
else:
    print("You win!")
