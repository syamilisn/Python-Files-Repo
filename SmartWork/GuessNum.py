#guessing game
#Either import random or from random import randrange or *
#import random
#x=random.randrange(1, 101)  OR
from random import randrange
def guessnum():
    x=randrange(1,101)
    count=0
    while(count<7):
        guess=int(input("Enter your guess: "))
        if guess==x:
            print('Your ',count,'guess is correct.')
            y=input(' Do you want to try again? y/n')
            if y=='y' or y=='Y':
                #x=random.randrange(1,101) OR
                x=randrange(1,101)
                count=0
                continue
            else:
                break
        elif guess<x:
            print('Guess is less than the number')
        else:
            print('Guess is more than the number')
        count+=1
    if count>=7:
        print('Your chance is over. The Number is',x)
    
print("Let's play the number guessing game!")   
guessnum()