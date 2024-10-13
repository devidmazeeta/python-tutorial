denominators = [1, 2, 3, 0, 5]
number = 100

for denom in denominators:
    try:
        result = number / denom
        print(result)
    except ZeroDivisionError as err: # Specifying exception class
        print("Caught an exception")
        print(err.args)

num1 = 10
while True:
    try:
        num2 = int(input("enter a number: "))
        break
    except:
        print("Please enter a valid number")

sum = num1+num2
print(sum)

try:
    text = "abc" + "def"
    # text = 10 + "abc"
    print(text)
except TypeError:
    print("Caught an exception - TypeError")
else: # Executes only when there is no exception
    print("Else block executed")
finally: # Mandatorily this block executes
    print("Finally block executed")
