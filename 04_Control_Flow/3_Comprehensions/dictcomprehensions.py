# ===================================================
# PYTHON DICTIONARY COMPREHENSIONS
# ===================================================
# Dictionary comprehensions provide a concise way to create dictionaries
# Syntax: {key_expression: value_expression for item in iterable if condition}

# ===================================================
# 1. BASIC DICTIONARY COMPREHENSION
# ===================================================
print("\n=== 1. Basic Dictionary Comprehension ===")
# Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print("Numbers and their squares:", squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ===================================================
# 2. DICTIONARY COMPREHENSION WITH CONDITION
# ===================================================
print("\n=== 2. Dictionary Comprehension with Condition ===")
# Create a dictionary of even numbers and their squares
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Even numbers and their squares:", even_squares)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# ===================================================
# 3. TRANSFORMING A DICTIONARY
# ===================================================
print("\n=== 3. Transforming a Dictionary ===")
# Original dictionary of fruits and their stock
fruits = {
    "apple": 7,
    "orange": 20,
    "grapes": 10,
    "pineapple": 6,
    "watermelon": 3,
    "kiwi": 25,
}

# Create a new dictionary with fruits that need to be reordered (stock < 10)
reorder_list = {fruit: 10 - stock for fruit, stock in fruits.items() if stock < 10}
print("Fruits that need reordering (quantity to order):", reorder_list)
# Output: {'apple': 3, 'pineapple': 4, 'watermelon': 7}

# ===================================================
# 4. COUNTING ELEMENT OCCURRENCES
# ===================================================
print("\n=== 4. Counting Element Occurrences ===")
# List of elements with duplicates
elements = [10, 10, "abc", 20, "def", "def", "100", 30, "GHI", "Xyz"]

# Method 1: Using a loop
occurrence_loop = {}
for element in elements:
    occurrence_loop[element] = occurrence_loop.get(element, 0) + 1
print("Using loop:", occurrence_loop)
# Output: {10: 2, 'abc': 1, 20: 1, 'def': 2, '100': 1, 30: 1, 'GHI': 1, 'Xyz': 1}

# Method 2: Using dictionary comprehension (more concise)
occurrence_comp = {element: elements.count(element) for element in set(elements)}
print("Using dictionary comprehension:", occurrence_comp)
# Output: {'Xyz': 1, 10: 2, 'abc': 1, 20: 1, 'def': 2, '100': 1, 30: 1, 'GHI': 1}

# ===================================================
# 5. CREATING A DICTIONARY FROM TWO LISTS
# ===================================================
print("\n=== 5. Creating Dictionary from Two Lists ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip() with dictionary comprehension
name_age_dict = {name: age for name, age in zip(names, ages)}
print("Name-Age Dictionary:", name_age_dict)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# ===================================================
# 6. NESTED DICTIONARY COMPREHENSION
# ===================================================
print("\n=== 6. Nested Dictionary Comprehension ===")
# Create a multiplication table
multiplication_table = {i: {j: i*j for j in range(1, 6)} for i in range(1, 4)}
print("Multiplication Table (1-3 x 1-5):")
for key, value in multiplication_table.items():
    print(f"  {key}: {value}")
# Output:
#   1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#   2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
#   3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
