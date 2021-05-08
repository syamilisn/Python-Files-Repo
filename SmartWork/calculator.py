# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:09:58 2020

@author: shyam

solving.py
scalculator.py
calculator.py

ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION
"""

class Calculator:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		
	def add(self):
		return self.a+self.b
		
	def subtract(self):
		return self.a-self.b
		
	def multiply(self):
		return self.a*self.b
		
	def divide(self):
		try:
			return self.a/self.b
		except ZeroDivisionError as eobj:
			print(eobj)