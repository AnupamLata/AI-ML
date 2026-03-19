class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def increase_salary(self, amount):
        self.__salary += amount

    def display_salary(self):
        print("salary", self.__salary)

e1 = Employee("ANiket", 5000)
e1.increase_salary(1000)
e1.display_salary()     



