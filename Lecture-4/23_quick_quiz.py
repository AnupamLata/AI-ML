class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 60:
            return "pass"
        else:
            return "fail"

s = Student("Ravi", 55)
print(s.result())            

students = [
   Student("aniket", 80),
   Student("ravi", 45),
   Student("anu", 90),
   
]
for s in students:
    if s.marks >= 60:
        print(s.name)
