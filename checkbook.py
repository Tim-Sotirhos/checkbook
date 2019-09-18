print("~~~ Welcome To Your Terminal Checkbook! ~~~\n")

selection = "Enter your choice: "

def menu():
    print("How may I help you today?\n") 
    print("Please select one of the following options:\n")
    print("1.) View current balance\n2.) Record a debit (withdrawal)\n3.) Record a credit (deposit)\n4.) Exit\n")

# function open and reads text file
def read_balance():
    f = open("balance_checkbook.txt", "r")
    balance = f.read()
    return balance

# function open and writes text file
def write_balance(new_balance):
    f = open("balance_checkbook.txt", "w")
    f.write(str(new_balance))

# function to make withdraw
def withdraw_balance(withdraw_amount):
    current_amount = read_balance()
    balance = int(current_amount) - int(withdraw_amount)
    write_balance(str(balance))

# function to deposit
def deposit_balance(deposit_amount):
    current_amount = read_balance()
    balance = int(current_amount) + int(deposit_amount)
    write_balance(str(balance))

# function to display menu and awaits a user input, then displays menu again
def main_menu():
    menu()
    choice = input(selection)
    print("\n")

    if choice == "1":
        print("You currently have a balance of $" + read_balance())
        print("\n")
        main_menu()

    elif choice == "2":
        withdraw_amount = input("Enter an amount to withdraw: $")
        print("\n")
        if int(read_balance()) > 0 and int(read_balance()) - int(withdraw_amount) > 0:
            withdraw_balance(withdraw_amount)
            print("Thank you for your $" + withdraw_amount + " withdrawl. Your current balance is $" + read_balance() + ".")
            print("\n")
        else:
            print("\nSorry you may not continue with the amount entered. Please enter a new amount:  \n")      
        
        main_menu()

    elif choice == "3":
        deposit_amount = input("Enter an amount to deposit: $")
        print("\n")
        deposit_balance(deposit_amount)
        print("Thank you for your $" + deposit_amount + " deposit. Your new total available balance is $" + read_balance() + ".")
        print("\n")
        main_menu()

    elif choice == "4":
        print("Thank you we appreciate your business and have a great day!")
    
    else:
        print("You have selected a non valid choice, please try again.")
        print("\n")
        main_menu()

main_menu()
