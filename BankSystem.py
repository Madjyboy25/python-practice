balance=0
transactions={}
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transactions History")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        transactions[len(transactions)+1] = f"Deposited: {amount}"
        print(f"Deposited {amount}. New balance: {balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print(f"Insufficient funds! Current balance: {balance}")
        else:
            balance -= amount
            transactions[len(transactions)+1] = f"Withdrew: {amount}"
            print(f"Withdrew {amount}. New balance: {balance}")
    elif choice == '3':
        print(f"Current balance: {balance}")
    elif choice == '4':
        print("Transaction History:")
        for key, value in transactions.items():
            print(f"{key}: {value}")
    elif choice == '5':
        print("Exiting the program")
        break
    else:
        print("Invalid choice, Please try again! Type a number between 1-5.")