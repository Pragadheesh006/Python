# Python Strings & File I/O: Demonstrations and Exercises
# Run this script to see outputs. It creates temporary files (example.txt, data.csv, data.json)
# in the current directory. Exercises are interactive where needed.
# Note: For CSV/JSON, ensure 'csv' and 'json' modules are available (standard library).

import csv
import json
import os  # For file cleanup (optional)

# 1. String Methods
print("1. String Methods Examples:")
s = "  Hello, World!  "
print("Original:", repr(s))  # '  Hello, World!  ' (repr shows whitespace)
print("strip():", repr(s.strip()))  # 'Hello, World!'
print("lower():", s.lower())  # '  hello, world!  '
print("upper():", s.upper())  # '  HELLO, WORLD!  '
print("title():", s.title())  # '  Hello, World!  '

# Split and join
words = s.strip().lower().split()
print("split():", words)  # ['hello,', 'world!']
joined = '-'.join(words)
print("join('-'):", joined)  # 'hello,-world!'

# Search and replace
print("find('World'):", s.find('World'))  # 9 (position)
print("replace('World', 'Python'):", s.replace('World', 'Python'))  # '  Hello, Python!  '
print("count('l'):", s.count('l'))  # 3
print("startswith('  H'):", s.startswith('  H'))  # True
print("endswith('!  '):", s.endswith('!  '))  # True

# Validation
print("isalpha():", "hello".isalpha())  # True
print("isdigit():", "123".isdigit())  # True
print("isspace():", "   ".isspace())  # True

# Slicing and membership
print("s[3:8]:", s[3:8])  # 'Hello'
print("'World' in s:", 'World' in s)  # True
print()

# 2. String Formatting
print("2. String Formatting Examples:")
name = "Alice"
age = 25
pi = 3.14159

# f-strings (preferred)
print(f"{name} is {age} years old.")  # Alice is 25 years old.
print(f"Pi rounded: {pi:.2f}")  # Pi rounded: 3.14
print(f"Name length: {len(name)}")  # Name length: 5
print(f"Upper: {name.upper()}")  # Upper: ALICE

# .format()
print("{} is {} years old.".format(name, age))
print("{n} is {a} years old. Pi: {p:.1f}".format(n=name, a=age, p=pi))  # Alice is 25 years old. Pi: 3.1

# % operator (old-style)
print("%s is %d years old." % (name, age))  # Alice is 25 years old.
print()

# 3. File I/O: Text Files
print("3. Text File I/O Examples:")

# Write to file
filename = 'example.txt'
with open(filename, 'w') as f:
    f.write("Hello\nWorld\nThis is line 3.\n")

# Read all
with open(filename, 'r') as f:
    content = f.read()
    print("read() all content:\n", repr(content))  # 'Hello\nWorld\nThis is line 3.\n'

# Read lines
with open(filename, 'r') as f:
    lines = f.readlines()
    print("readlines():", repr(lines))  # ['Hello\n', 'World\n', 'This is line 3.\n']

# Iterate over lines
with open(filename, 'r') as f:
    print("Iterating lines:")
    for line_num, line in enumerate(f, 1):
        print(f"Line {line_num}: {line.strip()}")  # Line 1: Hello \n etc.

# Append mode
with open(filename, 'a') as f:
    f.write("Appended line.\n")

# Read after append
with open(filename, 'r') as f:
    print("After append (last line):", f.readlines()[-1].strip())  # Appended line.

print()

# 4. CSV Files
print("4. CSV File I/O Examples:")

csv_filename = 'data.csv'
# Write CSV
with open(csv_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])  # Header
    writer.writerows([
        ['Alice', 25, 'NYC'],
        ['Bob', 30, 'LA'],
        ['Charlie', 35, 'Chicago']
    ])

# Read CSV as lists
with open(csv_filename, 'r') as f:
    reader = csv.reader(f)
    print("CSV reader (lists):")
    for row in reader:
        print(row)  # ['Name', 'Age', 'City'] \n ['Alice', '25', 'NYC'] etc.

# Read as dicts (DictReader)
with open(csv_filename, 'r') as f:
    dict_reader = csv.DictReader(f)
    print("\nCSV DictReader:")
    for row in dict_reader:
        print(f"{row['Name']} is {row['Age']} from {row['City']}")
    # Alice is 25 from NYC \n etc.

print()

# 5. JSON Files
print("5. JSON File I/O Examples:")

json_filename = 'data.json'
# Data
data = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'coding'],
    'address': {'city': 'NYC', 'zip': 10001}
}

# Write JSON
with open(json_filename, 'w') as f:
    json.dump(data, f, indent=4)  # indent for readability

# Read JSON
with open(json_filename, 'r') as f:
    loaded_data = json.load(f)
    print("Loaded JSON:", loaded_data)
    # {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'coding'], 'address': {'city': 'NYC', 'zip': 10001}}

# JSON strings (dumps/loads)
json_str = json.dumps(data, indent=2)
print("\nJSON string (dumps):", json_str[:100] + "...")  # Truncated
parsed = json.loads(json_str)
print("Parsed from string:", parsed['name'])  # Alice

print()

# EXERCISES
print("=== EXERCISES ===")

# Exercise: Parse a CSV and Summarize Columns
# We'll use the data.csv created above. Summarize: row count, unique cities, average age.
print("Exercise: CSV Parsing and Summarization")

def summarize_csv(filename):
    ages = []
    cities = set()
    row_count = 0
    
    with open(filename, 'r') as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            row_count += 1
            try:
                ages.append(int(row['Age']))
            except (ValueError, KeyError):
                pass  # Skip invalid ages
            cities.add(row['City'])
    
    if ages:
        avg_age = sum(ages) / len(ages)
    else:
        avg_age = 0
    
    print(f"Total rows (excluding header): {row_count}")
    print(f"Unique cities: {sorted(list(cities))}")
    print(f"Average age: {avg_age:.2f}")
    print(f"All ages: {ages}")

# Run summarization on data.csv
summarize_csv(csv_filename)
# Output example: Total rows: 3 \n Unique cities: ['Chicago', 'LA', 'NYC'] \n Average age: 30.00 \n All ages: [25, 30, 35]

# Interactive: Allow user to provide a custom CSV summary (but for simplicity, use existing)
# To test with custom: Uncomment and modify below
# custom_csv = input("Enter path to custom CSV (or press Enter for default): ")
# if custom_csv:
#     summarize_csv(custom_csv)
# else:
#     summarize_csv(csv_filename)

print()

# Optional: Cleanup files (uncomment to delete temp files)
# for file in [filename, csv_filename, json_filename]:
#     if os.path.exists(file):
#         os.remove(file)
#         print(f"Deleted {file}")

print("\nAll demonstrations and exercises complete!")
# Note: Files are created in the script's directory. Check them manually if needed.
