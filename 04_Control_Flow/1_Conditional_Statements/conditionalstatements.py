# Control Flow:
#     - Conditional Statements
#     - Looping
#     - Comprehensions

# Syntax:
# if condition:
#     code lines

name = input("Enter the name: ") # Google

if name.lower() == "google":
    print("Name is Google")

if len(name) == 6: # Google => True, Tesla => False
    print("Length of the given name is 5")

# Not
if not len(name) == 5:
    print("Length of the given name is not 5")
