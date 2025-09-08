# ===================================================
# PYTHON RANGE FUNCTION: COMPREHENSIVE GUIDE
# ===================================================
# The range() function generates a sequence of numbers and is commonly used in loops
# Syntax: range(start, stop, step)
# - start: Starting number (inclusive, optional, default=0)
# - stop: Ending number (exclusive, required)
# - step: Increment (optional, default=1)

# ===================================================
# 1. BASIC RANGE USAGE
# ===================================================
print("\n=== 1. Basic Range ===")
print("Range with stop only (0 to 6):")
for num in range(7):  # Equivalent to range(0, 7, 1)
    print(num, end=" ")  # 0 1 2 3 4 5 6

# ===================================================
# 2. RANGE WITH START AND STOP
# ===================================================
print("\n\n=== 2. Range with Start and Stop ===")
print("Range from 2 to 6:")
for num in range(2, 7):  # Start at 2, stop before 7
    print(num, end=" ")  # 2 3 4 5 6

# ===================================================
# 3. RANGE WITH START, STOP, AND STEP
# ===================================================
print("\n\n=== 3. Range with Start, Stop, and Step ===")
print("Even numbers from 2 to 8:")
for num in range(2, 10, 2):  # Start at 2, stop before 10, step by 2
    print(num, end=" ")  # 2 4 6 8

# ===================================================
# 4. NEGATIVE STEP (COUNTING BACKWARDS)
# ===================================================
print("\n\n=== 4. Counting Backwards ===")
print("Countdown from 5 to 1:")
for num in range(5, 0, -1):  # Start at 5, stop after 1, step -1
    print(num, end=" ")  # 5 4 3 2 1

# ===================================================
# 5. RANGE WITH FLOAT STEP (USING NUMPY)
# ===================================================
print("\n\n=== 5. Range with Float Step ===")
print("Floating point range (0.0 to 1.0, step 0.2):")
# Note: For floating point steps, we can use numpy's arange
import numpy as np
for num in np.arange(0, 1.1, 0.2):
    print(f"{num:.1f}", end=" ")  # 0.0 0.2 0.4 0.6 0.8 1.0

# ===================================================
# 6. RANGE WITH LENGTH AND INDEXING
# ===================================================
print("\n\n=== 6. Range with Length and Indexing ===")
fruits = ["apple", "banana", "cherry", "date"]
print("Index and value of each fruit:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
    # Index 0: apple
    # Index 1: banana
    # Index 2: cherry
    # Index 3: date

# ===================================================
# 7. RANGE WITH ELSE CLAUSE
# ===================================================
print("\n=== 7. Range with Else Clause ===")
print("Numbers from 1 to 3:")
for num in range(1, 4):
    print(num, end=" ")  # 1 2 3
else:
    print("\nLoop completed successfully!")
