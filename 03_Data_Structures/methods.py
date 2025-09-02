# Demonstration of Python built-in data types and their common methods

# Numeric Type
num = 10
print("Numeric:")
print("Absolute value:", abs(-num))  # Absolute value: 10
print("Power:", pow(num, 2))         # Power: 100
print("Float:", float(num))          # Float: 10.0
print("Division:", num / 3)          # Division: 3.3333333333333335
print("Integer Division:", num // 3) # Integer Division: 3
print("Modulo:", num % 3)            # Modulo: 1
print()

# Boolean Type
bool_val = True
print("Boolean:")
print("Boolean as int:", int(bool_val))      # Boolean as int: 1 (True -> 1, False -> 0)
print("Negation:", not bool_val)             # False (Logical NOT)
print("And with False:", bool_val and False) # False (Logical AND)
print("Or with False:", bool_val or False)   # True (Logical OR)
print()

print("Sequence Type:")
# List methods
seq_list = [1, 2, 3]
print("List append (new list):", seq_list + [4, 5]) # List append (new list): [1, 2, 3, 4, 5] (Concatenation)
seq_list.append(6)                                  # Append an element in-place
print("List after append:", seq_list)               # List after append: [1, 2, 3, 6]
new_seq_list = [7, 8, 9]
seq_list.extend(new_seq_list)                       # Append multiple elements in-place
print("List after extend:", seq_list)               # List after extend: [1, 2, 3, 6, 7, 8, 9]
print("New List:", new_seq_list)                    # New List: [7, 8, 9]
print("List length:", len(seq_list))                # List length: 7

# Sequence Slicing
# Syntax: list_object[start_index:stop_index:step] # Pass at least any one
print("List slice:", seq_list[1:3])    # [2, 3]
print("List slice:", seq_list[:3])     # [1, 2, 3]
print("List slice:", seq_list[1:])     # [2, 3, 6, 7, 8, 9]
print("List slice:", seq_list[1:6:3])  # [2, 7]
print("List slice:", seq_list[1:6:-3]) # []
print("List slice:", seq_list[6:1:-3]) # [9, 6]
print("List slice:", seq_list[::2])    # [1, 3, 7, 9]
print("List slice:", seq_list[::-1])   # [9, 8, 7, 6, 3, 2, 1] (Performs Reverse)

# Tuple methods
seq_tuple = (4, 5, 6, 5)
print("Tuple count of 5:", seq_tuple.count(5)) # Tuple count of 5: 2 (Count occurrences)
print("Tuple index of 6:", seq_tuple.index(6)) # Tuple index of 6: 2 (Index of value)
print("List slice:", seq_tuple[1:3])           # (5, 6)

# String methods
seq_str = "heLLo"
print("String upper:", seq_str.upper())      # HELLO
print("String lower:", seq_str.lower())      # hello
print("String replace:",
      seq_str.replace('L', 'x')) # hexxo (Replace characters)
print("String reversed:", seq_str[::-1])     # oLLeh (Reverse string)
print("String length:", len(seq_str))        # String length: 5
print()

# Dictionary Type
d = {'a': 1, 'b': 2}
print("Dictionary:")
print("Keys:", d.keys())           # Keys: dict_keys(['a', 'b'])
print("Keys:", list(d.keys()))     # Keys: ['a', 'b'] (List of keys)
print("Values:", list(d.values())) # Values: [1, 2] (List of values)
print("Get 'a':", d.get('a'))      # Get 'a': 1 (Get value for key 'a')
d['c'] = 3                         # Add new key-value pair
print("After adding 'c':", d)      # After adding 'c': {'a': 1, 'b': 2, 'c': 3}
print("Items:", list(d.items()))   # Items: [('a', 1), ('b', 2), ('c', 3)] (List of key-value pairs)
print("Pop 'b':", d.pop('b'))      # Pop 'b': 2 (Remove and return value for key 'b')
print("After pop:", d)             # After pop: {'a': 1, 'c': 3}
print()

# Set Data Type
s = {1, 2, 3}
print("Set Data Type:")
print("Add 4 (union):", s.union({4}))     # Add 4 (union): {1, 2, 3, 4} (Union with another set)
s.add(5)                                  # Add element in-place
print("Set after add:", s)                # Set after add: {1, 2, 3, 5}
print("Remove 2 (difference):", s - {2})  # Remove 2 (difference): {1, 3, 5}
s.discard(3)                              # Remove element if present
print("Set after discard 3:", s)          # Set after discard 3: {1, 5}
print("Is 1 in set?", 1 in s)             # Is 1 in set? True (Membership test)
print("Set length:", len(s))              # Set length: 2
print("Set intersection with {1, 5, 6}:",
      s.intersection({1, 5, 6}))          # Set intersection with {1, 5, 6}: {1, 5} (Intersection with another set)
