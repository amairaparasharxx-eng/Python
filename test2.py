def add(a,b):
    return (a+b)
def subtract(x,y):
    return (x-y)
def multiply(p,q):
    return (p*q)
def divide(h,i):
   return (h/i)
while True:
    try:
        a=float(input("Enter a number: "))
        b=float(input("Enter another number: "))
    except ValueError:
        print("Enter numerical values only.")
        print("Try again.. \n")
        continue
    break
print("Add: ", add(a,b))
print("SUbtract: ", subtract(a,b))
print("Multiply: ", multiply(a,b))
if b==0:
    try:
        divide(a,b)
    except ZeroDivisionError:
        print("A number cannot be divided by 0")
    b=float(input("Enter a non-zero value: "))
print("Divide: ", divide(a,b))