import math
import random
randomno=random.randint(1,10)
print(f"Your lucky number is {randomno}! \n")
funchoice=["Walk","Skipping","Hopskotch","Badminton"]
choice1=random.choice(funchoice)
print("Your Fun Activity is", choice1)
print()
print("GUESSING GAME")
guessno=random.randint(1,5)
print("The number can be from 1-5")
while True:
    userno=int(input("Guess a number: "))
    if userno==guessno:
        print("You Guessed it!!")
        break
    else:
        print("Try Again!!")
        continue
print()
newno=float(input("Enter a Decimal Number: "))
print("CEIL: ",math.ceil(newno))
print("FLOOR: ", math.floor(newno))
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
print("FabSign:", math.fabs(n1))
print("FabSign:", math.fabs(n2))
print("Copy Sign: ", math.copysign(n1,n2))
print("GCD: ", math.gcd(n1,n2))
