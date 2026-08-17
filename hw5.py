temperature = int(input("Enter today's temperature in Celsius: "))
if temperature < 20:
    activity = "indoor reading"
    print("It is cool today.")
    print("Do", activity)
else:
    activity = "outdoor play"
    print("It is warm today.")
    print("Do", activity)
israining = input("Is it raining today? (yes/no): ")
if israining == "yes":
    print("Choose an indoor activity or carry an umbrella!")
homeworktime = int(input("Enter homework time in minutes: "))
if homeworktime > 60:
    needsbreak = "yes"
    print("You have a long homework session today.")
    print("Take a short break before your", activity)
else:
    needsbreak = "no"
    print("Homework time is short today.")
    print("No long break needed before your", activity)
hasfreetime = input("Do you have free time today? (yes/no): ")
if hasfreetime == "yes":
    finaltask = "hobby time"
    print("You have free time today.")
    print("Enjoy your", finaltask)
else:
    finaltask = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", finaltask)
print("")
print("Daily activity check complete!")
print("-------------------DAILY ACTIVITY PLANNER-----------------------")
print("Temperature:", temperature)
print("Activity Chosen:", activity)
print("Raining:", israining)
print("Study Break Needed:", needsbreak)
print("Final Task:", finaltask)
print("----------------------------------------------------------------")
