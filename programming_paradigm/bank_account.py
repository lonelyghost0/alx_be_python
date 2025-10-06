class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
       
    def withdraw(self, amount):
        if self.account_balance < amount:
            print("You do not have enough money to withdraw that amount.")
            return False
        else:
            self.account_balance -= amount
            print(f"You have withdrawn ${amount}. The balance is now ${self.account_balance}.")
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
