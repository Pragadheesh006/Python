# Python OOP: Demonstrations and Exercises
# Run this script to see outputs. No external files needed.

import math  # For Circle area

# 1. Classes and Instances
print("1. Classes and Instances Example:")
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age=0):  # __init__ example
        self.name = name  # Instance attribute
        self.age = age

    def bark(self):
        print(f"{self.name} ({self.age} years old) says Woof!")

    def __str__(self):  # __str__ example
        return f"Dog: {self.name}, Age: {self.age}, Species: {self.species}"

my_dog = Dog("Buddy", 3)  # Instance creation
print(my_dog)             # Uses __str__: Dog: Buddy, Age: 3, Species: Canine
my_dog.bark()             # Buddy (3 years old) says Woof!
print("Dog species:", my_dog.species)
print()

# 2. Inheritance
print("2. Inheritance Example:")
class Puppy(Dog):  # Inherit from Dog
    def __init__(self, name, breed, age=0):
        super().__init__(name, age)  # Call parent's __init__
        self.breed = breed

    def play(self):  # New method
        print(f"{self.name} ({self.breed}) is playing!")

    def bark(self):  # Override parent's method
        super().bark()  # Call parent's bark
        print("...and yips!")

pup = Puppy("Max", "Labrador", 1)
print(pup)  # From Dog's __str__: Dog: Max, Age: 1, Species: Canine
pup.bark()  # Overridden: Max (1 years old) says Woof! \n ...and yips!
pup.play()  # Max (Labrador) is playing!
print()

# 3. Properties and Encapsulation
print("3. Properties and Encapsulation Example:")
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected (_ convention)

    @property
    def radius(self):  # Getter
        return self._radius

    @radius.setter
    def radius(self, value):  # Setter with validation
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):  # Read-only property
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle with radius {self._radius}, area {self.area:.2f}"

c = Circle(5)
print(c)  # Circle with radius 5, area 78.54
print("Radius (property):", c.radius)  # 5

c.radius = 10  # Uses setter
print("After set radius=10:", c)  # Circle with radius 10, area 314.16

# Encapsulation: Direct access discouraged
# print(c._radius)  # 10 (accessible, but shouldn't)
# c._radius = -5  # No validation! Bad practice

# Try invalid set
try:
    c.radius = -3  # Raises ValueError
except ValueError as e:
    print("Error:", e)  # Error: Radius cannot be negative

print("Area property:", c.area)  # 314.16 (computed)
print()

# EXERCISES
print("=== EXERCISES: BankAccount Class ===")

class BankAccount:
    """
    Simple BankAccount class demonstrating OOP concepts.
    Encapsulates balance, supports deposit/withdraw.
    """
    def __init__(self, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = initial_balance  # Private attribute (__ encapsulation)

    @property
    def balance(self):  # Property getter for balance (read-only)
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def get_balance(self):  # Method for balance (alternative to property)
        return self.__balance

    def __str__(self):
        return f"Account balance: ${self.__balance:.2f}"

# Demonstration of BankAccount
print("BankAccount Demonstration:")
acc = BankAccount(100.0)  # Initial balance
print(acc)  # Account balance: $100.00

# Test deposit
acc.deposit(50.50)
print("Balance via property:", acc.balance)  # 150.5

# Test withdraw
acc.withdraw(30.0)
print("Balance via method:", acc.get_balance())  # 120.5

# Test errors
try:
    acc.withdraw(200.0)  # Insufficient
except ValueError as e:
    print("Error:", e)

try:
    acc.deposit(-10)  # Invalid amount
except ValueError as e:
    print("Error:", e)

print()

# Inheritance example: Subclass for SavingsAccount with interest
class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0.0, interest_rate=0.02):
        super().__init__(initial_balance)
        self.__interest_rate = interest_rate  # Private

    def add_interest(self):
        interest = self.balance * self.__interest_rate
        self.deposit(interest)
        print(f"Added interest: ${interest:.2f}")

    def __str__(self):
        return f"Savings Account - Balance: ${self.balance:.2f}, Rate: {self.__interest_rate * 100:.1f}%"

savings = SavingsAccount(1000.0, 0.03)
print(savings)  # Savings Account - Balance: $1000.00, Rate: 3.0%
savings.add_interest()  # Deposits 30.0
print(savings)  # Updated balance

# Interactive test
print("\nInteractive BankAccount Test:")
user_choice = input("Create a BankAccount? Enter initial balance (or 'skip'): ")
if user_choice.lower() != 'skip':
    try:
        init_bal = float(user_choice)
        user_acc = BankAccount(init_bal)
        print(user_acc)

        dep = float(input("Deposit amount: "))
        user_acc.deposit(dep)

        wd = float(input("Withdraw amount: "))
        user_acc.withdraw(wd)

        print("Final balance:", user_acc)
    except ValueError as e:
        print("Error:", e)

print("\nAll OOP demonstrations and exercises complete!")
