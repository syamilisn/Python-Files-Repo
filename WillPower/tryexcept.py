# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:41:08 2020

@author: shyam

Try & Except
"""
#divide by zero error

try:
    a=12
    b=0
    c=a%b
    print(c)
    #not recommended
except:
    print("Invalid")
    
try:
    a=12
    b=0
    c=a/b
    print(c)
#recommended
except ZeroDivisionError:
    print("denomenator is zero. Division by zero error")
except ZeroDivisionError as err:
    print(err)
    
except ValueError:
    print("Invalid input")
    