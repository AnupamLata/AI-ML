class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee) :
    def __init__(self, role):
        self.role = role

staff1 = AdminStaff("manager")

print(staff1.role, staff1.start_time, staff1.end_time)
