# Object-Oriented Programming: Classes and Objects

class Dog:
    # __init__ is a special method that runs automatically when you create
    # a new object from this class - it sets up the initial data
    def __init__(self, name, breed):
        self.name = name    # attribute - data that belongs to this object
        self.breed = breed

    # a method - a function that belongs to the class, and can use self
    # to access this object's own data
    def bark(self):
        print(f"{self.name} says Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")


# Creating objects (instances) from the class
my_dog = Dog("Rex", "Labrador")
another_dog = Dog("Bella", "Poodle")

my_dog.bark()          # Rex says Woof!
my_dog.describe()      # Rex is a Labrador

another_dog.bark()     # Bella says Woof!
another_dog.describe() # Bella is a Poodle

print(my_dog.name)     # Rex - you can access attributes directly too

# 1. Create a BankAccount class with:
#    - attributes: owner_name, balance (starts at 0)
#    - a deposit(amount) method that adds to balance
#    - a withdraw(amount) method that subtracts from balance
#    - a check_balance() method that prints the current balance

class BankAccount:
    # First Version
    # def __init__(self, owner_name, balance):
    #     self.owner_name = owner_name
    #     self.balance = balance
    
    # def deposit(self, amount):
    #     self.balance += amount

    # def withdraw(self, amount):
    #     self.balance -= amount

    # def check_balance(self):
    #     print(f"Balance: {self.balance}")

    # Improved Version
    """A simple bank account that supports deposits and withdrawals."""
    def __init__(self, owner_name: str, balance: float = 0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def check_balance(self) -> None:
        print(f"Balance: {self.balance}")


# test it:
account = BankAccount("Tuan", 0)
account.deposit(100)
account.withdraw(30)
account.check_balance()  # should print something like "Balance: 70"