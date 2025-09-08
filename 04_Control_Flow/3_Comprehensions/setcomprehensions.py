# ===================================================
# PYTHON SET COMPREHENSIONS
# ===================================================
# Set comprehensions provide a concise way to create sets
# Syntax: {expression for item in iterable if condition}
# Note: Sets automatically remove duplicates and are unordered

# ===================================================
# 1. BASIC SET COMPREHENSION
# ===================================================
print("\n=== 1. Basic Set Comprehension ===")
# Create a set of unique squares from a list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_squares = {x**2 for x in numbers}
print("Unique squares:", unique_squares)  # {1, 4, 9, 16, 25}

# ===================================================
# 2. SET COMPREHENSION WITH CONDITION
# ===================================================
print("\n=== 2. Set Comprehension with Condition ===")
# Get unique even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 8, 6]
even_numbers = {x for x in numbers if x % 2 == 0}
print("Unique even numbers:", even_numbers)  # {2, 4, 6, 8, 10}

# ===================================================
# 3. CREATING A SET OF UNIQUE CHARACTERS
# ===================================================
print("\n=== 3. Creating a Set of Unique Characters ===")
# Get unique characters from a string (case-sensitive)
text = "Hello, World! How are you?"
unique_chars = {char.lower() for char in text if char.isalpha()}
print("Unique letters (case-insensitive):", sorted(unique_chars))
# Output: ['a', 'd', 'e', 'h', 'l', 'o', 'r', 'u', 'w', 'y']

# ===================================================
# 4. SET OPERATIONS WITH COMPREHENSIONS
# ===================================================
print("\n=== 4. Set Operations with Comprehensions ===")
# Two sets of numbers
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union using set comprehension
union = {x for x in set_a.union(set_b)}
print("Union of sets:", union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection using set comprehension
intersection = {x for x in set_a if x in set_b}
print("Intersection of sets:", intersection)  # {4, 5}

# Difference using set comprehension
difference = {x for x in set_a if x not in set_b}
print("Elements in set_a not in set_b:", difference)  # {1, 2, 3}

# ===================================================
# 5. SET COMPREHENSION WITH DICTIONARIES
# ===================================================
print("\n=== 5. Set Comprehension with Dictionaries ===")
# Sample data: Dictionary of students and their grades
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 85,  # Duplicate grade
    "Frank": 78  # Duplicate grade
}

# Get unique grades
grades = {grade for grade in students.values()}
print("Unique grades:", grades)  # {85, 90, 78, 92}

# Get students with grades above 85
high_achievers = {name for name, grade in students.items() if grade > 85}
print("High achievers (grade > 85):", high_achievers)  # {'Bob', 'David'}

# ===================================================
# 6. REMOVING DUPLICATES FROM A LIST
# ===================================================
print("\n=== 6. Removing Duplicates from a List ===")
# List with duplicate values
fruits = ["apple", "banana", "apple", "orange", "banana", "kiwi"]

# Convert to set and back to list to remove duplicates
unique_fruits = list({fruit for fruit in fruits})
print("Original list:", fruits)
print("List with duplicates removed:", unique_fruits)
# Output: ['banana', 'orange', 'kiwi', 'apple'] (order may vary)
