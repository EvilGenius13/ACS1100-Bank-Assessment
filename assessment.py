#going to write out to a new file since I have changed the data layout
#which would then be used for future iterations

import json
bank_accounts = {}
json.dumps = bank_accounts
green = '\033[1;92m' 
#put colour back to normal
reset = "\033[0;0m"
red = '\033[1;91m'

#get data from data.txt
def pull_data(filename):
    
    infile = open(filename, "r").readlines()
    for line in infile:
        split_list = line.rstrip().split(",")
       #taken from example 10
        username = split_list[0]
        password = split_list[1]
        name = split_list[2]
        balance = split_list[3]
        #create new list with username as key | password, name, balance as value
        bank_accounts[username] = password, name, balance

    return bank_accounts
 

#push data to file
def push_data(filename):
    push_string = ""
    for account in bank_accounts:
        push_string = (f"{push_string}{account}")
        for value in bank_accounts[account]:
            push_string = (f"{push_string},{value}")  
        push_string = (f'{push_string}\n') 
    with open(filename, "w") as outfile:
        outfile.writelines(push_string.rstrip())
    outfile.close()

#login loop
def user_login():
    print(f"{red}Welcome to EvilGenius Financial")
    print("Where you pay us interest!")
    user_input_one = input(f"{reset}Please enter your username: ")
    user_input_two = input("Please enter your password: ")

    if user_input_one in bank_accounts:
        user_key_values = bank_accounts[user_input_one]
        if user_key_values[0] == user_input_two:
            banking_loop(user_input_one)
    # catch both wrong user and/or wrong pass 
    if user_input_one not in bank_accounts or user_key_values[0] != user_input_two:
        print("Username or password not found. Please try again")
        return user_login()

#displays bank info and hops back to loop
def show_info(username):
    customer_info = bank_accounts[username]
    print(f"Hello {customer_info[1]}")
    print(f"Your current balance is: {green}${customer_info[2]}")
    return banking_loop(username)

#deposit test
def deposit_money(username):
  customer_info = bank_accounts[username]
  current_balance = customer_info[2]
  print(f"Your current balance is: {green}${customer_info[2]}")
  how_much = input(f"{reset}How much is your deposit?: $")
  current_balance = int(current_balance) + int(how_much)
  print(f"Your new balance is: {green}${current_balance}")
  update_balance(username, current_balance)
  

def withdraw_money(username):
    customer_info = bank_accounts[username]
    current_balance = customer_info[2]
    print(f"Your current balance is: {green}${customer_info[2]}")
    how_much = input(f"{reset}How much is your withdrawal?: $")
    if int(how_much) > int(current_balance):
        print(f"Sorry, you can't withdraw more than you have.")
    else:
        current_balance = int(current_balance) - int(how_much)
        print(f"Your new balance is: {green}${current_balance}")
    update_balance(username, current_balance)
    

def pay_day(username):
    customer_info = bank_accounts[username]
    current_balance = customer_info[2]
    current_balance = int(current_balance) / 1.05
    current_balance = round(current_balance)
    print(f"HAHAHA, Your new balance is {red}{current_balance}")
    print(f"Thank you for your business!")
    update_balance(username, current_balance)
    

def update_balance(username, currentbalance):
    account_check = bank_accounts[username]
    transfer_list = list(account_check)
    transfer_list[2] = currentbalance
    bank_accounts[username] = tuple(transfer_list)
    push_data("finaldata.txt")
    return banking_loop(username)


def banking_loop(username):

        choice = input(f"{reset}Please choose one of the following options\nB to show bank info\nD to deposit\nW to withdraw\nI for interest payment \nQ to quit\nUser Choice: ")
        if choice.upper() == 'B':
            return show_info(username)
        elif choice.upper() == 'D':
            return deposit_money(username)
        elif choice.upper() == "W":
            return withdraw_money(username)
        elif choice.upper() == "I":
            return pay_day(username)
        elif choice.upper() == 'Q':
            print(f"{red}Have a good day!")



pull_data("finaldata.txt")
user_login()
