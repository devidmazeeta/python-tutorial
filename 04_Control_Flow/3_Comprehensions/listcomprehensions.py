# ===================================================
# PYTHON LIST COMPREHENSIONS
# ===================================================
# List comprehensions provide a concise way to create lists
# Syntax: [expression for item in iterable if condition]

# ===================================================
# 1. BASIC LIST COMPREHENSION
# ===================================================
print("\n=== 1. Basic List Comprehension ===")
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares of numbers 1-5:", squares)  # [1, 4, 9, 16, 25]

# ===================================================
# 2. LIST COMPREHENSION WITH CONDITION
# ===================================================
print("\n=== 2. List Comprehension with Condition ===")
# Get only even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers from 1-10:", even_numbers)  # [2, 4, 6, 8, 10]

# ===================================================
# 3. FILTERING ELEMENTS BY TYPE
# ===================================================
print("\n=== 3. Filtering Elements by Type ===")
# Mixed data types in a list
values = [10, 10, "abc", 20, "def", "def", "100", 30, "GHI", "Xyz"]

# Method 1: Traditional approach
filtered_integers = []
for value in values:
    if isinstance(value, int):
        filtered_integers.append(value)
print("Using traditional loop:", filtered_integers)  # [10, 10, 20, 30]

# Method 2: Using list comprehension
filtered_integers_comp = [value for value in values if isinstance(value, int)]
print("Using list comprehension:", filtered_integers_comp)  # [10, 10, 20, 30]

# ===================================================
# 4. WORKING WITH DICTIONARIES
# ===================================================
print("\n=== 4. Working with Dictionaries ===")
# Sample fruit inventory
data = {
    "apple": 7,
    "orange": 20,
    "grapes": 10,
    "pineapple": 6,
    "watermelon": 3,
    "kiwi": 25,
}

# Get fruit names with stock less than 10
low_stock_fruits = [fruit for fruit, stock in data.items() if stock < 10]
print("Low stock fruits (stock < 10):", low_stock_fruits)
# Output: ['apple', 'pineapple', 'watermelon']

# Get fruit names and stock as tuples for low stock items
low_stock_details = [(fruit, stock) for fruit, stock in data.items() if stock < 10]
print("Low stock details (name, stock):", low_stock_details)
# Output: [('apple', 7), ('pineapple', 6), ('watermelon', 3)]

# ===================================================
# 5. NESTED LIST COMPREHENSIONS
# ===================================================
print("\n=== 5. Nested List Comprehensions ===")
# Create a 3x3 matrix using nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 Multiplication Matrix:")
for row in matrix:
    print(f"  {row}")
# Output:
#   [1, 2, 3]
#   [2, 4, 6]
#   [3, 6, 9]

# ===================================================
# 6. LIST COMPREHENSION WITH IF-ELSE
# ===================================================
print("\n=== 6. List Comprehension with If-Else ===")
# Categorize numbers as 'even' or 'odd'
numbers = range(1, 6)
categorized = ["even" if x % 2 == 0 else "odd" for x in numbers]
print("Number categories:", list(zip(numbers, categorized)))
# Output: [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd')]
