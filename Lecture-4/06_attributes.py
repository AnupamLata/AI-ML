# attributes
class Student:
    college_name = "ABC college"  # class attributes

    def __init__(self, name, cgpa):
        self.name = name  # instance Attributes
        self.cgpa = cgpa   

stu1 = Student("Khushi" , 8.7)        

print(f"{stu1.name} has cgpa = {stu1.cgpa}")

print("college name : ",Student.college_name)
