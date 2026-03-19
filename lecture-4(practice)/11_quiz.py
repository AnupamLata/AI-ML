# Create two classes Cat and Dog with a method sound() and demonstrate polymorphism.

class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks") 

def make_sound(animal):
    animal.sound()

c = Cat()
d = Dog()  

make_sound(c)
make_sound(d)
