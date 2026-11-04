class vehicle:
    def __init__(self, mileage, price):
        self.mileage= mileage
        self.price= price
    def showdetail(self):
        print("Mileage: ", self.mileage)
        print("Price: ", self.price)

class car(vehicle):
    def __init__(self, mileage, price, model, color):
        self.model=model
        self.color=color
        super().__init__(mileage, price)
    def showdetail(self):
        print("Model: ", self.model)
        print("Color: ", self.color)
        super().showdetail()

ob1= car(12,2000000, "X50", "black")
ob1.showdetail()

print("Is car a child class of vehicle?: ", issubclass(car, vehicle))