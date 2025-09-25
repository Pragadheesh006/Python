# Python Core Data Structures: Demonstrations and Exercises
# Run this script to see outputs. Exercises prompt for input.

# 1. List
print("1. List Examples:")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("Indexing my_list[2]:", my_list[2])  # 3
print("Slicing my_list[1:4]:", my_list[1:4])  # [2, 3, 4]
print("Reverse slice my_list[::-1]:", my_list[::-1])  # [5, 4, 3, 2, 1]
print("Length:", len(my_list))  # 5

# Methods
my_list.append(6)
print("After append(6):", my_list)  # [1, 2, 3, 4, 5, 6]
my_list.pop(0)  # Remove first
print("After pop(0):", my_list)  # [2, 3, 4, 5, 6]
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)  # [6, 5, 4, 3, 2]
print("2 in my_list:", 2 in my_list)  # True
print()

# 2. Tuple
print("2. Tuple Examples:")
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)
print("Indexing my_tuple[1]:", my_tuple[1])  # 2
print("Slicing my_tuple[1:3]:", my_tuple[1:3])  # (2, 3)
print("Length:", len(my_tuple))  # 5
print("Count of 2:", my_tuple.count(2))  # 1
# my_tuple[0] = 10  # Uncomment to see TypeError (immutable)
print("Membership 3 in my_tuple:", 3 in my_tuple)  # True
print()

# 3. Set
print("3. Set Examples:")
my_set = {1, 2, 3, 2, 4}  # Duplicates removed: {1, 2, 3, 4}
print("Original set:", my_set)
my_set.add(5)
print("After add(5):", my_set)  # {1, 2, 3, 4, 5}
my_set.remove(2)
print("After remove(2):", my_set)  # {1, 3, 4, 5}
print("Length:", len(my_set))  # 4
print("2 in my_set:", 2 in my_set)  # False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union set_a | set_b:", set_a | set_b)  # {1, 2, 3, 4, 5}
print("Intersection set_a & set_b:", set_a & set_b)  # {3}
print("Difference set_a - set_b:", set_a - set_b)  # {1, 2}
print()

# 4. Dict
print("4. Dict Examples:")
my_dict = {'name': 'Alice', 'age': 25, 'name': 'Bob'}  # Last 'name' overwrites: {'name': 'Bob', 'age': 25}
print("Original dict:", my_dict)
print("Indexing my_dict['age']:", my_dict['age'])  # 25
print("get('city', 'Unknown'):", my_dict.get('city', 'Unknown'))  # Unknown
my_dict['city'] = 'NYC'  # Add/update
print("After adding 'city':", my_dict)  # {'name': 'Bob', 'age': 25, 'city': 'NYC'}
print("Length:", len(my_dict))  # 3
print("'age' in my_dict:", 'age' in my_dict)  # True

# Iterating
print("Keys:", list(my_dict.keys()))  # ['name', 'age', 'city']
print("Values:", list(my_dict.values()))  # ['Bob', 25, 'NYC']
for k, v in my_dict.items():
    print(f"{k}: {v}")
# name: Bob
# age: 25
# city: NYC
my_dict.pop('name')
print("After pop('name'):", my_dict)  # {'age': 25, 'city': 'NYC'}
print()

# EXERCISES
print("=== EXERCISES ===")

# Exercise 1: Count Word Frequency in a Sentence (using dict)
print("Exercise 1: Word Frequency Counter")
def count_word_frequency(sentence):
    # Lowercase and split into words (simple: split on spaces, ignore punctuation)
    words = sentence.lower().replace('.', '').replace(',', '').replace('!', '').split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Interactive
user_sentence = input("Enter a sentence (e.g., 'Hello world! Hello Alice.'): ")
freq = count_word_frequency(user_sentence)
print("Word frequencies:", freq)
# Example input: "hello world hello" → {'hello': 2, 'world': 1}

# Alternative using collections.Counter (advanced, commented)
# from collections import Counter
# freq_alt = Counter(words)
# print("Using Counter:", dict(freq_alt))
print()

# Exercise 2: Remove Duplicates (using set)
print("Exercise 2: Remove Duplicates from List")
def remove_duplicates(lst):
    return list(set(lst))  # Convert to set (removes dups), back to list (ordered? No, sets unordered)

# Example list with duplicates
example_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", example_list)
unique_list = remove_duplicates(example_list)
print("After removing duplicates:", unique_list)  # [1, 2, 3, 4, 5] (order may vary, but uniques)

# Interactive
user_input = input("Enter numbers separated by commas (e.g., 1,2,2,3): ")
user_list = [int(x.strip()) for x in user_input.split(',') if x.strip().isdigit()]
unique_user = remove_duplicates(user_list)
print("Unique elements:", unique_user)
# Example input: "1,2,2,3" → Unique: [1, 2, 3]

print("\nAll demonstrations and exercises complete!")
