current_number = 2
account_number = ''
def lcg(current_number):
    
    multiplier = 7
    c = 20
    m = 10
    step_1 = multiplier * current_number + c
    step_1 = step_1 % m
    current_number = step_1

    return step_1

current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)
current_number = (lcg(current_number))
account_number += str(current_number)

print(f"Your account number is: {account_number}")