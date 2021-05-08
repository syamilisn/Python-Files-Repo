# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:31:00 2020

@author: shyam

Topic: FUNCTIONS
"""
#importing custom calculator
import calculator
#fn w/o parameter
def hello():
        print("Hello World!")

hello()

#fn w/ parameter
def param(num,lit):
    print(num,lit)
    
param(8,"cube of 2")

#fn w/ return value
#return is like the ending statement of the fn
def cube(a):
        return a*a*a
    
cub=cube(3)
print(cub)

print(cube(2))

print(calculator.add(35,53))
