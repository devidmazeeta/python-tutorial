# Chapter 3: Data Structures in Python

Data structures allow you to store and organize data efficiently. Python offers several built-in data structures that are versatile and easy to use.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Understand the need for data structures.
- Use Python's built-in data structures: **lists**, **tuples**, **sets**, and **dictionaries**.
- Perform common operations like indexing, slicing, adding, removing, and updating data.
- Understand mutability and immutability.
- Choose the appropriate data structure for a problem.

---

## 🚩 Learning Order of Programs

1. [Numeric](../03_Data_Structures/numeric.py)  
2. [Boolean](../03_Data_Structures/boolean.py)  
3. [Sequence Type](../03_Data_Structures/sequencetype.py)  
4. [Dictionary](../03_Data_Structures/dictionary.py)  
5. [Set Data Type](../03_Data_Structures/setdatatype.py)  
6. [Methods](../03_Data_Structures/methods.py)

---

## Python Data Types Overview

Below is a visual representation of Python data types:

![Python Data Types](./pythondatastructures.png)

---

## 1. Lists

**Lists** are ordered, mutable collections of items. They can contain elements of different types.

**Creating a List:**
```python
fruits = ["apple", "banana", "cherry"]
```

**Accessing Elements:**
```python
print(fruits[0])      # apple
print(fruits[-1])     # cherry
```

**Slicing:**
```python
print(fruits[0:2])    # ['apple', 'banana']
```

**Modifying Lists:**
```python
fruits[1] = "blueberry"
fruits.append("orange")
fruits.insert(1, "kiwi")
print(fruits)
```

**Removing Elements:**
```python
fruits.remove("apple")
popped_item = fruits.pop()
del fruits[0]
```

**List Methods:**
```python
numbers = [1, 2, 3, 4]
print(len(numbers))   # 4
print(sum(numbers))   # 10
numbers.sort(reverse=True)
```

---

## 2. Tuples

**Tuples** are ordered, immutable collections. They are faster than lists and useful for fixed data.

**Creating a Tuple:**
```python
coordinates = (10, 20)
single_item = (5,)  # Note the comma
```

**Accessing Elements:**
```python
print(coordinates[0])  # 10
```

**Why Tuples?**
- Data integrity (unchangeable).
- Can be used as keys in dictionaries.

---

## 3. Sets

**Sets** are unordered collections of unique items.

**Creating a Set:**
```python
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}
```

**Adding and Removing:**
```python
unique_numbers.add(4)
unique_numbers.remove(2)
```

**Set Operations:**
```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # Union {1, 2, 3, 4, 5}
print(A & B)   # Intersection {3}
print(A - B)   # Difference {1, 2}
```

---

## 4. Dictionaries

**Dictionaries** store key-value pairs. Keys must be unique and immutable.

**Creating a Dictionary:**
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```

**Accessing and Modifying:**
```python
print(person["name"])
person["age"] = 26
person["email"] = "alice@example.com"
```

**Dictionary Methods:**
```python
print(person.keys())
print(person.values())
print(person.items())
```

**Looping Through a Dictionary:**
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 5. Mutability and Immutability

- **Lists, sets, dictionaries** are mutable (can be changed).
- **Tuples and strings** are immutable (cannot be changed).

**Example:**
```python
my_list = [1, 2, 3]
my_list.append(4)   # Allowed

my_tuple = (1, 2, 3)
# my_tuple[0] = 5   # Error: TypeError
```

---

## 6. Choosing the Right Data Structure

- **List:** Ordered, mutable sequence of items.
- **Tuple:** Ordered, immutable, fixed collection.
- **Set:** Unique, unordered items, good for membership tests.
- **Dictionary:** Key-value mapping, fast lookups.

---

## 7. Methods Summary

| Data Structure | Common Methods/Functions               | Description                          |
|----------------|---------------------------------------|--------------------------------------|
| List           | `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `len()` | Add, remove, sort elements, get length |
| Tuple          | `count()`, `index()`                  | Count occurrences, find index        |
| Set            | `add()`, `remove()`, `union()`, `intersection()` | Add/remove elements, set operations |
| Dictionary     | `keys()`, `values()`, `items()`, `get()` | Access keys/values, get items        |

---

## Exercises

1. Create a list of your 5 favorite movies and:
   - Replace the third movie.
   - Add a new movie to the end.
   - Remove one movie.

2. Store the following data as a tuple: `(latitude, longitude, elevation)`.

3. Create two sets of numbers and:
   - Find their union, intersection, and difference.

4. Create a dictionary for a student containing name, roll number, and grades in three subjects. Update one subject’s grade.

5. Write a program to count the occurrence of each word in a sentence using a dictionary.

---

## Next Steps

Proceed to **[Chapter 4: Control Flow](../04_Control_Flow/README.md)** to learn how to make decisions and loop through data.
