# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:34:46 2020

@author: shyam

translator
"""
#replaces vowels with letter g
def translate(word):
    translation=""
    for letter in word:
        if letter in "AEIOUaeiou":
            translation=translation +'g'
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter word:")))