# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:52:46 2020

@author: shyam
"""
""" 
"r+": read & write
"w":write -->overwrite or new file
"a":append --->adds at end of existing file
"""
hellofile=open("hello.txt","r+")#read
print(hellofile.readable())#checks if file is readable
print(hellofile.readline())#reads a line
print(hellofile.readlines())#many lines
hellofile.write("\nWelcome")
hellofile.close()
