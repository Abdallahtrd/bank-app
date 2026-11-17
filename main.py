from bank import Bank
from authentication import Authentication

bank = Bank()
authentication = Authentication(bank)

while True:
    print("WELCOME TO ABDALLAHS' BANK")
    print("*"*45)
    print("WHAT WOULD YOU LIKE TO DO?")
    print("1. CREATE AN ACCOUNT ")
    print("2. LOGIN TO ACCOUNT ")
    print("3. EXIT")
    print("*"*45)

    try:
        choice = int(input("PICK AN OPTION: "))
    except ValueError:
        print("You're meant to pick a number twin!!✌️✌️")
        continue

    if choice == 1:
        pin = input("Please create a PIN (Do not share this number): ")
        account = bank.create_account(pin)
        print(f"Your Account Number is {account.account_number}")

    elif choice == 2:
        
        account_numb = str(input("Please Input Account Number: "))
        login_account = authentication.authenticate_accountnumber(account_numb)
        if login_account is False:
            print("Please Enter a valid account number")
            continue
        input_pin = input("Please Input your PIN: ")
        pin_verifies = authentication.authenticate_account_pin(input_pin,login_account)
        if pin_verifies is False:
            print("Your information is incorrect")
            continue
        print(f"WELCOME USER {login_account.account_number}")

        

    elif choice == 3:
        break