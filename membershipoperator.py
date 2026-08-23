print("Enter marks obtained in 5 subjects")
eng=int(input("ENGLISH:"))
math=int(input("MATH:"))
hindi=int(input("HINDI:"))
comp=int(input("COMPUTERS:"))
sci=int(input("SCIENCE:"))
total=eng+math+hindi+comp+sci
avg=total/5
validrange=range(0,101)
if avg not in validrange:
    print("Invalid Input!!")
elif avg in range(91,101):
    print("Grade A1")
elif avg in range(81,91):
    print("Grade A2")
elif avg in range(71,81):
    print("Grade B1")
elif avg in range(61,71):
    print("Grade B2")
elif avg in range(51,61):
    print("Grade C1")
elif avg in range(41,51):
    print("Grade C2")
elif avg in range(31,41):
    print("Grade D1")
elif avg in range(21,31):
    print("Grade D2")
elif avg in range(0,21):
    print("Grade E")

