import random
secretno=random.randint(1,10)
while True:
    userno=int(input("Enter a number from 1-10 \n"))
    if userno==secretno:
        print("You have Won!!")
        print(f"The number was {secretno}")
        break
    else:
        print("Try Again!!")
