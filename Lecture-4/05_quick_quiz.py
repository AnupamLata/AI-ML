# for return

class Student:
    def __init__(self, name, cgpa):  #parameterized constructor
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("khushi ", 8.1)
stu2 = Student("Anupam", 8.2)
stu3 = Student("Aniket", 8.3)      

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
print(f"{stu2.name} has cgpa = {stu1.get_cgpa()}")
