#Number Guessing Game
#Build a game where the computer picks a secret number between 1 and 50.
#You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. 
# Remaining lives are shown as hearts after each attempt.
import random
number=random.randint(1,50)
for i in range(1,6):
    guess=int(input("enter your guess: "))
    if guess>number:
       print("Hint: Number is lesser than guess")
    elif guess<number:
        print("Hint: Number is greater than guess")
    else:
        print(f"CORRECT!! The number was {number}!!")
        break