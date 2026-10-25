class parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age

ob1=parrot("Blue", 10)
ob2=parrot("Woo", 15)

print("Blu is a {}".format(ob1.species))
print("Woo is also a {}".format(ob2.species))

print("{} is {} years old".format(ob1.name, ob1.age))
print("{} is {} years old".format(ob2.name, ob2.age))