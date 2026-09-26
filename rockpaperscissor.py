import random
playing=True
while playing==True:
    choices=["rock", "paper", "scissor"]
    computerchoice=random.choice(choices)
    userchoice=input("enter a choice: rock, paper, scissor").strip().lower()
    if userchoice==computerchoice:
        print("Tie!!")
    elif userchoice=="rock":
        if computerchoice=="scissor":
            print("You Win!!")
        else:
            print("You Lost..")
    elif userchoice=="paper":
        if computerchoice=="rock":
            print("You Win!!")
        else:
            print("You Lost...")
    elif userchoice=="scissor":
        if computerchoice=="paper":
            print("You Win!!")
        else:
            print("You Lost...")
    playagain=input("Do you want to play again?(yes/no):").strip().lower()
    if playagain!="yes":
        playing=False
    else:
        playing=True
    