# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:39:28 2020

@author: shyam
if-else stat
comparison operators
"""
#simple if-else 
c=30
if(c>20):
    print("c is greater than 20")
else:
    print("c is lesser than 20")
    
if(True):
    print("print")
if True:
    print("print")
    
yes= True
no= False
Maybe= True
Will_See= False

if(yes or no):
    print("*")
#else if
#and 
#and not
if(yes and no):
    print("-")
elif(yes and not no):
    print("-")   
    
    
#return largest of 3 numbers:
def largestOf3(p,q,r):
    if p>q:
        if p>r:
            print(p,"is the largest number")
        else:
            print(r,"is the largest number")
    else:
        if q>r:
            print(q,"is the largest number")
        else:
            print(r,"is the largest number")
        
largestOf3(3,6,9)
#return smallest of 3 numbers:
def smallerOf3(p,q,r):
        if p<q and p<r:
            print(p,"is the smallest number")
        elif q<p and q<r:
            print(q,"is the smallest number")
        else:
            print(r,"is the smallest number")
smallerOf3(3,6,9)