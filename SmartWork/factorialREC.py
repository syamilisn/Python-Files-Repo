#factorial by recursion
"""
Created on Fri Sep 18 11:26:28 2020

@author: shyam
"""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))