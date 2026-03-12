# create a class Employee with attributes name and salary. Write a method to Increase salary by 10%

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        self.salary = self.salary + (self.salary * 0.10)
        print(f"name is {self.name} and updated salary is {self.salary}")

e1 = Employee("Aniket", 3000)
e1.increase_salary()    
