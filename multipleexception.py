try:
    n1,n2=eval(int(input("Enter 2 numbers, seperated by a comma: ")))
    result=n1/n2
    print(f"Result is {result}")
except ValueError:
    print("Invalid Value Entered...")
except ZeroDivisionError:
    print("A number cannot be divided by 0...")
except SyntaxError:
    print("The values given should be seperated by a comma...")
else:
    print("No Errors!!")
finally:
    ("This will execute no matter what!!")