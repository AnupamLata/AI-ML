# Create a class Person with attributes name and age. Inherit it in class Student and add roll_no.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age,  roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print(f"name: {self.name} \nage: {self.age} \nroll_no: {self.roll_no}") 


s = Student("Anupam", 21, 165)

s.display()
            
