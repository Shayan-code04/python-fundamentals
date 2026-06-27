def create_account(**kwargs):
    # Use provided kwargs or prompt the user for missing values
    name = kwargs.get('name') or input("Enter your name: ")
    # if balance provided in kwargs, ensure it's a float
    balance = float(kwargs.get('balance')) if 'balance' in kwargs else float(input("Enter your initial balance: ") or 0.0)
    pin = kwargs.get('pin') or input("Enter your PIN: ")

    account = {
        'name': name,
        'balance': balance,
        'pin': str(pin),
    }
    # Keep any extra details passed in kwargs
    for key, value in kwargs.items():
        if key not in account:
            account[key] = value
    return account


def atm_menu(account):
    print(f"Welcome, {account['name']}.")
    while True:
        print("\nATM Menu")
        print("1. View balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            print(f"Current balance: {account['balance']}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account['balance'] += amount
            print(f"Deposited {amount}. New balance: {account['balance']}")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount > account['balance']:
                print("Insufficient funds.")
            else:
                account['balance'] -= amount
                print(f"Withdrawn {amount}. New balance: {account['balance']}")
        elif choice == '4':
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    # Call without kwargs so the user is prompted, or pass values like:
    # account = create_account(name="Raj", balance=100.0, pin="1234")
    account = create_account()
    atm_menu(account)
