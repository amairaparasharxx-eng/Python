name=input("Enter your name: ")
gadget=input("Enter the name of your favourite gadget: ")

agentno=7
speedrating=9.5
missoncount=12
height=1.65
isactive=True

#Data Types using type function
print("Data Type of Name: ", type(name))
print("Data Type of Gadget: ", type(gadget))
print("Data Type of Agent Number: ", type(agentno))
print("Data Type of Speed Rating: ", type(speedrating))
print("Data Type of Mission Count: ", type(missoncount))
print("Data Type of Height: ", type(height))
print("Data Type of Is Active: ", type(isactive))

#Typecasting
speedrating1=int(speedrating)
missoncount1=float(missoncount)
agentno1=str(agentno)
print(speedrating1)
print(missoncount1)
print(type(agentno1))

#string operation
first3=name[0:3]
lastletter=name[-1]
codename= first3+lastletter
print("First 3 letters of Name: ", first3)
print("Last Letter of Name: ", lastletter)
print("Secret Codename: ", codename)
revgadget=gadget[::-1]

