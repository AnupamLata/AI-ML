# Create a class MathOperations with a method add() that can add two or three numbers.

class MathOperations:
    def add(self , a, b, c=0):
        result = a + b + c

        print("sum = " , result)

m = MathOperations()
m.add(3,4)
m.add(3,4, 2)
