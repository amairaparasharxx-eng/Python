class MyClass:
    __privateVar=27
    def __privMethod(self):
        print("I'm inside class MyClass.")
    def hello(self):
        print("The private variable value is",MyClass.__privateVar)

ob1=MyClass()
ob1.hello()
ob1.__privMethod
