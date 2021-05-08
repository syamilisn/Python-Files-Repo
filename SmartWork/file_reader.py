# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:15:24 2020

@author: shyam

FILES
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    for line in file_object:
        print(line,"\n")
for line in contents:
    print(line)

    