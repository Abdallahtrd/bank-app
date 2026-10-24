import secrets
storage = {}
prefix = '534'
def initial_account(prefix):
    number = str(secrets.randbelow(10_000_000)).zfill(7)
    temp_number = prefix + number
    return temp_number
account_number = initial_account(prefix)

while True:
    if account_number in storage:
        new_account_number = str(secrets.randbelow(10_000_000)).zfill(7)
        account_number = prefix + new_account_number
        
    else:
        break
storage[account_number]=int(account_number)
print(storage)
