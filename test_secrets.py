import secrets
storage = {}
prefix = '534'
number = str(secrets.randbelow(10_000_000)).zfill(7)
account_number = prefix + number

storage[account_number]=int(account_number)
print(storage)
