class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")
        else:
            print("insufficient balance or invalid amount!")
    
account = BankAccount("Maanya", 1000000000)
print("Account Owner:", account.owner)
print("Initial balance: ", account.get_balance())
account.deposit(2000)
account.withdraw(100)
