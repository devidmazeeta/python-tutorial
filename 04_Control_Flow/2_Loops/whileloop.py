# ===================================================
# PYTHON WHILE LOOPS: COMPREHENSIVE GUIDE
# ===================================================
# While loops execute a block of code as long as a condition is True

# ===================================================
# 1. BASIC WHILE LOOP
# ===================================================
print("\n=== 1. Basic while loop ===")
count = 1
print("Counting from 1 to 5:")
while count <= 5:
    print(f"Count: {count}")  # Count: 1, Count: 2, ..., Count: 5
    count += 1

# ===================================================
# 2. USING ELSE WITH WHILE LOOP
# ===================================================
print("\n=== 2. While-else statement ===")
number = 3
print(f"Counting down from {number}:")
while number > 0:
    print(f"{number}...")  # 3..., 2..., 1...
    number -= 1
else:
    print("Liftoff!")  # This executes when the loop completes normally

# ===================================================
# 3. NESTED WHILE LOOPS
# ===================================================
print("\n=== 3. Nested while loops ===")
print("Multiplication table (1-3):")

i = 1
while i <= 3:  # Outer loop for rows
    j = 1
    while j <= 3:  # Inner loop for columns
        print(f"{i}×{j}={i*j:2}", end="  ")
        j += 1
    print()  # New line after each row
    i += 1

# ===================================================
# 4. WHILE LOOPS WITH LISTS
# ===================================================
print("\n=== 4. While loops with lists ===")
print("Processing a list of items:")

shopping_list = ["apples", "bananas", "milk", "bread"]
while shopping_list:  # While list is not empty
    item = shopping_list.pop(0)  # Remove and return first item
    print(f"- Processing: {item}")

print("All items processed!")
