class Account:
    def __init__(self,balance,pin,account_number):
        self.balance = balance
        self.pin = pin
        self.account_number = account_number
        
    def deposit(self,amount):
        if amount <= 0:
            print("Deposits must be greater than 0")
            return

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("You can't withdraw negative amounts!!")
            return
        
        if self.balance >= amount:
            self.balance-=amount
        else:
            print("Insufficient Funds")