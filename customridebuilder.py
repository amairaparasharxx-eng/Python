print("------------------------------------")
print(" WELCOME TO CUSTOM RIDE BUILDER!!")
print("------------------------------------")
print()

print("STEP 1: PICK YOUR VEHICLE:")
print("1- BIKE")
print("2- CAR")
print()
choice=int(input("ENTER 1 OR 2:  "))
print()

if (choice==1):
    print("STEP 2: PICK YOUR BIKE TYPE:")
    print("1- SCOOTY")
    print("2- MOUNTAIN BIKE")
    print()
    biketype=int(input("ENTER 1 OR 2:  "))
    if (biketype==1):
        print("YOU PICKED: SCOOTY")
        print("TOP SPEED: 80 KM/H")
        print("BEST FOR: CITY DRIVES")
    else:
        print("YOU PICKED: MOUNTAIN BIKE")
        print("TOP SPEED: 40 KM/H")
        print("BEST FOR: OFF ROUTE TRAILS")
elif(choice==2):
    print("STEP 2: PICK YOUR CAR TYPE:")
    print("1- SUDAN")
    print("2- SUV")
    print()
    cartype=int(input("ENTER 1 OR 2:  "))
    if(cartype==1):
        print("YOU PICKED: SUDAN")
        print("SEATS: 5 PASSENGER")
        print("BEST FOR: FAMILY TRIP")
    else:
        print("YOU PICKED: SUV")
        print("SEATS: 7 PASSENGERS")
        print("BEST FOR: OFF ROAD ADVENTURES")
else:
    print("THAT WAS NOT A VALID CHOICE!!")
    print("PLEASE ENTER 1 FOR BIKE")
    print("       ENTER 2 FOR CAR")

print()
print("------------------------------------")
print("YOUR CUSTOM RIDE IS READY!!")
print("ENJOY YOUR JOURNEY!!")
print("------------------------------------")