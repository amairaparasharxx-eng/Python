class employee:
    def __init__(self):
        print("Employee created.")
    def __del__(self):
        print("Destructed.")

def Createobj():
    print("Making Object...")
    obj=employee()
    print("function end...")
    return obj

print("Calling Createobj() function....")
obj=Createobj()
print("Program end....")
