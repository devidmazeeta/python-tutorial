# Demonstration of Set Data Structure in Python

# Creating a set with duplicate elements
unique_numbers = {1, 2, 3, 4, 5, 1, 2, 6}
print("Unique numbers set:", unique_numbers)  # {1, 2, 3, 4, 5, 6}

# Defining two sets for set operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print("Set A:", set_a)
print("Set B:", set_b)

# Set Operations
print("Union:", set_a | set_b)  # {1, 2, 3, 4, 5, 6, 7}
print("Intersection:", set_a & set_b)  # {3, 4, 5}
print("Difference (A - B):", set_a - set_b)  # {1, 2}
print("Difference (B - A):", set_b - set_a)  # {6, 7}
print("Symmetric Difference:", set_a ^ set_b)  # {1, 2, 6, 7}

# Set Methods
unique_numbers.add(9)
print("After adding 9:", unique_numbers)  # {1, 2, 3, 4, 5, 6, 9}

# Removing an element
unique_numbers.discard(2)
print("After discarding 2:", unique_numbers)

# Checking membership
print("Is 3 in unique_numbers?", 3 in unique_numbers)

# Converting list to set to remove duplicates
number_list = [1, 2, 3, 4, 1, 2, 5]
unique_from_list = set(number_list)
print("Unique elements from list:", unique_from_list)  # {1, 2, 3, 4, 5}

# Converting set back to list
list_from_set = list(unique_from_list)
print("List from set:", list_from_set)  # [1, 2, 3, 4, 5]
