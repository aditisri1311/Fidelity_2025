'''Make a class customer with 2 methods as deposit and withdraw'''
class Customer:
    def __init__(self, balance, name ):
        self.balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}. Current balance: {self.balance}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.name}'s current balance: Rs{self.balance}")
