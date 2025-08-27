# Variables and Assignments

number = 100 # Integer
score = 90.56  # Float
fruit_name = "Apple"  # String

# Basic Data Types (int, float, str, bool)
flag_str = "True"  # String
flag_bool = True  # Boolean

if flag_bool:
    print("Condition satisfied")

# Type Conversion and Casting
# Syntax => type(variable_name)

# String to Integer conversion
string_count = "50"  # String
print("Before conversion:", string_count, "| Type:", type(string_count))
int_count = int(string_count)  # Converts string to integer
print("After conversion:", int_count, "| Type:", type(int_count))

# Integer to String conversion
int_num = 1234
print("Before conversion:", int_num, "| Type:", type(int_num))
string_num = str(int_num)
print("After conversion:", string_num, "| Type:", type(string_num))

# Float to Integer conversion
float_num = 45.67
print("Before conversion:", float_num, "| Type:", type(float_num))
int_from_float = int(float_num)
print("After conversion (truncated):", int_from_float, "| Type:", type(int_from_float))

# Boolean to Integer and String
bool_val = False
print("Boolean value:", bool_val, "| Type:", type(bool_val))
int_from_bool = int(bool_val)
str_from_bool = str(bool_val)
print("As integer:", int_from_bool, "| Type:", type(int_from_bool))
print("As string:", str_from_bool, "| Type:", type(str_from_bool))

# User input example (uncomment to use)
# user_input = input("Enter a number: ")
# print("You entered:", user_input, "| Type:", type(user_input))
# converted_input = int(user_input)
# print("Converted to integer:", converted_input, "| Type:", type(converted_input))
