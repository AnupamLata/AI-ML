# class methods

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
       print(f"storage type = {cls.storage_type}")

def get_info(self):
    print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")  


l1 = Laptop("16gb", "512gb")

print(Laptop.get_storage_type())  #or
Laptop.get_storage_type()
l1.get_storage_type()

       
