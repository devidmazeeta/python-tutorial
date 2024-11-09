import json

# Generating JSON:
# Create a Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

# Convert dictionary to JSON string
json_string = json.dumps(data)

print(json_string)

# Parsing JSON:
# Sample JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON data into a Python dictionary
data = json.loads(json_data)

# Access values
print(data["name"])
print(data["age"])
