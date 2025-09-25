# Python Functions: Demonstrations and Exercises
# Run this script to see outputs. Exercises prompt for input.

# 1. Defining Functions with def
print("1. Basic def Examples:")

def hello():
    print("Hello, World!")

hello()  # Output: Hello, World!

def greet(name):
    """Greet a person by name (docstring example)."""
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

print()

# Default parameters
def greet_default(name="World"):
    print(f"Hi, {name}!")

greet_default()  # Hi, World!
greet_default("Bob")  # Hi, Bob!
print()

# 2. Return Values
print("2. Return Value Examples:")
def add(a, b):
    return a + b

result = add(3, 5)
print("add(3,5):", result)  # 8

def divide(a, b):
    if b == 0:
        return None, "Error: Division by zero"
    return a / b, "Success"

quot, msg = divide(10, 2)
print(f"Quotient: {quot}, Message: {msg}")  # Quotient: 5.0, Message: Success

# Early return example
def check_positive(n):
    if n <= 0:
        return False
    return True  # Implicit else

print("check_positive(5):", check_positive(5))  # True
print()

# 3. Positional and Keyword Arguments
print("3. Positional/Keyword Args Examples:")
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Alice", 25)  # Positional
introduce(age=25, name="Bob")  # Keyword

# Mix
introduce("Charlie", age=30)  # Valid mix

# Default with keyword override
def greet_msg(name, greeting="Hi"):
    print(f"{greeting}, {name}!")

greet_msg("Dana", greeting="Hello")  # Override
print()

# 4. *args and **kwargs
print("4. *args and **kwargs Examples:")
def sum_all(*args):
    return sum(args)

print("sum_all(1,2,3,4):", sum_all(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=28, city="LA")
# name: Eve
# age: 28
# city: LA

# Combined
def flexible(a, b=10, *args, **kwargs):
    print("Fixed positional:", a, b)
    print("Extra positional (*args):", args)
    print("Extra keyword (**kwargs):", kwargs)

flexible(1, 2, 3, 4, x=5, y=6)
# Fixed positional: 1 2
# Extra positional (*args): (3, 4)
# Extra keyword (**kwargs): {'x': 5, 'y': 6}
print()

# 5. Lambda Functions
print("5. Lambda Examples:")
square = lambda x: x ** 2
print("lambda square(5):", square(5))  # 25

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print("map lambda squares:", squares)  # [1, 4, 9, 16]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter lambda evens:", evens)  # [2, 4]

# Sorted with lambda key
names = ["Bob", "Alice", "Charlie"]
sorted_names = sorted(names, key=lambda n: len(n))
print("sorted by length:", sorted_names)  # ['Bob', 'Alice', 'Charlie']
print()

# EXERCISES: Reusable Utility Functions
print("=== EXERCISES: Utility Functions ===")

# Utility 1: is_palindrome(s) - Checks if string is palindrome (ignore case, spaces, punctuation)
def is_palindrome(s):
    # Clean: lowercase, remove non-alphabetic
    cleaned = ''.join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]

# Interactive test
user_str = input("Enter a string to check palindrome (e.g., 'A man a plan a canal Panama'): ")
print(f"'{user_str}' is a palindrome: {is_palindrome(user_str)}")
# Example: True for the input above

print()

# Utility 2: reverse_string(s) - Returns reversed string
def reverse_string(s):
    return s[::-1]  # Using slicing

user_str2 = input("Enter a string to reverse (e.g., 'hello'): ")
print(f"Reversed: '{reverse_string(user_str2)}'")
# Example: 'olleh'

print()

# Utility 3: is_even(n) - Checks if number is even
def is_even(n):
    return n % 2 == 0

user_num = int(input("Enter a number to check if even (e.g., 4): "))
print(f"{user_num} is even: {is_even(user_num)}")
# Example: True for 4

print()

# Utility 4: factorial(n) - Reusable factorial (from control flow, using loop)
def factorial(n):
    if n < 0:
        return None  # Or raise error
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

user_n = int(input("Enter a number for factorial (e.g., 5): "))
fact = factorial(user_n)
print(f"{user_n}! = {fact if fact is not None else 'Invalid input'}")
# Example: 5! = 120

print("\nAll demonstrations and utility functions complete!")
# Example usage of utilities together:
# print(is_palindrome(reverse_string("racecar")))  # True
