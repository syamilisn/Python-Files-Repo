#List of dictionaries
#Dictionary: anime character database
char1={'name':'Asta','Attribute':'Anti Magic'}
char2={'name':'Yuno','Attribute':'Wind Magic'}
char3={'name':'Noelle','Attribute':'Water Magic'}
Database=[char1,char2,char3]
for character in Database:
    print(character,end='\n')
    
#Adding a list of items dynamically/ Modifying list
list=[]
active=True
while active:
    response=input('Continue? y/n ')
    if response=='n':
        active=False
    else:
        a=input('Enter anime character name:')
        list.append(a)
print(list)