# Create a class Bird with a method fly(). Override the method in class Sparrow.

class Bird:
    def fly(self):
        print("bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("sparrow can fly")    

s = Sparrow()

s.fly()
