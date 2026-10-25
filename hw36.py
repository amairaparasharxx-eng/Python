grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Evan": 88
}

total = 0
for score in grades.values():
    total += score

average = total / len(grades)
print(f"Class Average: {average}")


top_name = ""
top_score = 0

for name, score in grades.items():
    if score > top_score:
        top_score = score
        top_name = name

print(f"Highest Scorer: {top_name} with a score of {top_score}")


search_name = input("Enter a student name to look up: ")
student_score = grades.get(search_name, "Not found")

print(f"Result: {student_score}")
