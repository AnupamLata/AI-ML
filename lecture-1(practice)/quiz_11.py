# create a class Student with attributes name and roll_no. Create an object and print the values.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

  
s1 = Student("anupam", 23)
s2 = Student("Aniket", 33) 

print(s1.name)
print(s2.name)
print(s1.roll_no)


