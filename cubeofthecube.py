def cube(x):
    return x*x*x
def divisible_by_3(x):
    if x%3==0:
        return cube(x)
    else:
        return False
print(divisible_by_3(15))
print(divisible_by_3(7))