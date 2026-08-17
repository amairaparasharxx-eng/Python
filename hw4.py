tpoint1=50
tpoint2=78
tpoint3=47
tpoint4=82
tpoint5=94
total=tpoint1+tpoint2+tpoint3+tpoint4+tpoint5
avg=total/5
print("TOTAL NUMBER OF POINTS: ", total)
print("AVERAGE OF POINTS: ",avg)
starppoint=5
tstar1=(tpoint1*starppoint)
tstar2=(tpoint2*starppoint)
tstar3=(tpoint3*starppoint)
tstar4=(tpoint4*starppoint)
tstar5=(tpoint5*starppoint)
print()
print("Stars for Team 1: ", tstar1, "⭐")
print("Stars for Team 2: ", tstar2, "⭐")
print("Stars for Team 3: ", tstar3, "⭐")
print("Stars for Team 4: ", tstar4, "⭐")
print("Stars for Team 5: ", tstar5, "⭐")
totalstar=tstar1+tstar2+tstar3+tstar4+tstar5
box=totalstar//25
leftover=totalstar%25
print("TOTAL NUMBER OF STARS:", totalstar)
print("NUMBER OF STAR BOXES PACKED:", box)
print("LEFTOVER STARS:", leftover)
lastweekpoint=270
lastweekstar=lastweekpoint*starppoint
print()
print("COMPARISON OF POINTS:")
print("Better than last week?: ", total>lastweekpoint)
print("Same as last week?: ", lastweekpoint==total)
print("Atleast as good?: ", total>=lastweekpoint)
print("COMPARISON OF STARS")
print("Better than last week?: ", totalstar>lastweekstar)
print("Same as last week?: ", lastweekstar==totalstar)
print("Atleast as good?: ", totalstar>=lastweekstar)
pointfortask=15
total+=pointfortask
totalstar+=(total*starppoint)
print("THE TOTAL NUMBER OF POINTS AFTER ADDING MISSED POINTS:", total)
print("THE TOTAL NUMBER OF STARS AFTER ADDING MISSED POINTS:", totalstar)
minuspoints=32
total-=minuspoints
totalstar-=(total*starppoint)
print("THE TOTAL NUMBER OF POINTS AFTER MINUS POINTS:", total)
print("THE TOTAL NUMBER OF STARS AFTER MINUS POINTS:", totalstar)