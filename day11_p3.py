# 1. Exceptions
class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

# 2. Bank hierarchy
class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, minimum_balance=5000):
        super().__init__(account_number, account_holder_name, balance)
        self.minimum_balance = minimum_balance

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_limit = overdraft_limit

# 3. Animal hierarchy
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

# 4. Now the verification — everything is defined above, so this works
sa = SavingsAccount(101, "Alice", 10000)
ca = CurrentAccount(102, "Bob", 5000, 3000)
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(issubclass(Dog, Animal))
print(issubclass(SavingsAccount, CurrentAccount))
print(issubclass(Dog, Cat))