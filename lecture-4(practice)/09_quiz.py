# Create a base class Shape with a method draw(). Override it in a derived class Circle.

class Shape:
    def draw(self):
        print("draw a shape")

class Circle(Shape):
    def draw(self):
        print("draw a circle")  

c = Circle()
c.draw()              
