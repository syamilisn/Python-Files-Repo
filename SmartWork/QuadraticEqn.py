#Quadratic Equations
"""
Created on Fri Sep 11 11:39:02 2020

@author: shyam

d:discriminant 
"""
import math
import numpy as np

print('Enter Quadratic Equation:')
a,b,c=map(int,input('a b c ').split())
print('Quadratic Equation is:',a,'x^2 +',b,'x +',c)
d= b**2 - 4*a*c
r1,r2=0,0
if d>0:
    #Eg: a,b,c=1,-1,-3
    r1= (-b + math.sqrt(d))/2*a
    r2= (-b - math.sqrt(d))/2*a
    print("The roots are real and distinct:")
    print("root1 = ",r1)
    print("root2 = ",r2)
elif d==0:
    #Eg: a,b,c=1,2,1
    r1= -b/(2*a)
    r2= r1
    print("The roots are real and equal:")
    print("root1 = ",r1)
    print("root2 = ",r2)
elif d<0:
    #Eg: a,b,c=1,4,5
    x= -b/(2*a)
    y= math.sqrt(-d)/(2*a)
    z=complex(x,y)
    print("The roots are imaginary:")
    print("root1 = ",z)
    print("root2 = ",np.conj(z))