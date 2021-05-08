# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:56:34 2020

@author: shyam
"""
 
dict1= {'I':1,'II':21,'III':21,'IV':1,'V':45}
print("The original dictionary is : " + str(dict1)) 
temp = [] 
res = dict() 
for key, val in dict1.items(): 
	if val not in temp: 
		temp.append(val) 
		res[key] = val 


print("The dictionary after values removal : " + str(res)) 
