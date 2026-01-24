# This is a simple bank account management system using Class in Python.
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"{self.name}'s balance: {self.balance}")

    def transaction_history(self):
        if self.transactions:
            print(f"{self.name}'s Transaction History:")
            for t in self.transactions:
                print("-", t)
        else:
            print("No transactions yet.")


# -------- ACCOUNT STORAGE --------
accounts = []


# -------- CREATE ACCOUNT FUNCTION --------
def CreateAccount():
    name = input("Enter account holder's name: ")

    # Check ONLY here if account already exists
    for account in accounts:
        if account.name == name:
            print("An account with this name already exists.")
            return

    new_account = BankAccount(name)
    accounts.append(new_account)
    print(f"Account created successfully for {name}.")


def find_account(name):
    for account in accounts:
        if account.name == name:
            return account
    return None


# -------- MAIN PROGRAM --------
while True:
    print("\nWelcome to the Bank System")
    print("-------------------------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        CreateAccount()

    elif choice in ["2", "3", "4", "5"]:
        name = input("Enter account holder's name: ")
        account = find_account(name)

        if account is None:
            print("Account not found.")
            continue

        if choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "4":
            account.check_balance()

        elif choice == "5":
            account.transaction_history()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1–6.")
