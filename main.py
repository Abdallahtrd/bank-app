from bank import Bank
from authentication import Authentication

bank = Bank()
authentication = Authentication(bank)

def dashboard(login_account):
    logout_confirmed = False
    while True:
            print("*"*40)
            print(f"WELCOME {login_account.name}!!! ")
            print(f"ACCOUNT BALANCE N {login_account.balance} ")
            print("*"*40)
            print("1. DEPOSIT ")
            print("2. WITHDRAW ")
            print("3. CHECK HISTORY")
            print("4. LOG OUT")
            choice = input("WHAT WOULD YOU LIKE TO DO?: ").strip()
            if choice.isdigit() is False:
                print("PLEASE INPUT A VALID DIGIT")
                continue
            if choice == "1":
                while True:
                    try:
                        deposit_amount = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT?: ").strip())
                    except ValueError:
                        print("ENTER A VALID AMOUNT")
                        continue
                    login_account.deposit(deposit_amount)
                    break
            elif choice == "2":
                while True:
                    try:
                        withdraw_amount = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW?:  ").strip())
                    except ValueError:
                        print("PLEASE INPUT A VALID DIGIT")
                        continue
                    login_account.withdraw(withdraw_amount)
                    break
            elif choice == "3":
                #I might need the bank as an argument here
                print(f"HERE'S YOUR HISTORY {login_account.history}")
            elif choice == "4":
                
                while True:
                    confirmation = input("ARE YOU SURE YOU WANT TO LOG OUT? (Y/N)").lower().strip()
                    if confirmation == "y":
                        logout_confirmed = True
                        break  
                    
                
                    elif confirmation == "n":
                        break
                    else:
                        print("ENTER VALID INPUT")
                        continue    

            else:
                print("ENTER A VALID INPUT")
                continue

            if logout_confirmed is True:
                break
                        
             
                    


while True:
    print("WELCOME TO ABDALLAHS' BANK")
    print("*"*45)
    print("WHAT WOULD YOU LIKE TO DO?")
    print("1. CREATE AN ACCOUNT ")
    print("2. LOGIN TO ACCOUNT ")
    print("3. EXIT")
    print("*"*45)

    try:
        choice = int(input("PICK AN OPTION: ").strip())
    except ValueError:
        print("You're meant to pick a number twin!!✌️✌️")
        continue

    if choice == 1:
        while True:
            user_name = input("Please Input Your Full Name: ").strip().upper()
            if user_name.replace(" ","").isalpha() == False:
                print("Please Input a valid name")
                continue
            while True:
                pin = input("Please create a PIN (Do not share this number): ").strip()
                if len(pin) != 4:
                    print("ENTER A VALID PIN FORMAT")
                    continue
                if pin.isdigit() is False:
                    print("Invalid Input")
                    continue
                else:
                    break

            account = bank.create_account(pin,user_name)
            print(f"Your Account Details are: NAME: {account.name}, Account Number: {account.account_number}")
            break
    elif choice == 2:
        while True:
            account_numb = input("Please Input Account Number: ").strip()
            login_account = authentication.authenticate_accountnumber(account_numb)
            if login_account is False:
                print("Please Enter a valid account number")
                continue
            while True:
                input_pin = input("Please Input your PIN: ").strip()
                if len(input_pin) != 4 or input_pin.isdigit() is False:
                    print("ENTER A VALID PIN")
                    continue
                else:
                    break
            pin_verifies = authentication.authenticate_account_pin(input_pin,login_account)
            if pin_verifies is False:
                print("Your information is incorrect")
                continue
            dashboard(login_account)
            break

    

    elif choice == 3:
        break

    