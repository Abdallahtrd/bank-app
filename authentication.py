from bank import Bank

class Authentication:
    def __init__(self,receivedbank_object):
        self.bank = receivedbank_object

    def authenticate_accountnumber(self,received_number):
         check =  self.bank.account_retrieve(received_number)
         if check is None:
             return False
         else:
             return check
    def authenticate_account_pin(self,received_pin,received_account):
        if not received_account:
            return False
        else:
            return received_account.verify_pin(received_pin)
            
