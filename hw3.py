name=input("Enter your name: ")
clubname=input("Enter club name: ")
print("------------------------------------------------")
memberno=4
pointsearned=121
eventcount= 10
meetinghours=3.5
active=True
print("Name :", name, end="  ")
print("Data Type : ", type(name))
print("Club Name :", clubname, end="  ")
print("Data Type : ", type(clubname))
print("Points Earned  :", pointsearned, end="  ")
print("Data Type : ", type(pointsearned))
print("Member Number :", memberno, end="  ")
print("Data Type : ", type(memberno))
print("Event Count :", eventcount, end="  ")
print("Data Type : ", type(eventcount))
print("Meeting Hours :", meetinghours, end="  ")
print("Data Type : ", type(meetinghours))
print("Active Status :", active, end="  ")
print("Data Type : ", type(active))
print("------------------------------------------------")
memberno1=str(memberno)
pointsearned1=str(pointsearned)
eventcount1=str(eventcount)
meetinghours1=str(meetinghours)
active1=str(active)
first3=name[0:3]
lastletter=name[-1]
badgecode=first3+lastletter
revclubname=clubname[::-1]
print("First 3 letters of Name : ", first3)
print("Last letter of Name : ", lastletter)
print("Badge Code : ", badgecode)
print("Reversed Club Name : ", revclubname)
l1= "NAME:", name.upper() + " || CLUB NAME:", clubname.upper()
l2= "BADGE CODE:", badgecode.upper() + " || MEMBER NUMBER:", memberno1
l3= "MEETING HOURS:", meetinghours1 + " || EVENT COUNT:", eventcount1
l4= "POINTS EARNED:", pointsearned1 + " || ACTIVE STATUS:", active1
l5= "SECRET CLUB NAME:", revclubname.upper()
print("------------------------------------------------")
print("                 CLUB CARD                      ")
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print("------------------------------------------------")