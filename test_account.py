from account import Account
user_1 = Account(3000,1124,1000000000)
user_1.deposit(2000)
user_1.withdraw(-1222)
print(f"Your Balance is {user_1.balance}")

user_2 = Account(10000,1234,100000002)
user_2.withdraw(2000)
user_2.deposit(0)
print(f"Your balance is {user_2.balance}")

user_3 = Account(0,1111,1002223020)
user_3.deposit(100000)
user_3.withdraw(1000000)
print(f"Your balance is {user_3.balance}")