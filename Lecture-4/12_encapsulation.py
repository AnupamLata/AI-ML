class BankAccount:
    def __init__(self, name, balance):
        self.name = name   #public
        self._balance = balance   #protected attributes _
        # self.__balance = balance #private attributes 


acc1 = BankAccount("aniket Yadav", 100_000)

print(f"{acc1.name} has balance = {acc1._balance}")
