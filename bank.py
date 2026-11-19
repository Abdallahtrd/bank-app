from account import Account
import secrets

class Bank:
    def __init__(self):
        self.account_storage = {}


    def create_account(self,pin,name):
        prefix = '534'
        
        while True:
            temp_number = prefix + str(secrets.randbelow(10_000_000)).zfill(7)
            if temp_number in self.account_storage:
                continue
            else:
                break

        account_object = Account(0,pin,temp_number,name)
        self.account_storage[temp_number] = account_object
        return account_object

    def account_retrieve(self,account_to_retrieve):
        if account_to_retrieve in self.account_storage:
            yes = self.account_storage[account_to_retrieve]
            return yes
        else:
            return None 

