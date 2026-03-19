# Method overriding (polymorphism)
# same method name, different behavior in subclass

class Animal:
    def sound(self):
        print("Some generic sound")

class Cat(Animal):
    def sound(self):
        print("meow")

a = Animal()
c = Cat()

a.sound()
c.sound()
