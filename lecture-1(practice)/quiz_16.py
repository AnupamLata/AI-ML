# create a base class Animal with a method sound(). Create a derived class Dog that prints " Dog Barks"
 
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# object  create
d = Dog()

# method call
d.sound()             
