#for loop 
#for(i=0;i<5;i++)
#loop variable starts from 0
for i in range(5):
    print(i)
#for scope is defined by indentation
sum=0
for i in range(5):
    print(i)
    sum=sum+i
print("Sum is",sum)

#Multiplication Tables
#n=input("Enter number whose table is needed ")
n=12
n=int(n)
for i in range(10):
    print(n,"x",i+1,"=",n*(i+1))
    
#While Loop to print 10 to 1
i=10
while(i>0):
    print(i,end=' ')
    i -= 1;
print("")
    
#w/o flag condition
message='Initially'
while message!='quit1':
    message=input("Enter message ['quit1' to exit]")
#w/ flag
message='Initially'
active=True
while active:
    message=input("Enter message ['quit2' to exit]")
    if message=='quit2':
        active=False
        
    
