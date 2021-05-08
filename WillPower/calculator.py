#Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
try:    
    def div(a,b):
        return a/b
except ZeroDivisionError:
    print("Divide by Zero error")
    