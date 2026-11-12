n=4
guess=input("Total points: 1+2+3+4=")

input("Formula: one calculation. Press Enter to run.")
total=n*(n+1)//2
print(" Total = ", total, " Steps = 1")

input("Loop: adds one student at a time. Press Enter to run.")
total=0
for student in range(1,n+1):
    total+=student
print(" Total = ", total, " Steps = ", n)

input("Double Loop: Counts every single point. Press Enter to run.")
total=0
steps=0
for student in range(1, n+1):
    for point in range(1, student+1):
        total+=1
        steps+=1
print(" Total = ", total, " Steps = ", steps, "  Your guess was: ",guess)