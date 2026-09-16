def factorial(x):
    """This is a reccursive function to find the factorial of an integer"""
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print(f"Factorial of 1: {factorial(1)}")
print(f"Factorial of 2: {factorial(2)}")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 10: {factorial(10)}")