# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:11:20 2020

@author: shyam

solving.py
scalculator.py
calculator.py
"""

from scalculator import Scalculator as sc
a=5
b=0
obj=sc(a,b)
print(f"The sum of {a} and {b} is {obj.add()}")
print(f"The difference of {a} and {b} is {obj.subtract()}")
print(f"The product of {a} and {b} is {obj.multiply()}")
if obj.divide():
    """Returns none if denominator is zero"""
    print(f"The division of {a} and {b} is {obj.divide()}")
    print(f"The remainder of {a} and {b} is {obj.mod()}")
print(f"The factorial of {a} is {obj.fact(a)}")
