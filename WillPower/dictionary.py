# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:00:38 2020

@author: shyam

DICTIONARY[similar to switch]
"""
weekdays={
    "sun":"sunday",
    "mon":"monday",
    "tue":"tuesday",
    "wed":"wednesday",
    "thu":"thursday",
    "fri":"friday",
    "sat":"saturday"
}
print(weekdays["sun"])
print(weekdays.get("thu"))
print(weekdays.get("thor","invalid"))
print("")
specialA={
	1: "Kei",
	2: "Hikari",
	3:"Jun",
	4:"Megumi",
	5:"Tadashi",
	6:"Akira",
	7:"Ryuu"
}
    
for rank in specialA:
    if rank==1:
        print("Congratulations on getting 1st Rank",specialA[rank])
        
    print("Rank",rank,": Name",specialA[rank])
    
print (specialA)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0,"\n")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0,"\n")
list=["Maggi","Top Ramen", "Yippee"]
dict={1:"Maggi",2:"Top Ramen", 3:"Yippee"}
dict2={"Maggi","Top Ramen", "Yippee"}
print(list,"\n")
print(list[0],"\n")
print(dict,"\n")
print(dict[1],"\n")
print(dict2,"\n")
