# ===================================================
# PYTHON BREAK AND CONTINUE: LOOP CONTROL FLOW
# ===================================================
# break    : Immediately exits the current loop
# continue : Skips the current iteration and moves to the next one

# ===================================================
# 1. USING BREAK IN A WHILE LOOP
# ===================================================
print("\n=== 1. Using break in a while loop ===")
count = 10
while count > 0:
    if count == 5:
        print("\nBreaking the loop at count = 5")
        break  # Exit the loop immediately
    print(count, end=" ")  # 10 9 8 7 6 
    count -= 1
else:
    # This won't execute because we broke out of the loop
    print("Loop completed normally")

# ===================================================
# 2. USING CONTINUE IN A WHILE LOOP
# ===================================================
print("\n\n=== 2. Using continue in a while loop ===")
num = 0
print("Printing odd numbers from 1 to 9:")
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")  # 1 3 5 7 9

# ===================================================
# 3. BREAK IN NESTED LOOPS
# ===================================================
print("\n\n=== 3. Using break in nested loops ===")
print("Nested loop with break (only inner loop exits):")
for i in range(3):
    print(f"\nOuter loop iteration: {i}")
    for j in range(3):
        if j == 1:
            print("  Breaking inner loop")
            break  # Only exits the inner loop
        print(f"  Inner loop: {j}")
    # Outer loop continues to next iteration

# ===================================================
# 4. BREAK WITH ELSE CLAUSE
# ===================================================
print("\n=== 4. Using break with else ===")
print("Searching for number 5 in range(10):")
for num in range(10):
    if num == 5:
        print(f"  Found {num}! Breaking the loop.")
        break
else:
    # This only executes if the loop completes without hitting break
    print("Number not found!")

# ===================================================
# 5. PRACTICAL EXAMPLE: PRIME NUMBER CHECK
# ===================================================
print("\n=== 5. Practical Example: Prime Number Check ===")
number = 17
print(f"Checking if {number} is a prime number:")

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print(f"  {number} is not a prime number (divisible by {i})")
        break
else:
    print(f"  {number} is a prime number!")
