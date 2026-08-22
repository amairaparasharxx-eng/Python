print("---------------SMART SCHOOL DAY PLANNER---------------")
print("ANSWER THREE QUESTIONS AND I WILL PLAN YOUR DAY!")

day=input("WHAT DAY IS IT?(MONDAY-SUNDAY):").strip().upper()
weather=input("WHAT IS THE WEATHER?(SUNNY/RAINY/CLOUDY):").strip().lower()
homework=input("IS YOUR HOMEWORK COMPLETE?(YES/NO):").strip().capitalize()

print(f"YOUR PLAN FOR {day}: ")
print("-"*30)

if day in ("SATURDAY", "SUNDAY"):
    print("DAY TYPE IS WEEKEND, SO ENJOY YOUR FREE TIME!")
elif day=="MONDAY":
    print("DAY TYPE IS FIRST DAY OF WEEK, PACK YOUR WEEKLY PLANNER!")
elif day=="FRIDAY":
    print("DAY TYPE IS LAST SCHOOL DAY, READ LIBRARY BOOKS!")
elif day in ("TUESDAY", "WEDNESDAY", "THURSDAY"):
    print("DAY TYPE IS REGULAR SCHOOL DAY, STAY FOCUSED!")
else:
    print("DAY TYPE NOT RECOGNIZED, PLEASE CHECK AGAIN!")

if weather=="sunny" and homework=="Yes":
    print("AFTER SCHOOL HEAD TO PARK, GREAT WEATHER AND HOMEWORK COMPLETE!")

if weather=="rainy" or weather=="cloudy":
    print("WEATHER TIP: PACK AN UMBRELLA, IT MAY GET WET OUTSIDE!")

if not homework=="Yes":
    print("HOMEWORK NOT DONE YET, FINISH IT BEFORE GOING OUT!")

if weather=="rainy" and not(homework=="Yes"):
    print("BEST PLAN: STAY IN FINISH HOMEWORK AND WATCH YOUR FAV SHOW!")
elif weather=="sunny" and homework=="Yes" and not(day in ("SATURDAY", "SUNDAY")):
    print("BEST PLAN ALL SET FOR GREAT SCHOOL DAY, YOU ARE PREPARED!")
elif day in ("SATURDAY", "SUNDAY") and weather=="sunny":
    print("BEST PLAN, PERFECT WEEKEND WEATHER HEAD OUTSIDE AND HAVE FUN!")
else:
    print("BEST PLAN, TAKE IT ONE STEP AT A TIME YOU HAVE GOT THIS!")
print()
print("PLAN COMPLETE!!! HAVE A WONDERFUL DAY!!!")