# Demonstration of Python built-in data types and their common methods

# Numeric Type
num = 10
print("Numeric:")
print("Absolute value:", abs(-num))  # Returns the absolute value
print("Power:", pow(num, 2))         # num raised to the power of 2
print("Float:", float(num))          # Converts integer to float
print("Division:", num / 3)          # Division returns float
print("Integer Division:", num // 3) # Integer division
print("Modulo:", num % 3)            # Remainder of division
print()

# Boolean Type
bool_val = True
print("Boolean:")
print("Boolean as int:", int(bool_val))  # True -> 1, False -> 0
print("Negation:", not bool_val)         # Logical NOT
print("And with False:", bool_val and False) # Logical AND
print("Or with False:", bool_val or False)   # Logical OR
print()

# Sequence Types (List, Tuple, String)
seq_list = [1, 2, 3]
seq_tuple = (4, 5, 6)
seq_str = "hello"

print("Sequence Type:")
# List methods
print("List append (new list):", seq_list + [4])  # Concatenation
seq_list.append(5)                                # Append in-place
print("List after append:", seq_list)
print("List length:", len(seq_list))
print("List slice:", seq_list[1:3])               # Slicing

# Tuple methods
print("Tuple count of 5:", seq_tuple.count(5))    # Count occurrences
print("Tuple index of 6:", seq_tuple.index(6))    # Index of value

# String methods
print("String upper:", seq_str.upper())           # Uppercase
print("String replace:", seq_str.replace('l', 'x')) # Replace characters
print("String reversed:", seq_str[::-1])          # Reverse string
print("String length:", len(seq_str))
print()

# Dictionary Type
d = {'a': 1, 'b': 2}
print("Dictionary:")
print("Keys:", list(d.keys()))        # List of keys
print("Values:", list(d.values()))    # List of values
print("Get 'a':", d.get('a'))         # Get value for key 'a'
d['c'] = 3                            # Add new key-value pair
print("After adding 'c':", d)
print("Items:", list(d.items()))      # List of key-value pairs
print("Pop 'b':", d.pop('b'))         # Remove and return value for key 'b'
print("After pop:", d)
print()

# Set Data Type
s = {1, 2, 3}
print("Set Data Type:")
print("Add 4 (union):", s.union({4}))     # Union with another set
s.add(5)                                  # Add element in-place
print("Set after add:", s)
print("Remove 2 (difference):", s - {2})  # Difference
s.discard(3)                              # Remove element if present
print("Set after discard 3:", s)
print("Is 1 in set?", 1 in s)             # Membership test
print("Set length:", len(s))
print("Set intersection with {1, 5, 6}:", s.intersection({1, 5, 6}))
