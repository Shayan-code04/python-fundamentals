def create_account(**kwargs):
    account = {
        'name': kwargs.get('name', 'Guest'),
        'balance': kwargs.get('balance', 0.0),
        'pin': kwargs.get('pin', '0000'),
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


if __name__ == '__main__':
    account = create_account(name='Raj', balance=250.75, pin='4321', account_type='savings')
    atm_menu(account)
