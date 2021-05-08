# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:23:16 2020

@author: shyam

functions user-defined and built-in
"""
#math is one of the module
from math import *
#Defining a function
def add():
    a=input("Enter value 1: ")
    b=input("Enter value 2: ")
    print(int(a)+int(b)) 
    
#calling the function    
add()
print("")
c=-12
print(abs(c))
print(pow(2,2))
print(max(3,5))
print(min(3,4))
print(round(3.67))
print(floor(3.67))
print(ceil(3.67))
print(sqrt(36))
