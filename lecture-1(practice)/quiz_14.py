# Create a class Car with attributes brand and price . Initialize them using a constructor and display the details

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price 

    def display(self):
        print(f"car brand is {self.brand} and price is {self.price}")

c1 = Car("ford", 32000)
c1.display()        



     
