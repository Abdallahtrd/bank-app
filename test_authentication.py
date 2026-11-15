from bank import Bank
from authentication import Authentication

my_bank = Bank()
authentication = Authentication(my_bank)
user_1 = my_bank.create_account(1234)
user_2 = my_bank.create_account(9902)
print(user_1)
print(user_2)
# For Authenticating account numbers
print("For Authenticating account numbers")
print(authentication.authenticate_accountnumber(user_1.account_number))
print(authentication.authenticate_accountnumber(user_2.account_number))


#THE TESTS
print("THE TESTS")
# correct account number + correct pin
print("correct account number + correct pin")
print(authentication.authenticate_account_pin(1234, user_1))
print(authentication.authenticate_account_pin(9902, user_2))

# correct account number + incorret pin
print("correct account number + incorret pin") 
print(authentication.authenticate_account_pin(9902, user_1))
print(authentication.authenticate_account_pin(1234,user_2))

# incorrect account number this also tests incorrect account number + PIN verification attempted
print("incorrect account number this also tests incorrect account number + PIN verification attempted")
invalid_account = authentication.authenticate_accountnumber(5341223455)
print(authentication.authenticate_account_pin(1223,invalid_account)) 
print(authentication.authenticate_account_pin(1113,invalid_account))


