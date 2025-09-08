# ===================================================
# PYTHON FOR LOOPS: COMPREHENSIVE GUIDE
# ===================================================
# For loops are used for iterating over a sequence (list, tuple, string, dictionary, etc.)

# ===================================================
# 1. BASIC FOR LOOP WITH LISTS
# ===================================================
print("\n=== 1. Looping through a list ===")
names = ["Alex", "Arun", "Ajay", "Priya", "Rahul"]

# Basic for loop
print("\nAll names:")
for name in names:
    print(f"- {name}")
    # - Alex
    # - Arun
    # - Ajay
    # - Priya
    # - Rahul

# Using enumerate() to get both index and value
print("\nNames with index:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
    # 1. Alex
    # 2. Arun
    # 3. Ajay
    # 4. Priya
    # 5. Rahul

# ===================================================
# 2. LOOPING THROUGH STRINGS
# ===================================================
print("\n=== 2. Looping through strings ===")
company = "Google"

# Iterate through each character
print("\nCharacters in 'Google':")
for char in company:
    print(char.upper(), end=" ")  # G O O G L E

# Using range with string length
print("\n\nCharacters with index:")
for i in range(len(company)):
    print(f"{i}: {company[i]}")
    # 0: G
    # 1: o
    # 2: o
    # 3: g
    # 4: l
    # 5: e

# ===================================================
# 3. LOOPING THROUGH DICTIONARIES
# ===================================================
print("\n=== 3. Looping through dictionaries ===")
fruits = {
    "apple": 10,
    "grapes": 20,
    "orange": 30,
    "banana": 15,
    "mango": 25
}

# Method 1: Iterate through keys (default behavior)
print("\nFruits (keys only):")
for fruit in fruits:
    print(f"- {fruit}")
    # - apple
    # - grapes
    # - orange
    # - banana
    # - mango

# Method 2: Using items() to get key-value pairs
print("\nFruits with quantities (Method 1):")
for fruit, quantity in fruits.items():
    print(f"- {fruit}: {quantity} pieces")
    # - apple: 10 pieces
    # - grapes: 20 pieces
    # - orange: 30 pieces
    # - banana: 15 pieces
    # - mango: 25 pieces

# Method 3: Using keys() and values() separately
print("\nFruits with quantities (Method 2):")
for fruit in fruits.keys():
    print(f"- {fruit}: {fruits[fruit]} pieces")

# ===================================================
# 4. PRACTICAL EXAMPLES
# ===================================================
print("\n=== 4. Practical examples ===")

# Example 1: Calculate total quantity
print("\nCalculating total fruits:")
total = 0
for fruit, quantity in fruits.items():
    print(f"Adding {quantity} {fruit}s")
    total += quantity
print(f"\nTotal fruits in stock: {total}")
# Adding 10 apples
# Adding 20 grapess
# Adding 30 oranges
# Adding 15 bananas
# Adding 25 mangos
# 
# Total fruits in stock: 100

# Example 2: Nested loops (multiplication table)
print("\nMultiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()  # New line after each row

# ===================================================
# 5. LOOP CONTROL STATEMENTS
# ===================================================
print("\n=== 5. Loop control statements ===")

# break: Exit the loop
print("\nUsing break:")
for fruit in fruits:
    if fruit == "orange":
        print("Found orange! Stopping search.")
        break
    print(f"Checking {fruit}...")

# continue: Skip current iteration
print("\nUsing continue (odd numbers only):")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()  # 1 3 5 7 9

# ===================================================
# 6. THE ELSE CLAUSE IN FOR LOOPS
# ===================================================
print("\n=== 6. The else clause in for loops ===")
print("\nSearching for 'pear':")
for fruit in fruits:
    if fruit == "pear":
        print("Found pear!")
        break
else:
    print("Pear not found in the inventory.")
    # This else clause runs if the loop completes without hitting a break
