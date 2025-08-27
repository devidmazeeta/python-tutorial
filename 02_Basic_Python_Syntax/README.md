# Chapter 2: Basic Python Syntax

Python syntax refers to the rules that define how programs are written and interpreted. Mastering the basic syntax is essential for writing clear, efficient, and error-free code.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Understand how Python code is structured using **indentation**.
- Use **comments and documentation** effectively to make your code readable.
- Create and use **variables** with Python’s **dynamic typing**.
- Work with Python’s **basic data types** and perform operations using **operators**.
- Use **print statements** for output and **input** for user interaction.

---

## 🚩 Learning Order of Programs

1. [Syntax and Indentation](syntaxandindentation.py)
2. [Comment Lines](commentlines.py)
3. [Print Statement](printstatement.py)
4. [String Formatting](stringformatting.py)
5. [Variables and Data Types](variablesanddatatypes.py)
6. [Input and Output](inputandoutput.py)
7. [Basic Operators](basicoperators.py)
8. [Logical Operators](logicaloperators.py)

---

## 1. Indentation and Code Blocks

Unlike many languages that use braces `{}` or keywords to define blocks, Python uses **indentation**. Proper indentation is critical and not optional.

### Key Points:
- Standard indentation: **4 spaces**.
- Do not mix tabs and spaces.
- Incorrect indentation causes `IndentationError`.

**Example:**

```python
if True:
    print("This block is indented correctly")
    print("All lines inside the block must be indented equally")
else:
    print("This is another block")
```

**Bad Example:**

```python
if True:
print("This will throw an IndentationError")  # ❌ Wrong indentation
```

---

## 2. Comments and Documentation

Comments are used to explain the code and are ignored during execution.

- **Single-line comments** start with `#`.
- **Multi-line comments** or **docstrings** use triple quotes `''' ... '''`.
- Docstrings can also document **functions, classes, and modules**.

**Examples:**

```python
# This is a single-line comment

'''
This is a multi-line comment
often used for documentation.
'''

def greet(name):
    '''This function greets a person by name.'''
    return f"Hello, {name}!"
```

**Best Practice:** Write clear, concise comments; avoid obvious comments like `# add two numbers` for `a + b`.

---

## 3. Variables and Assignment

Python variables are created when you assign them a value. There’s no need to declare the type explicitly.

### Key Points:
- Variables are **dynamically typed**.
- Valid names: letters, numbers, and underscores; cannot start with a number.
- Case-sensitive: `Name` and `name` are different.

**Example:**

```python
age = 25
name = "Alice"
is_student = True

print(name, "is", age, "years old.")
```

**Multiple Assignment:**

```python
x, y, z = 1, 2, 3
a = b = c = 0  # All assigned 0
```

**Swapping Values:**

```python
x, y = y, x
```

---

## 4. Basic Data Types

Python has several built-in data types. At this stage, we focus on the most common:

- **Numeric Types:** `int`, `float`, `complex`
- **Text Type:** `str`
- **Boolean Type:** `bool`

**Examples:**

```python
integer_value = 42        # int
float_value = 3.14159     # float
complex_value = 2 + 3j    # complex
text = "Python is fun!"   # str
flag = False              # bool
```

**Useful Functions:**

```python
print(type(integer_value))   # <class 'int'>
print(isinstance(text, str)) # True
```

**String Operations:**

```python
greeting = "Hello"
name = "Bob"
full_greeting = greeting + " " + name  # Concatenation
print(full_greeting)
print(greeting * 3)  # Repeats string
```

---

## 5. Operators and Expressions

Operators are symbols that perform operations on variables and values.

### Arithmetic Operators:
`+`, `-`, `*`, `/`, `//`, `%`, `**`

```python
a, b = 7, 3
print(a + b)   # 10
print(a / b)   # 2.333...
print(a // b)  # 2 (floor division)
print(a % b)   # 1 (modulo)
print(a ** b)  # 343 (power)
```

### Comparison Operators:
`==`, `!=`, `<`, `>`, `<=`, `>=`

```python
print(a > b)   # True
print(a == 7)  # True
```

### Logical Operators:
`and`, `or`, `not`

```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

### Assignment Operators:
`=`, `+=`, `-=`, `*=`, `/=`, etc.

```python
count = 5
count += 2  # count = 7
```

---

## 6. Input and Output

- **Output:** `print()`
- **Input:** `input()` returns data as **string**; convert if needed.

**Examples:**

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

**Important:** Always handle type conversion when reading numbers.

---

## 7. Best Practices

- Follow **PEP 8** style guidelines for naming and indentation.
- Use descriptive variable names (`total_amount` vs. `x`).
- Keep comments meaningful and updated.

---

## Exercises

1. Write a program to:
   - Ask for your first and last name.
   - Print them in reverse order separated by a space.

2. Take two numbers from the user:
   - Perform all arithmetic operations and print results.
   - Show which number is greater using comparison operators.

3. Explain what happens if you divide by zero. Try catching this error and print a friendly message.

4. Write a script with **multi-line comments** explaining each section.

---

## Next Steps

Move to **[Chapter 3: Data Structures](../03_Data_Structures/README.md)** to learn how to store and manage collections of data efficiently.
