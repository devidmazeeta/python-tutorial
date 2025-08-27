# Demonstration of Python Operators

# Arithmetic Operators (+, -, *, /, %, **, //)
num_a = 2
num_b = 4
print("Arithmetic Operators:")
print(f"{num_a} + {num_b} = {num_a + num_b}")   # 6
print(f"{num_a} - {num_b} = {num_a - num_b}")   # -2
print(f"{num_a} * {num_b} = {num_a * num_b}")   # 8
print(f"{num_a} / {num_b} = {num_a / num_b}")   # 0.5
print(f"{num_a} % {num_b} = {num_a % num_b}")   # 2
print(f"{num_a} ** {num_b} = {num_a ** num_b}") # 16
print(f"{num_b} // {num_a} = {num_b // num_a}") # 2

floor_div_result = 10 // 3
print(f"10 // 3 = {floor_div_result}") # 3

print("\nComparison Operators:")
# Comparison Operators (==, !=, >, <, >=, <=)
value_x = 10
value_y = 20
print(f"{value_x} == {value_y}: {value_x == value_y}")
print(f"{value_x} != {value_y}: {value_x != value_y}")
print(f"{value_x} > {value_y}: {value_x > value_y}")
print(f"{value_x} < {value_y}: {value_x < value_y}")
print(f"{value_x} >= {value_y}: {value_x >= value_y}")
print(f"{value_x} <= {value_y}: {value_x <= value_y}")

if value_x < value_y:
    print("Condition satisfied: value_x is less than value_y")

print("\nLogical Operators:")
# Logical Operators (and, or, not)
is_flag1 = True
is_flag2 = True
is_flag3 = False
is_flag4 = False

print(f"is_flag1 and is_flag2: {is_flag1 and is_flag2}")
print(f"is_flag1 or is_flag3: {is_flag1 or is_flag3}")
print(f"not is_flag3: {not is_flag3}")

if is_flag1 and is_flag2:
    print("And passed")

if is_flag1 or is_flag3:
    print("Or passed")

if is_flag3 or is_flag4:
    print("Or passed")
else:
    print("Or failed")

if not is_flag3: # True
    print("Not passed")

print("\nAssignment Operators:")
# Assignment Operators (+=, -=, *=, /=, //=, %=, **=)
number_val = 10
print(f"Initial value: {number_val}")
number_val += 20
print(f"After += 20: {number_val}") # 30
number_val -= 5
print(f"After -= 5: {number_val}") # 25
number_val *= 2
print(f"After *= 2: {number_val}") # 50
number_val /= 5
print(f"After /= 5: {number_val}") # 10.0
number_val //= 3
print(f"After //= 3: {number_val}") # 3.0
number_val %= 2
print(f"After %= 2: {number_val}") # 1.0
number_val **= 3
print(f"After **= 3: {number_val}") # 1.0

print("\nBitwise Operators:")
# Bitwise Operators (&, |, ^, ~, <<, >>)
a = 5  # 0b0101
b = 3  # 0b0011
print(f"{a} & {b} = {a & b}")   # 1
print(f"{a} | {b} = {a | b}")   # 7
print(f"{a} ^ {b} = {a ^ b}")   # 6
print(f"~{a} = {~a}")           # -6
print(f"{a} << 1 = {a << 1}")   # 10
print(f"{a} >> 1 = {a >> 1}")   # 2

print("\nMembership Operators:")
# Membership Operators (in, not in)
sample_list = [1, 2, 3, 4, 5]
print(f"3 in sample_list: {3 in sample_list}")
print(f"6 not in sample_list: {6 not in sample_list}")

print("\nIdentity Operators:")
# Identity Operators (is, is not)
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is y: {x is y}")       # False
print(f"x is z: {x is z}")       # True
print(f"x is not y: {x is not y}") # True
