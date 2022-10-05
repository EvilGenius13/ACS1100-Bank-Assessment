bank_accounts = {}
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


def banking_loop(username):

    choice = input(f"{reset}Please choose one of the following options\nB to show bank info\nQ to quit\nUser Choice: ")
    if choice.upper() == 'B':
        return show_info(username)
    elif choice.upper() == 'Q':
        print(f"{red}Have a good day!")
    else: 
        print("That is not a valid option")
        return banking_loop(username)





pull_data("data.txt")
user_login()