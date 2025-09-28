try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    number += 5
    print(f"The result is: {number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    raise RuntimeError("An error occurred") from e


try:
    numbers = int(input(f"Enter a number: "))
    print(f"The result is: {numbers + 5}")
except Exception as e:
    print("Invalid input. Please enter a valid number.")

# except Exception as e:
#     raise RuntimeError("An error occurred") from e

# bank account

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def get_balance(self):
        print(f"Account balance: {self.balance}")
        return self.balance
    def transfer(self, amount, target_account):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance, target_account.get_balance()

account1 = BankAccount(1000)
account2 = BankAccount(500)

try:
    account1.transfer(200, account2)
except ValueError as e:
    print(f"Error: {e}")
    print(f"Account 1 balance: {account1.get_balance()}")
    print(f"Account 2 balance: {account2.get_balance()}")


