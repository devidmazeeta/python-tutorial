# Dictionary
# Creating a dictionary with personal information
person_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Dictionary:", person_info)
print("Name:", person_info["name"])

# Adding a new key-value pair
person_info["profession"] = "Engineer"
print("Updated Dictionary:", person_info)

# Accessing all keys and values
print("Keys:", person_info.keys()) # Keys: dict_keys(['name', 'age', 'city', 'profession'])
print("Keys:", list(person_info.keys())) # Keys: ['name', 'age', 'city', 'profession']
print("Values:", list(person_info.values())) # Values: ['Alice', 25, 'New York', 'Engineer']

# Updating an existing value
person_info["age"] = 26
print("After updating age:", person_info) # After updating age: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Removing a key-value pair
removed_value = person_info.pop("city")
print("Removed 'city':", removed_value) # Removed 'city': New York
print("Dictionary after removal:", person_info) # Dictionary after removal: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

# Key Error
# print(person_info["country"]) # KeyError: 'country'

# Checking if a key exists
if "country" in person_info:
    print("key 'country' exists in the dictionary.")
    print(person_info["country"])
else:
    print("key 'country' does not exist in the dictionary.")

if "country" not in person_info:
    print("key 'country' does not exist in the dictionary.")
else:
    print("key 'country' exists in the dictionary.")
