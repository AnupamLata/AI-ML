# Create a base class Employee with attribute salary. Inherit it in class Manager and add bonus.

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def display(self):
        print(f"salary is : {self.salary} and bonus is : {self.bonus}")  

m = Manager(5000, 1000)

m.display()
