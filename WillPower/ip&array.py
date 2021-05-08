#creating array
list=["Inuyasha","Kagome","Kikyo"]
#print all at once
print(list)
#print one by one
for item in list:
    print(item)
#individual item
print(list[0])
print(list[1])
print("")
print("Anime characters from Inuyasha")
i=item 
#i=0;i<3;i++
for i in range(3):
    print(list[i])
#another array    
list2=["Miroku","Sango","Shippo","Koga","Kirara"]
for i in range(5):
    print(list2[i])

"""
Array operation is Python
append():insert item at end of list
insert():insert item at the given position
remove():delete element
pop():removes one item[when no index is passed] or at given position[if index is passed]
arrayname.count(x): To find frequency of given x value in list 'arrayname'
len(arrayname):Length of list
sort():ascending order
reverse():descending order
array1.append(array2): adds 2 arrays
array2=array1.copy: copies array to another
selecting range in array elements: Given below
"""
list.append("Naraku")
list.remove("Kikyo")
list2.insert(2,"Sesshomaru")
print(list)
print(list2)
#removes naraku
list.pop(2)
print(list)
#Display freq. using count
list3=[2,2,4,2,3,4,4,3,8,4,1,1]
print("")
print(list3.count(2))
n=list3.count(4)
#Find array length using len()
print(n)
print(len(list3))
#Find array length manually usinf for loop
count=0
for i in list3:
    count=count+1
print(count)
#sorts in ascending order
print(list3)
list3.sort()
print(list3)
list3.reverse()
print(list3)

print(list)
list.sort()
print(list)
list.reverse()
print(list)

print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)

"""using slicing to choose part of a data structure i.e. range"""
print("")
print(list2)
print(list2[0:3])
print(list2[1:3]) #doesn't include 3rd item: Miroku
print(list2[3:])  #includes 3rd item: Miroku


#negative indices represent reverse order indices starting from {0,.....-3,-2,-1}
print(list2[-1])  #prints kirara
print("")
#Adding/Extending a list
list.extend(list2)
print(list)
print(list2)
print(list3)
list3=list.copy()
print(list3)
#multi-dimensional array
print("")
list4=[[1,2],[2,3],[4,5]]
print(list4[1][0])

for row in list4:
    print(row)
    #Nested for loops
print("")
for row in list4:
    for col in row:
        print(col)


