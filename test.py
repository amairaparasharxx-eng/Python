scorepair= {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}
total=0
for name in scorepair:
    total+=scorepair[name]
    avg=total/5
print(avg)

lowest=scorepair.min(scorepair.values(), key= scorepair.get())
highest=max(scorepair.values(), key=scorepair.get())
print(f"Highest: {highest}, and Lowest: {lowest}")

student=input("Enter the name of the student you want to search for: ")
score=scorepair.get(student)
if score is None:
    print("student not found!!!!")
else:
    print(f"Found!!!{student}'s score is {score}")
