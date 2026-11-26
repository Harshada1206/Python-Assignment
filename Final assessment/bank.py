
accounts = {}

def create_account():
    account_no = input("Enter account number: ")

    if account_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    balance = float(input("Enter initial deposit: "))

    if balance < 0:
        print("Initial deposit cannot be negative.")
        return

    accounts[account_no] = {
        "name": name,
        "balance": balance
    }

    print("Account created successfully!")

def deposit():
    account_no = input("Enter account number: ")

    if account_no in accounts:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            accounts[account_no]["balance"] += amount
            print("Money deposited successfully!")
        else:
            print("Enter a valid amount.")
    else:
        print("Account not found!")

def withdraw():
    account_no = input("Enter account number: ")

    if account_no in accounts:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= accounts[account_no]["balance"]:
            accounts[account_no]["balance"] -= amount
            print("Money withdrawn successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    account_no = input("Enter account number: ")

    if account_no in accounts:
        print("Account Holder:", accounts[account_no]["name"])
        print("Available Balance:", accounts[account_no]["balance"])
    else:
        print("Account not found!")

def account_details():
    account_no = input("Enter account number: ")

    if account_no in accounts:
        print("\n--- Account Details ---")
        print("Account Number:", account_no)
        print("Account Holder:", accounts[account_no]["name"])
        print("Balance:", accounts[account_no]["balance"])
    else:
        print("Account not found!")

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        account_details()
    elif choice == "6":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
