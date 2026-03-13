# Create a base class Vehicle with attribute type. Create a child class Bike with attribute brand.

class Vehicle:
    def __init__(self, type):
        self.type = type

class Bike(Vehicle):
    def __init__(self, type, brand):
        super().__init__(type)
        self.brand = brand

    def display(self):
        print(f"vehicle type is : {self.type} and vehicle brand is : {self.brand}") 

b1 = Bike("2 wheeler", "nike")
b1.display()         
