# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 06:15:25 2020

@author: shyam
"""
from random import randint
def guessnum():
    x= randint(1,10)
    chance=1
    while chance<=7:
        guess=int(input("Enter your guess "))
        chance+=1
        if guess==x:
            print('You guess is the correct guess')
            break
        elif guess<x:
            print('you guess is less than number')
        else:
            print('you guess is more than number')
            
    print("THE END")
    ans=int(input("DO you want to continue? 1/0 "))
    return(ans)
    

choice=1    
while(choice):
    #print("Do you want to play the guessing game? 1/0 for y/n")
    choice = guessnum()