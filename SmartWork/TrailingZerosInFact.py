# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:31:46 2020

@author: shyam

To find the No. Of Trailing zeros in factorial of n
"""

n=int(input("Enter the value of n: "))
Fact=1
Count=0
for i in range(n):
    Fact=Fact*(i+1) 
while(Fact>0):
    Fact=Fact/10
    Rem=Fact%10
    if Rem==0:
        Count+=1
print(f"Trailing zeros in {n} factorial is {Count}")