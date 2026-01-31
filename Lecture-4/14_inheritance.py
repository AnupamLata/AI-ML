class Employee:
    start_time = "10am"
    end_time = "6pm"

class Teacher(Employee):
    def __init__(self, subject) :
        self.subject = subject

t1 = Teacher("math")

print(f"{t1.subject} , teachers timing is {t1.start_time} to {t1.end_time}")
