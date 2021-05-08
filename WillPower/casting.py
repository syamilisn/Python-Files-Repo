n=input("What's your favorite number ")
print(n)
#Default i/p type is String
#concatenation
a=n+n
print(a)
#Type casting
a=int(n)+int(n)
print(a)
print("")
#Single line comment
"""This is also a comment
But it is multi lined"""
#input in single line
#inside split specifies custom seperator between inputs
a,b=10,20
print(a,b)
p,q,r=input("Enter 3 numbers separated by comma ").split(",")
print("P,Q,R values",p,q,r)

t=20
print(t+t)
st=str(t)
print(st+st)
print(st,t)
#print(st+t): error