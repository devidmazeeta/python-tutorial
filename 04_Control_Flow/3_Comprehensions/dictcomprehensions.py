# Dict Comprehension
# Simply a looping + condition
# Used to filter data & convert List => Dictionary

# Dict Comprehension Syntax
# listVar = { keyExpression: valueExpression for itemVar in iterable if condition }
# listVar = { keyExpression: valueExpression for itemVar in iterable }

fruits = {
    "apple": 7,
    "orange": 20,
    "grapes": 10,
    "pineapple": 6,
    "watermelon": 3,
    "kiwi": 25,
}

orderCount = { fruitName: 10 - stockCount for fruitName, stockCount in fruits.items() if stockCount < 10 }
print(orderCount) # { "apple": 3, "pineapple": 4, "watermelon": 7 }

# To find the occurrence of elements in a list
# Normal Method
elements = [
    10,
    10,
    "abc",
    20,
    "def",
    "def",
    "100",
    30,
    "GHI",
    "Xyz"
]

occurrence = {}
for element in elements:
    if not element in occurrence.keys():
        occurrence[element] = 1
    else:
        occurrence[element] += 1 # occurrence[value] = occurrence[value] + 1
print("******* Normal Method *********")
print(occurrence) # { 10: 2, "abc": 1, "def": 2, "100": 1, 30: 1, "GHI": 1, "Xyz": 1 }

# Comprehension Method
occurrence = { element: elements.count(element) for element in elements }
print("******* Dict Comprehension *********")
print(occurrence) # { 10: 2, "abc": 1, "def": 2, "100": 1, 30: 1, "GHI": 1, "Xyz": 1 }
