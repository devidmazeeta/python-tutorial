"""
Conditional Statements in Python
--------------------------------
This script demonstrates the use of conditional statements (if, elif, else) in Python
to make decisions based on different conditions.
"""

# Get user input
name = input("Enter a name: ").strip()  # Remove any leading/trailing whitespace

# Simple if statement
if name.lower() == "google":
    print(f"Hello, {name}! You entered 'Google' (case-insensitive check)")
    # Output if input is "Google" or "GOOGLE" or "google": Hello, Google! You entered 'Google' (case-insensitive check)
