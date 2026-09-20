try:
    number=int(input("Enter any number: "))
    print(f"number={number}")
except ValueError as ex:
    print("Exception: ", ex)