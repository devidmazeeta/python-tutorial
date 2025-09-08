# ===================================================
# TERNARY OPERATIONS IN PYTHON
# ===================================================
# A ternary operation is a concise way to write if-else statements in a single line.
# Syntax: value_if_true if condition else value_if_false

# ===================================================
# 1. BASIC TERNARY OPERATION
# ===================================================
# Example 1.1: Simple pass/fail check
mark = 75
result = "Pass" if mark >= 50 else "Fail"
print(f"Example 1.1 - Mark: {mark}, Result: {result}")  # Mark: 75, Result: Pass

# Equivalent if-else statement
if mark >= 50:
    result = "Pass"
else:
    result = "Fail"
print(f"Traditional if-else: {result}\n")  # Traditional if-else: Pass

# Example 1.2: Checking number sign
number = -5
sign = "Positive" if number > 0 else "Negative or Zero"
print(f"Example 1.2 - Number: {number}, Sign: {sign}")  # Number: -5, Sign: Negative or Zero

# ===================================================
# 2. NESTED TERNARY OPERATIONS
# ===================================================
# Example 2.1: Grade classification
mark = 85
grade = "A" if mark >= 90 else "B" if mark >= 80 else "C" if mark >= 70 else "D" if mark >= 50 else "F"
print(f"\nExample 2.1 - Mark: {mark}, Grade: {grade}")  # Mark: 85, Grade: B

# Equivalent if-elif-else statement
if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"
print(f"Traditional if-elif-else: {grade}")  # Traditional if-elif-else: B

# ===================================================
# 3. PRACTICAL EXAMPLES
# ===================================================
# Example 3.1: Checking list emptiness
shopping_list = ["apples", "bananas"]
status = "Go shopping!" if not shopping_list else f"{len(shopping_list)} items in list"
print(f"\nExample 3.1 - {status}")  # 2 items in list

# Example 3.2: Finding maximum of two numbers
a, b = 10, 20
maximum = a if a > b else b
print(f"Example 3.2 - Max of {a} and {b} is: {maximum}")  # Max of 10 and 20 is: 20

# Example 3.3: String formatting based on condition
name = "Alice"
greeting = f"Hello, {name}!" if name else "Hello, Guest!"
print(f"Example 3.3 - {greeting}")  # Hello, Alice!

# ===================================================
# 4. TERNARY WITH FUNCTION CALLS
# ===================================================
def is_even(num):
    return num % 2 == 0

number = 4
result = "Even" if is_even(number) else "Odd"
print(f"\nExample 4.1 - {number} is {result}")  # 4 is Even

# ===================================================
# BEST PRACTICES
# ===================================================
# 1. Use ternary for simple conditions only
# 2. Avoid deep nesting (more than 2 levels)
# 3. When in doubt, prefer traditional if-else for better readability

# Example of what NOT to do (too complex):
# result = "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D" if x > 50 else "E" if x > 30 else "F"

# Instead, consider:
# if x > 90: result = "A"
# elif x > 80: result = "B"
# ... and so on ...
