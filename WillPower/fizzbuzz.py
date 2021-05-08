"""FizzBuzz Game:
    For all multiples of 3 say fizz
    For all multiples of 5 say bizz
    For all multiples of 3 & 5 say fizzbuzz
    """
        
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(i,"= FizzBuzz")
    elif((i%3)==0):
        print(i,"= Fizz")
    elif((i%5)==0):
        print(i,"= Buzz")
    else:
        print(i)