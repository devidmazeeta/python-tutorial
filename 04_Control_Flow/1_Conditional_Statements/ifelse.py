# Demonstrating basic if-else conditional statement in Python
# This program checks if a student has passed or failed based on their score

# Get student's score as input and convert to integer
# Using strip() to remove any accidental whitespace
score = input("Enter your score (0-100): ").strip()

# Convert to integer and validate the input range
score = int(score)
if not 0 <= score <= 100:
    print("Error: Score must be between 0 and 100")  # Error: Score must be between 0 and 100
else:
    # Single if-else statement to determine pass/fail
    if score >= 50:
        print(f"Your score is {score}: Pass")  # Your score is 75: Pass
    else:
        print(f"Your score is {score}: Fail")  # Your score is 42: Fail
