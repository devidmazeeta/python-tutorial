# Demonstrating if-elif-else conditional statements in Python
# This program evaluates a student's mark and provides a performance category

# Get student's mark as input and convert to integer
mark = int(input("Enter your mark (0-100): "))

# Check mark against different grade thresholds
if 90 < mark <= 100:  # Check for outstanding performance
    print(f"Your mark is {mark}: Outstanding performance!")  # Your mark is 95: Outstanding performance!
elif mark > 75:  # Check for distinction
    print(f"Your mark is {mark}: Distinction!")  # Your mark is 80: Distinction!
elif mark > 65:  # Check for average performance
    print(f"Your mark is {mark}: Average")  # Your mark is 70: Average
elif mark >= 50:  # Check for passing mark
    print(f"Your mark is {mark}: Pass")  # Your mark is 55: Pass
elif mark >= 0:  # Handle failing marks
    print(f"Your mark is {mark}: Fail - Needs improvement")  # Your mark is 45: Fail - Needs improvement
else:  # Handle invalid input
    print("Invalid mark! Please enter a value between 0 and 100")  # Invalid mark! Please enter a value between 0 and 100
