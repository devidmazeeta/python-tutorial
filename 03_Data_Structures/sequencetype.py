# String
string_example = "Hello, World!"
print("String:", string_example) # String: Hello, World!
print("First character of string:", string_example[0]) # First character of string: H
# String methods
print(string_example.replace("World", "Python")) # Hello, Python
print(string_example) # Hello, World!
string_example = string_example.replace("World", "Python")
print(string_example) # Hello, Python!

# List
list_example = [1, 2, 3, "Python", 4.5]
print(list_example[3])  # Python
print(list_example[3][2])  # t
# Positive indexing
print(list_example[2])  # 3
print(list_example[3])  # Python
# Negative indexing
print(list_example[-3])  # 3
print(list_example[-2])  # Python
print("List:", list_example)
# List Methods
print(len(list_example))
list_example.append("Java")  # Adding an element at the end
print("Updated List:", list_example)
print(len(list_example))
list_example.insert(2, "C++")
print("Modified List:", list_example)
print(len(list_example))
list_example[0] = 9
print("Modified List:", list_example)
print(len(list_example))

# Tuple
tuple_example = (10, 20, "Tuple", 30.5)
print("Tuple:", tuple_example)
# tuple_example[0] = 99  # Error: Tuples are immutable
# tpl[0] = 99  # Error: Tuples are immutable
