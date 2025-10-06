class BankAccount:

    def  __init__(self, inital_balance = 0):
        self.account_balance = inital_balance
        
    
    def deposit (self, amount):
        self.account_balance += amount

    def  withdraw(self, amount):
        if self.account_balance < amount:
             print (" you do nit have the money to withdraq the amount ")
             return False
        else :
             self.account_balance -= amount
            print (f"ypu have withdrawn {amount}, the balaance is now {self.account_balance}")
            return True

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")

