# ===================================================
# FUNCTION PARAMETERS AND ARGUMENTS IN PYTHON
# ===================================================
# Parameters are the variables listed inside the parentheses in the function definition.
# Arguments are the values passed to the function when it is called.

# ===================================================
# 1. POSITIONAL ARGUMENTS
# ===================================================
def add_numbers(num1, num2):
    """
    Adds two numbers and returns the result.

    Args:
        num1 (int/float): First number
        num2 (int/float): Second number

    Returns:
        int/float: Sum of num1 and num2
    """
    return num1 + num2

print("=== Positional Arguments ===")
result = add_numbers(10, 20)
print(f"10 + 20 = {result}")  # Output: 10 + 20 = 30

# ===================================================
# 2. KEYWORD ARGUMENTS
# ===================================================
def greet_user(name, message):
    """
    Greets a user with a custom message.

    Args:
        name (str): Name of the user
        message (str): Greeting message
    """
    print(f"{message}, {name}!")

print("\n=== Keyword Arguments ===")
greet_user(name="Alice", message="Hello")  # Output: Hello, Alice!
greet_user(message="Hi there", name="Bob")  # Order doesn't matter with keyword args

# ===================================================
# 3. DEFAULT PARAMETER VALUES
# ===================================================
def power(base, exponent=2):
    """
    Returns base raised to the power of exponent.
    If exponent is not provided, defaults to 2 (square).
    """
    return base ** exponent

print("\n=== Default Parameters ===")
print(f"5 squared is {power(5)}")  # Output: 5 squared is 25
print(f"2^4 is {power(2, 4)}")  # Output: 2^4 is 16
print(f"3^3 is {power(base=3, exponent=3)}")  # Output: 3^3 is 27

# ===================================================
# 4. ARBITRARY ARGUMENTS (*args)
# ===================================================
def calculate_average(*numbers):
    """
    Calculates the average of any number of values.
    *args collects all positional arguments into a tuple.
    """
    if not numbers:  # Check if no arguments were passed
        return 0
    return sum(numbers) / len(numbers)

print("\n=== Arbitrary Arguments (*args) ===")
print(f"Average of 10, 20: {calculate_average(10, 20)}")  # Output: 15.0
print(f"Average of 1,2,3,4,5: {calculate_average(1, 2, 3, 4, 5)}")  # Output: 3.0
print(f"Average with no arguments: {calculate_average()}")  # Output: 0

# ===================================================
# 5. KEYWORD ARBITRARY ARGUMENTS (**kwargs)
# ===================================================
def print_student_info(**student):
    """
    Prints student information.
    **kwargs collects all keyword arguments into a dictionary.
    """
    print("\nStudent Information:")
    for key, value in student.items():
        print(f"{key.title()}: {value}")

print("\n=== Keyword Arbitrary Arguments (**kwargs) ===")
print_student_info(
    name="Alice",
    age=20,
    major="Computer Science",
    gpa=3.8
)

# Output:
# Student Information:
# Name: Alice
# Age: 20
# Major: Computer Science
# Gpa: 3.8

# ===================================================
# 6. COMBINING DIFFERENT ARGUMENT TYPES
# ===================================================
def create_profile(name, email, *skills, **additional_info):
    """
    Creates a user profile with required name/email,
    variable skills, and additional information.
    """
    print(f"\nCreating profile for {name} ({email})")
    if skills:
        print(f"Skills: {', '.join(skills)}")
    if additional_info:
        print("Additional Information:")
        for key, value in additional_info.items():
            print(f"  {key.title()}: {value}")

print("\n=== Combining Different Argument Types ===")
create_profile(
    "John Doe",
    "john@example.com",
    "Python", "JavaScript", "SQL",
    experience="5 years",
    location="New York",
    status="Active"
)
# Output:
# Creating profile for John Doe (john@example.com)
# Skills: Python, JavaScript, SQL
# Additional Information:
#   Experience: 5 years
#   Location: New York
#   Status: Active
