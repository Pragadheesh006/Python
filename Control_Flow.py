# Python Control Flow: Demonstrations and Exercises
# Run this script to see outputs. Exercises are interactive where needed.

# 1. if/elif/else Statements
print("1. if/elif/else Example:")
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
# Output: Adult

# Nested if example
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
if grade == "A":
    print("Excellent!")
else:
    print(f"Good job, grade: {grade}")
# Output: Good job, grade: B

print()  # Empty line

# 2. for Loops
print("2. for Loop Examples:")
# Basic range
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # Newline

# range with start, stop, step
for i in range(1, 10, 2):
    print(i, end=" ")  # 1 3 5 7 9
print()

# Over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# Over string
for char in "Hello":
    print(char, end=" ")
# H e l l o
print()
print()

# 3. while Loops
print("3. while Loop Example:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
# Output: 0 1 2 3 4
print()

# while with input (simple counter until user says stop)
print("while with condition (type 'stop' to end):")
user_input = ""
while user_input != "stop":
    user_input = input("Enter something (or 'stop'): ")
    if user_input != "stop":
        print("You entered:", user_input)
print("Loop ended.")
print()

# 4. break and continue
print("4. break and continue Examples:")
# break
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
# Output: 0 1 2 3 4
print()

# continue
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
# Output: 0 1 3 4
print()

# break in while
count = 0
while True:  # Infinite loop, but break exits
    print(count, end=" ")
    count += 1
    if count == 3:
        break
# Output: 0 1 2
print()

# Loop else (runs if no break)
for i in range(3):
    print(i, end=" ")
else:
    print(" (Loop completed without break)")
# Output: 0 1 2  (Loop completed without break)
print()

# EXERCISES
print("=== EXERCISES ===")

# Exercise 1: FizzBuzz (1 to 100)
print("Exercise 1: FizzBuzz")
def fizzbuzz(n=100):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()  # Newline at end

fizzbuzz()
# Output: 1 2 Fizz 4 Buzz ... (up to 100)

print()

# Exercise 2: Factorial (using while loop)
print("Exercise 2: Factorial")
def factorial(n):
    if n < 0:
        return "Invalid: n must be non-negative"
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

# Interactive
user_n = int(input("Enter a number for factorial (e.g., 5): "))
print(f"{user_n}! = {factorial(user_n)}")
# Example input 5: Output: 5! = 120

# Alternative with for loop (commented)
# def factorial_for(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
print()

# Exercise 3: Prime Check (using for loop)
print("Exercise 3: Prime Check")
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Interactive
user_num = int(input("Enter a number to check if prime (e.g., 17): "))
if is_prime(user_num):
    print(f"{user_num} is prime.")
else:
    print(f"{user_num} is not prime.")
# Example input 17: Output: 17 is prime.
# Example input 4: Output: 4 is not prime.

# Simple for-loop version for basics (less efficient for large n)
def is_prime_basic(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Basic check for {user_num}: {is_prime_basic(user_num)}")

print("\nAll demonstrations and exercises complete!")
