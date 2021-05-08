# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:22:39 2020

@author: shyam

CREATING FILE
"""
filename = 'programming.txt'
#write+create
with open(filename, 'w') as file_object:
    file_object.write("I love Anime.")
#read
with open(filename, 'r') as file_object:
    contents=file_object.read()
print(contents)
#append
with open(filename, 'w') as file_object:
    file_object.write("Hi\nMy name is asta\nNice to meet you!")
    
with open(filename, 'r') as file_object:
    contents=file_object.read()
print(contents)