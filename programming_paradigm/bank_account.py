class BankAccount :

    def  __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
    
    def deposit (self, amount):
        amount = int(input("how much would you like to deposit : "))
        self.account_balance += amount

    def  withdraw(self, amount):
        amount = int(input("how much would you like to withdraw :"))
        while True :
            if self.account_balance < amount:
                print (" you do nit have the money to withdraq the amount ")
                False
            else :
                self.account_balance -= amount
                print (f"ypu have withdrawn {amount}, the balaance is now {self.account_balance}")
                break

    def display_balance(self):
        print(self.account_balance)

