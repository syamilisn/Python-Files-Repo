#remove duplicates from list
"""
Created on Wed Oct  7 13:34:16 2020

@author: shyam
"""
def rmduplicate(list1):
    list2=[]
    for item in list1:
        if(item not in list2):
            list2.append(item)
    return list2

list1=[1,2,3,4,4,3,2,1]
print(rmduplicate(list1))
        
        