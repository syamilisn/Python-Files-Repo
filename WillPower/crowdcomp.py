"""
Crowd Computing
Estimation of average trimmed mean
IMPORTING LIBRARIES
"""
#importing mean function
from statistics import mean
from scipy import stats
import matplotlib.pyplot as plt #last lines
import statistics #last lines
list=[100,212,90,78,2323,67,342,12,34,565,45,78,123,678,345,123,765,234,123,234,432,56,34,43,]
n=len(list)
#10% of n
m=int(0.1*n)
print(n)
#Imp:First sort the list
list.sort()

#METHOD1
#manual trim
trimmed=list[2:22]
mean1=0
#manual calculation of mean
for i in range(24):
    mean1=mean1+list[i]
mean1=mean1/24
print("mean is ",mean1)
print("mean using imported library is ",mean(list))
trimean=0
for i in range(10):
    trimean=trimean+trimmed[i]
trimean=trimean/24
print("trimmed mean: ",trimean)
print("")
print("OR")
print("")

#METHOD2
#Trim maually using calculated value/integer variables
trimmed=list[m:n+m]
print("mean using imported library is ",mean(list))
trimean=0
for i in range(10):
    trimean=trimean+trimmed[i]
trimean=trimean/24
print("trimmed mean: ",trimean)
print("")
print("OR")
print("")

#METHOD3
#importing trim_mean from stats
#Easiest method
"""syntax for trim mean: stats.trim_mean(arraylist,percentage)"""
print("Mean using library is", mean(list))
print("Trimmed mean using library is", stats.trim_mean(list,0.1))


#METHOD4
#plotting graphs
y=[]
for i in range(n):
    y.append(5)    #any constant value for y axis
plt.plot(list,y,'g--')   #green lines graph

print("")
print("OR")
print("")
q=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
plt.plot(list,q,'r--')   #red lines graph
plt.plot([statistics.mean(list)],[5],'ro')
plt.plot([statistics.median(list)],[5],'bs')

"""
print("")
print("OR")
print("")
y=[]
#q=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
for i in range(n-2*m):
    y.append(5) 
plt.plot(trimmed,y,'g--')   #green dots graph
#plt.plot(trimmed,q,'r--')   #red dots graph"""