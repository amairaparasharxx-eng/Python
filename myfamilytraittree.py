class family:
    def __init__(self, eye, heightcm):
        self.eye = eye
        self.heightcm = heightcm

    def showtraits(self):
        print("Eye Colour: ", self.eye)
        print("Height in Centimeters: ", self.heightcm)

class kid(family):
    def __init__(self, eye, heightcm, name, age):
        self.name= name
        self.age= age
        super().__init__(eye, heightcm)
    def showtraits(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().showtraits()
    def hobby(self, hobbies):
        print(f"{self.name} loves {hobbies}")

child= kid("brown", 150, "Bob", 9)
child.showtraits()
child.hobby("Reading")

print("Is kid() a subclass of family(): ", issubclass(kid,family))
