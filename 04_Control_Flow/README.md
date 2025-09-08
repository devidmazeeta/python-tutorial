# Chapter 4: Control Flow in Python

Control flow statements determine the order in which the program's code executes. They help in decision making, repeating code, and managing the flow of execution.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Make decisions in your code using conditional statements
- Execute code repeatedly using different types of loops
- Control the flow of loops with `break` and `continue`
- Write concise code using Python's comprehensions
- Choose the right control flow structure for different programming scenarios

---

## 🚩 Learning Order of Programs

### 1. Conditional Statements
1. [if-else Statements](1_Conditional_Statements/ifelse.py)
2. [if-elif-else Statements](1_Conditional_Statements/ifelifelse.py)
3. [Nested Conditions](1_Conditional_Statements/nestedconditions.py)
4. [Ternary Operations](1_Conditional_Statements/ternaryoperation.py)
5. [Conditional Statements Overview](1_Conditional_Statements/conditionalstatements.py)

### 2. Loops
1. [for Loops](2_Loops/forloop.py)
2. [while Loops](2_Loops/whileloop.py)
3. [Using range()](2_Loops/ranges.py)
4. [break and continue](2_Loops/breakandcontinue.py)

### 3. Comprehensions
1. [List Comprehensions](3_Comprehensions/listcomprehensions.py)
2. [Dictionary Comprehensions](3_Comprehensions/dictcomprehensions.py)
3. [Set Comprehensions](3_Comprehensions/setcomprehensions.py)

---

## 1. Conditional Statements

Conditional statements allow you to execute different blocks of code based on certain conditions.

### if-else Statement
```python
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```

### if-elif-else Statement
```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
else:
    # code to execute if all conditions are False
```

### Ternary Operator
```python
value_if_true if condition else value_if_false
```

---

## 2. Loops

Loops allow you to execute a block of code multiple times.

### for Loop
```python
for item in iterable:
    # code to execute for each item
```

### while Loop
```python
while condition:
    # code to execute while condition is True
```

### Loop Control
- `break`: Exit the loop immediately
- `continue`: Skip the rest of the current iteration and move to the next one
- `else`: Executed when the loop completes normally (not with a break)

---

## 3. Comprehensions

Comprehensions provide a concise way to create collections (lists, dictionaries, sets) from existing iterables.

### List Comprehension
```python
new_list = [expression for item in iterable if condition]
```

### Dictionary Comprehension
```python
new_dict = {key: value for item in iterable if condition}
```

### Set Comprehension
```python
new_set = {expression for item in iterable if condition}
```

---

## Practice Exercises

1. Write a program that prints numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

2. Create a program that takes a list of numbers and returns a new list with only the even numbers squared, using list comprehension.

3. Write a program that takes a sentence and returns a dictionary where the keys are the words and the values are the lengths of the words, using dictionary comprehension.

4. Implement a program that checks if a number is prime using a while loop.

5. Create a program that takes a list of strings and returns a new list with all strings that have a length greater than 5, converted to uppercase, using list comprehension.

---

## Next Steps

Proceed to **[Chapter 5: Functions and Modules](../05_Functions_and_Modules/README.md)** to learn how to organize your code into reusable and maintainable components.
