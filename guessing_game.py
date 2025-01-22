'''
from math import *

print(sqrt(9))
print(ceil(3.4))
# print(dir(math))





from random import *

for i in range(10):
    print(randrange(10))
'''


import random


def number_guessing_game():
    secret_number = random.randint(1, 100)
    print('Welcome to the Number guessing game')
    print('Guess a number between 1 and 100')
    guess = None
    while guess != secret_number:
        guess = int(input('Enter your guess: '))
        
        if guess < secret_number:
            print('Too low!')
        elif guess > secret_number:
            print('Too high')
        else:
            print('Congratulations! you got it right')
    
number_guessing_game()
            
