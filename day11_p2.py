class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("The animal makes a sound.")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says: Woof! Woof!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says: Meow! Meow!")


# -------------------------
# Testing
# -------------------------

dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print(dog)
dog.speak()

print()

print(cat)
cat.speak()



class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(issubclass(Dog, Animal))
print(issubclass(SavingsAccount, CurrentAccount))
print(issubclass(Dog, Cat))