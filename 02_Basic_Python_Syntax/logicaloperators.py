# Logical operators => not, and, or

number = int(input("Enter a number: "))

if 40 <= number <= 60:
    print("Entered number is in range")

if number == 0 or number == 1:
    print("Entered number is binary")

if not (number == 1):
    print("Entered number is not 1")

# Method 1
if 40 <= number <= 50:
    print("Given number range is between 40 and 50")
elif 80 <= number <= 90:
    print("Given number range is between 80 and 90")

# Method 2 - Simplified
if (40 <= number <= 50) or (80 <= number <= 90):
    print("Given number range is between 40 and 50 or 80 and 90")

if not (40 <= number <= 50):
    print("Given number is not in the range 40 to 50")
else:
    print("Given number is in the range 40 to 50")
