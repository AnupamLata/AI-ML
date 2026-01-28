# lets define name every student

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Rahul", 7.0)
stu2 = Student("Anupam", 8.2)
stu3 = Student("Aniket", 8.9)  

print(stu1.name, "=" , stu1.cgpa)
print(stu2.name)
print(stu3.name)
