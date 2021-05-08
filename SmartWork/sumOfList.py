#sum of list
"""
Created on Wed Oct  7 13:19:29 2020

@author: shyam
"""

def sumOfList(list):
    for item in list:
        sum=0
        sum+=item
    print('sum of list is',sum)
    
def min(list):
    min=list[0]
    for item in list:
        if min>item:
            min=item
            return min

def max(list):
    max=list[0]
    for item in list:
        if max<item:
            max=item
            return max
        
    
    
list=[4,1,2,3]
#sumOfList(list)
print('minimum of list',min(list))
print('maximum of list',max(list))
