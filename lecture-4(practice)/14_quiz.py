class Student:
    def __init__(self, name , marks):
        self.name = name
        self.__marks = marks

    def display(self):
        print("Marks = ", self.__marks)

s1 = Student("john", 100)
s1.display()        
