# Python Syntax & Basics: Combined Example
# This script demonstrates variables, numbers, strings, booleans, comments, I/O, and operators.
# Run this in a Python environment (e.g., IDLE, VS Code). It includes interactive inputs.

# 1. Variables (including int)
age = 25          # int variable
count = -10       # negative int
big_num = 1000000 # large int
x = 5             # int
x = "hello"       # reassigned to string

print("Variables:")
print("age:", age, "type:", type(age))
print("count:", count)
print("big_num:", big_num)
print("x after reassignment:", x, "type:", type(x))
print()  # Empty line for readability

# 2. Numbers
height = 5.9      # float
pi = 3.14159
c = 3 + 4j        # complex

print("Numbers:")
print("height (float):", height, "type:", type(height))
print("pi:", pi)
print("complex c:", c, "type:", type(c))
print() 

# 3. Strings
name = "Alice"    # double quotes
greeting = 'Hello' # single quotes
multi_line = """This is a
multi-line string."""
print("name[0]:", name[0])  # Indexing

# String operations
concat = "Hello" + " " + "World"
repeat = "Hi" * 3
escaped = "Line1\nLine2"

print("Strings:")
print("name:", name)
print("greeting:", greeting)
print("multi_line:", multi_line)
print("Concatenation:", concat)
print("Repetition:", repeat)
print("Escaped (will show newline):")
print(escaped)
print()

# 4. Booleans
is_adult = True
is_raining = False
result = None

print("Booleans:")
print("is_adult:", is_adult, "type:", type(is_adult))
print("is_raining:", is_raining)
print("None example:", result)
print("Comparison example:", 5 > 3)  # True
print()

# 5. Comments
# This is a single-line comment
"""
This is a multi-line
comment block (using triple quotes).
"""
print("Comments are ignored by the interpreter.")
print()

# 6. Basic I/O: print() and input()
# print() examples
print("print() Examples:")
print("Hello, World!")
print("Age:", 25)
print("Custom end:", end=" ")  # No newline
print("No newline here.")

# input() examples (interactive - will prompt user)
print("\ninput() Examples:")
user_name = input("Enter your name: ")  # String input
user_age_input = input("Enter your age: ")
user_age = int(user_age_input)  # Convert to int (assumes valid input)

print("Hello,", user_name, "! You are", user_age, "years old.")
print("Using sep: 'A' 'B' 'C' ->", 'A', 'B', 'C', sep='-')
print()

# 7. Operators

# Arithmetic
print("Arithmetic Operators:")
num1 = 10
num2 = 3
print("num1 + num2 =", num1 + num2)      # 13
print("num1 - num2 =", num1 - num2)      # 7
print("num1 * num2 =", num1 * num2)      # 30
print("num1 / num2 =", num1 / num2)      # 3.333...
print("num1 // num2 =", num1 // num2)    # 3 (floor)
print("num1 % num2 =", num1 % num2)      # 1 (modulo)
print("num1 ** num2 =", num1 ** num2)    # 1000
result = (num1 + 5) * 2
print("Complex arithmetic:", result)     # 30
print()

# Comparison (returns booleans)
print("Comparison Operators:")
print("5 == 5:", 5 == 5)     # True
print("5 != 3:", 5 != 3)     # True
print("5 > 3:", 5 > 3)       # True
print("5 < 3:", 5 < 3)       # False
print("5 >= 5:", 5 >= 5)     # True
print("5 <= 3:", 5 <= 3)     # False
print()

# Logical
x = 10
print("Logical Operators:")
print("x > 5 and x < 15:", x > 5 and x < 15)  # True
print("x > 15 or x < 5:", x > 15 or x < 5)    # False
print("not (x > 15):", not (x > 15))          # True
print()

# Assignment (including augmented)
y = 20
print("Assignment Operators:")
print("y = 20:", y)
y += 5  # y = y + 5
print("y += 5:", y)  # 25
y *= 2  # y = y * 2
print("y *= 2:", y)  # 50
print()

# Membership (for strings)
print("Membership Operators:")
print("'a' in 'apple':", 'a' in 'apple')      # True
print("'z' not in 'apple':", 'z' not in 'apple')  # True
print()

# Quick Example: Simple Calculator (combines everything)
print("Simple Calculator Example:")
calc_name = input("Enter your name for calculator: ")  # Interactive string
calc_num1 = int(input("Enter first number: "))         # int input
calc_num2 = int(input("Enter second number: "))        # int input

calc_sum = calc_num1 + calc_num2  # Arithmetic
is_even = (calc_sum % 2 == 0)     # Modulo and comparison -> boolean

print(f"Hello, {calc_name}! The sum is {calc_sum}.")  # f-string formatting
print("Is the sum even?", is_even)                    # Boolean output

# End of script
print("\nAll basics demonstrated! Check the outputs above.")
