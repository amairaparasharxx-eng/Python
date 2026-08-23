x=5
if type(x) is int:
    print(True)
else:
    print(False)
y=5.5
if type(y) is not float:
    print(True)
else:
    print(False)
a=20
b=10
if a is b:
    print("a and b same identity.")
c=30
if a is not c:
    print("a and c have different identity.")