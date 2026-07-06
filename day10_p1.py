class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass



class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.balance=balance

    def deposit(self,amount): 
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else: raise InvalidAmountError("Deposit amount must be positive.")
            

    def withdraw(self, amount):
      if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be positive.")

      if amount > self.balance:
        raise InsufficientFundsError("Insufficient funds for withdrawal.")
      self.balance -= amount
      print(f"Withdrew {amount}. New balance: {self.balance}")
        
    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder_name}, Balance: {self.balance}"