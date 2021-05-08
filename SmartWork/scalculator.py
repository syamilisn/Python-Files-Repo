# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:11:04 2020

@author: shyam

solving.py
scalculator.py
calculator.py

MODULUS, FACTORIAL
"""

from calculator import  Calculator
class Scalculator(Calculator):
    def __init__(self,a,b):
            super().__init__(a,b)
		
    def mod(self):
        try:
            return self.a % self.b
        except ZeroDivisionError as eobj:
            print(eobj)
           
    def fact(self,n):
        if n==0 or n==1:
            return 1
        else:
            return n * self.fact(n-1)