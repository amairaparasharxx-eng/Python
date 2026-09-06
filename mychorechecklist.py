totaltask=4
ogcount=totaltask
print(f"You have {totaltask} task to finish today")
completed=0
taskno=1
while taskno<=totaltask:
    if taskno==1:
        nexttask="Make your Bed"
    elif taskno==2:
        nexttask="Feed the pet"
    elif taskno==3:
        nexttask="Take out the trash"
    else:
        nexttask="Wash the dishes"
    ans=input(f"Have you finished {nexttask}?(YES/NO): ")
    if ans=="YES":
        completed += 1
        taskno+=1
        print("Great Job Task Completed!!")
    else:
        print("Okay! Finish and Check again!!")
    print("Pending Task",totaltask-completed)
    print()
print("-------------ALL TASK COMPLETE!!----------------")
print("GREAT WORK, FINISHING YOUR ENTIRE CHECKLIST TODAY!!")
print("------------------------------------------------")

#Infinite Loop
print("Now, let's safely peek at a infinite loop!!")
testvalue=0
safetycount=0
while testvalue<=0:
    print("The condition never changes so it would run forever!!")
    safetycount+=1
    if safetycount==3:
        print("Stopping here on purpose. A real infinite loop never stops on its own...")
        break
print("-----------------------TASK CHECKLIST SUMMARY---------------------------")
print("TASK ASSIGNED TODAY: ",ogcount)
print("TASK COMPLETED: ", completed)
print("PENDING TASKS: ", totaltask-completed)
print("------------------------------------------------------------------------")
