class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

"""Represents a bank account with deposit and withdrawal operations."""

class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=balance

    def deposit(self,amount): 
        """Deposit money into the account."""
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else: raise InvalidAmountError("Deposit amount must be positive.")
            

    def withdraw(self, amount):
      """Withdraw money from the account."""
      if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be positive.")

      if amount > self.balance:
        raise InsufficientFundsError("Insufficient funds for withdrawal.")
      self.balance -= amount
      print(f"Withdrew {amount}. New balance: {self.balance}")
        
    def __str__(self):
        return( f"Account Number: {self.account_number},"
       f" Account Holder: {self.account_holder_name}, "
        f"  Balance: {self.balance}")
    
class CurrentAccount(BankAccount):
    def __init__(self,account_number,account_holder_name,balance,overdraft_limit):
        super().__init__(account_number,account_holder_name,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
            

        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError("Insufficient funds for withdrawal, including overdraft limit.")
            
    
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self,account_number,account_holder_name,balance,minimum_balance=5000):
        super().__init__(account_number,account_holder_name,balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount ):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
            return
        if self.balance - amount < self.minimum_balance:
            raise InsufficientFundsError("Withdrawal would violate minimum balance requirement.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")        


try:
    sa = SavingsAccount(101, "Alice", 10000)

    print(sa)

    sa.deposit(2000)

    sa.withdraw(6000)

    sa.withdraw(2000)   # Should raise exception

except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)



try:
    ca = CurrentAccount(102, "Bob", 5000, 3000)

    print(ca)

    ca.withdraw(7000)

    ca.withdraw(2000)

except (InvalidAmountError, InsufficientFundsError) as e:
    print(e)    
    sa = SavingsAccount(101, "Alice", 10000)
ca = CurrentAccount(102, "Bob", 5000, 3000)

print(isinstance(sa, SavingsAccount))
print(isinstance(sa, BankAccount))

print(isinstance(ca, CurrentAccount))
print(isinstance(ca, BankAccount))

print()

print(issubclass(SavingsAccount, BankAccount))
print(issubclass(CurrentAccount, BankAccount))
print(issubclass(SavingsAccount,BankAccount))