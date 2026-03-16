# Create a class rectangle with Attributes length and breadth . write a method to calculate and print the area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calc(self):
        return self.length * self.breadth    

t1 = Rectangle(2 , 3) 
print(t1.calc())       
