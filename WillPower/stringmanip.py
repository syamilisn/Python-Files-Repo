# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:47:22 2020

@author: shyam
"""
#Theme: Black Clover
#STRING MANIPULATIONS
#BOOLEAN VALUES

"""
1)STRING CONCATINATION/ADDITION [3 ways]

, appends spaces [exception: Can't be used in input statements]
    print("Hello",name,"-san ")----->Hello name -san
+ gives no spaces
    print("Hello"+name+"-san ")----->Helloname-san
f"": f-strings [f:format] are another way of concatination
    string3=f"{string1}{string2}"
    print(f"Hello, {full_name.title()}!")
    message = f"Hello, {full_name.title()}!"

2)BOOLEAN VALUES
Mind the difference----
if("True") returns true         String value
if("False") returns true        String value
if(True) returns true           Boolean value
if(False) returns false         Boolean value

3)Character Sequences
\n:nextline
\": one double quote
....

4)String manipulations: more than one can be used at a time
stringname.upper(): upper case      
.lower(): lower case
.isupper():  Checks if upper, returns boolean
.islower():   checks if lower, returns boolean     
.title(): First letter of each word in string is capital  
len(stringname): string length 
.index(insert_char):  returns char's index no.     
.replace("orig. string","replace string")            
"""

first_name=input("Enter your first-name: ")
last_name=input("Enter your last-name: ")
name=f"{first_name} {last_name}"
print("\nHello",name.title(),"-san ")
anime="Black Clover"
#String concatenation
interested = input("Do you like watching "+anime+"? Reply if yes otherwise press 'Enter' key\n")
#Here string is returned not boolean value.
if(interested):
    print("Welcome to Black Clover Fandom!!! \n")
    print(anime,"Font style:")
    #temporary upper case
    print(anime.upper())
    print(anime.upper().isupper())
    print(len(anime),'\n')
    #string is character array and can be accessed using indices
    for i in range(len(anime)):
        print(anime[i],anime.index(anime[i]))
else:
    print("Oh! Too bad. Please enjoy watching other anime series.\n")


