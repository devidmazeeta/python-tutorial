# Demonstrating nested conditional statements in Python
# This program categorizes fruits based on their name length and letter content

# Example fruits to demonstrate different conditions
fruits = ["Apple", "Kiwi", "Banana", "Grape", "Fig"]

for fruit in fruits:
    print(f"\nAnalyzing fruit: {fruit}")
    
    # First level: Check the length of the fruit name
    if len(fruit) > 4:
        print(f"  - {fruit} has more than 4 characters")
        
        # Nested condition: Check for specific letters in longer fruit names
        if "a" in fruit.lower():
            print(f"  - {fruit} contains the letter 'a'")
            print(f"  Result: {fruit} is a common fruit")  # Result: Banana is a common fruit
        else:
            print(f"  - {fruit} doesn't contain the letter 'a'")
            print(f"  Result: {fruit} is an uncommon fruit")  # Result: Grape is an uncommon fruit
    
    else:
        print(f"  - {fruit} has 4 or fewer characters")
        
        # Another nested condition: Check specific letters in shorter fruit names
        if "i" in fruit.lower():
            print(f"  - {fruit} contains the letter 'i'")
            print(f"  Result: {fruit} is a small fruit with 'i'")
            # Result: Kiwi is a small fruit with 'i'
        elif "g" in fruit.lower():
            print(f"  - {fruit} contains the letter 'g'")
            print("  Result: Small fruit with 'g'")
        else:
            print(f"  - {fruit} doesn't match our special cases")
            print(f"  Result: {fruit} is a basic small fruit")  # Result: Fig is a basic small fruit

# Note: This example demonstrates how to use nested if-elif-else statements
# to create more complex decision-making structures in Python.
