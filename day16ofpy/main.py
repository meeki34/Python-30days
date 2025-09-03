# create a python Banking program 

def show_balance(balance):
    print(f"Your current balance is ₹{balance:.2f}")

def deposit(balance):
    print("------------------------------------")
    amount = float(input("Enter the amount to deposit: "))
    print("------------------------------------")
     
    if amount <= 0:
        print("------------------------------------")
        print("That is not a valid amount. Please enter a positive number.")
        print("------------------------------------")
        return balance
    else:
        balance += amount
        print(f"You have deposited ₹{amount:.2f}")
        print(f"Your new balance is ₹{balance:.2f}")
        return balance


def withdraw(balance):
    print("------------------------------------")
    amount = float(input("Enter the amount to withdraw: "))
    print("------------------------------------")
    if amount > balance:
        print("Insufficient funds. Please enter a valid amount.")
        return balance
    elif amount <= 0:
        print("That is not a valid amount. Please enter a positive number.")
        return balance
    else:
        balance -= amount
        print(f"You have withdrawn ₹{amount:.2f}")
        print(f"Your new balance is ₹{balance:.2f}")
        return balance

def main():
    balance = 0 
    is_running = True

    while is_running:
        print("------------------------------------")
        print("Banking program")
        print("------------------------------------")
        print("\nWelcome to the bank of python")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("------------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice")

    print("Thank you for using the bank of python")

if __name__ == "__main__":
    main()