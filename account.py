class Account:
    def __init__(self,balance,pin,account_number,name):
        self.balance = balance
        self.pin = pin
        self.account_number = account_number
        self.history = []
        self.name = name
       
    def deposit(self,amount):
        if amount <= 0:
            #This part makes sure the amount to be deposited is eligible in this case higher than zero
            print("Deposits must be greater than 0")
            return 
        #This part deposits the amount into the account and records it.
        self.balance += amount
        checker = ("deposits",amount)
        self.transaction_recorder(checker)
        return checker
    
    def withdraw(self, amount):
        #This checks if the amount entered is valid for transaction
        if amount <= 0:
            print("You can't withdraw negative amounts!!")
            return
        
        #This part checks if the balance allows for withdrawal
        if amount <= self.balance:
            #If this part runs it means a withdrawal was successful
            #This part also returns the withdrawal transation and its amount 
            self.balance-=amount
            checker = ("withdrawals",amount)
            self.transaction_recorder(checker)
            return checker 
        else:
            #This part means there's no funds to withdraw
            print("Insufficient Funds")
            return

    #This method adds the transaction to history
    def transaction_recorder(self,record):
        self.history.append(record)
        
    def verify_pin(self,received_pin):
        #This method verifies the pin
        if received_pin == self.pin:
            return True
        else:
            return False


    