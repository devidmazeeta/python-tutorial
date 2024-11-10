# Syntax:
# raise ExceptionName(message)

try:
    raise ValueError("This is custom error message for ValueError!")
    raise NameError("This is custom error message for NameError!") # This line will not execute
except NameError:
    print("Caught an exception - NameError!")
    raise
except ValueError:
    print("Caught an exception - ValueError!")
    raise
