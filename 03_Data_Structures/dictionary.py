# Dictionary
# Creating a dictionary with personal information
person_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Print the dictionary
print("Dictionary:", person_info)

# Access a value by key
print("Name:", person_info["name"])

# Add a new key-value pair
person_info["profession"] = "Engineer"
print("Updated Dictionary:", person_info)

# Access all keys and values
print("Keys:", person_info.keys())  # Keys: dict_keys(['name', 'age', 'city', 'profession'])
print("Keys:", list(person_info.keys()))  # Keys: ['name', 'age', 'city', 'profession']
print("Values:", list(person_info.values()))  # Values: ['Alice', 25, 'New York', 'Engineer']

# Update an existing value
person_info["age"] = 26
print("After updating age:", person_info)  # After updating age: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Remove a key-value pair
removed_value = person_info.pop("city")
print("Removed 'city':", removed_value)  # Removed 'city': New York
print("Dictionary after removal:", person_info)  # Dictionary after removal: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

# Handle KeyError using get() method
print("Get 'country':", person_info.get('country'))  # Get 'country': None

# Check if a key exists
if "country" in person_info:
    print("Key 'country' exists in the dictionary.")
    print(person_info["country"])
else:
    print("Key 'country' does not exist in the dictionary.")

if "country" not in person_info:
    print("Key 'country' does not exist in the dictionary.")
else:
    print("Key 'country' exists in the dictionary.")

# Create an empty dictionary
dict_example1 = {}
print("Empty Dictionary:", dict_example1)  # Empty Dictionary: {}
dict_example2 = dict()
print("Empty Dictionary:", dict_example2)  # Empty Dictionary: {}
