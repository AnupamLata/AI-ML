# for private attributes

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance 

    def get_balance(self):  #getter
        return self.__balance
    
    def set_balance(self, newBalance):  #setter
        self.__balance = newBalance

acc1 = BankAccount("Aniket Yadav", 10_000) 

acc1.set_balance(200_000)
print(acc1.name, acc1.get_balance())
