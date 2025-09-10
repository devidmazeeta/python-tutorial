# ===================================================
# DEFINING AND CALLING FUNCTIONS IN PYTHON
# ===================================================
# Functions are blocks of reusable code that perform a specific task.
# They help in organizing code, improving reusability, and making the code more readable.

# ===================================================
# 1. BASIC FUNCTION DEFINITION AND CALLING
# ===================================================
def greet():
    """A simple function that prints a greeting message."""
    print("Welcome to the greet function!")  # This will print when the function is called

# Function call - executes the code inside the function
greet()  # Output: Welcome to the greet function!

# ===================================================
# 2. FUNCTIONS WITH RETURN STATEMENT
# ===================================================
def get_greeting():
    """
    Returns a greeting message.
    The return statement sends a value back to the caller.
    """
    greeting_text = "Hello from get_greeting function!"
    return greeting_text

# Calling and storing the returned value
message = get_greeting()
print(message)  # Output: Hello from get_greeting function!

# Directly using the returned value
print(get_greeting())  # Output: Hello from get_greeting function!

# ===================================================
# 3. FUNCTION WITH MULTIPLE RETURN STATEMENTS
# ===================================================
def check_number(num):
    """Returns a message based on the number's value."""
    if num > 0:
        return "Positive number"  # First return statement
    elif num < 0:
        return "Negative number"  # Second return statement
    else:
        return "Zero"  # Third return statement

# Testing the function with different inputs
print(check_number(5))  # Output: Positive number
print(check_number(-3))  # Output: Negative number
print(check_number(0))  # Output: Zero

# ===================================================
# 4. FUNCTION WITHOUT RETURN STATEMENT
# ===================================================
def print_message():
    """Prints a message but doesn't return any value."""
    print("This function performs an action but returns None")

# The function returns None by default
result = print_message()  # Output: This function performs an action but returns None
print("Return value:", result)  # Output: Return value: None

# ===================================================
# 5. FUNCTION DOCSTRINGS
# ===================================================
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The calculated area
    """
    return length * width

# Accessing the calculate_area function
print(calculate_area(10.1,20))

# Accessing the docstring
print(calculate_area.__doc__)  # Output: The docstring will be printed

# ===================================================
# 6. FUNCTION CALLING OTHER FUNCTIONS
# ===================================================
def greet_user(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}! Welcome!"

def greet_morning():
    """Calls greet_user with a default name."""
    return greet_user("Morning User")

print(greet_morning())  # Output: Hello, Morning User! Welcome!
