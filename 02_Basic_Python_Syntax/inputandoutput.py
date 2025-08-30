# Input for name and roll number
name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")

print(f"My name is {name} and my roll number is {roll_no}")

# To get multiple inputs in a single input command
numbers_input = input("Enter multiple numbers using comma separator: ")  # e.g. "1,2,3,4,5,6"
comma_separated_numbers = numbers_input.split(",") # [ 1, 2, 3, 4, 5, 6 ]
numbers = [int(num.strip()) for num in comma_separated_numbers if num.strip().isdigit()]
print(f"Numbers entered: {numbers}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Average of numbers: {sum(numbers)/len(numbers) if numbers else 0}")

# To check type of input
test_input = input("Enter something: ")
print(f"Type of input: {type(test_input)}")

# Type conversion/casting
score_input = input("Enter score: ")
try:
    score = int(score_input)
    print(f"My HSC score: {score}")
    print(f"100 + score = {100 + score}")
except ValueError:
    print("Invalid score entered. Please enter a numeric value.")

# Additional: Ask for age and check if user is adult
age_input = input("Enter your age: ")
try:
    age = int(age_input)
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")
except ValueError:
    print("Invalid age entered. Please enter a numeric value.")
