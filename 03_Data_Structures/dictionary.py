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
print("Keys:", list(person_info.keys()))
print("Values:", list(person_info.values()))

# Updating an existing value
person_info["age"] = 26
print("After updating age:", person_info)

# Removing a key-value pair
removed_value = person_info.pop("city")
print("Removed 'city':", removed_value)
print("Dictionary after removal:", person_info)

# Checking if a key exists
if "profession" in person_info:
    print("Profession exists in the dictionary.")
else:
    print("Profession does not exist in the dictionary.")
