from bank import Bank
user = Bank()
user_2 = Bank()
account = user.create_account(2223)

print(account)
print(account.account_number)

#Account that exists
print(user.account_retrieve(account.account_number))