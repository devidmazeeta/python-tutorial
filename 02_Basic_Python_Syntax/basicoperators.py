# Demonstration of Python Operators

# Arithmetic Operators (+, -, *, /, %, **, //)
num_a = 2
num_b = 4
print("Arithmetic Operators:")
print(f"{num_a} + {num_b} = {num_a + num_b}")   # 2 + 4 = 6
print(f"{num_a} - {num_b} = {num_a - num_b}")   # 2 - 4 = -2
print(f"{num_a} * {num_b} = {num_a * num_b}")   # 2 * 4 = 8
print(f"{num_a} / {num_b} = {num_a / num_b}")   # 2 / 4 = 0.5
print(f"{num_a} % {num_b} = {num_a % num_b}")   # 2 % 4 = 2
print(f"{num_a} ** {num_b} = {num_a ** num_b}") # 2 ** 4 = 16
print(f"{num_b} // {num_a} = {num_b // num_a}") # 2 // 4 = 0

floor_div_result = 10 // 3
print(f"10 // 3 = {floor_div_result}") # 10 // 3 = 3

print("\nComparison Operators:")
# Comparison Operators (==, !=, >, <, >=, <=)
value_x = 10
value_y = 20
print(f"{value_x} == {value_y}: {value_x == value_y}") # 10 == 20: False
print(f"{value_x} != {value_y}: {value_x != value_y}") # 10 != 20: True
print(f"{value_x} > {value_y}: {value_x > value_y}") # 10 > 20: False
print(f"{value_x} < {value_y}: {value_x < value_y}") # 10 < 20: True
print(f"{value_x} >= {value_y}: {value_x >= value_y}") # 10 >= 20: False
print(f"{value_x} <= {value_y}: {value_x <= value_y}") # 10 <= 20: True

if value_x < value_y:
    print("Condition satisfied: value_x is less than value_y")

print("\nLogical Operators:")
# Logical Operators (and, or, not)
# Logical Operators Truth Table:
# A      B      A and B    A or B    not A
# True   True   True       True      False
# True   False  False      True      False
# False  True   False      True      True
# False  False  False      False     True
is_flag1 = True
is_flag2 = True
is_flag3 = False
is_flag4 = False

print(f"is_flag1 and is_flag2: {is_flag1 and is_flag2}") # is_flag1 and is_flag2: True
print(f"is_flag1 or is_flag3: {is_flag1 or is_flag3}") # is_flag1 or is_flag3: True
print(f"not is_flag3: {not is_flag3}") # not is_flag3: True

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
print(f"Initial value: {number_val}") # Initial value: 10
# number_val = number_val + 20
number_val += 20
print(f"After += 20: {number_val}") # After += 20: 30
number_val -= 5
print(f"After -= 5: {number_val}") # After -= 5: 25
number_val *= 2
print(f"After *= 2: {number_val}") # After *= 2: 50
number_val /= 5
print(f"After /= 5: {number_val}") # After /= 5: 10.0
number_val //= 3
print(f"After //= 3: {number_val}") # After //= 3: 3.0
number_val %= 2
print(f"After %= 2: {number_val}") # After %= 2: 1.0
number_val **= 3
print(f"After **= 3: {number_val}") # After **= 3: 1.0

print("\nBitwise Operators:")
# Bitwise Operators (&, |, ^, ~, <<, >>)
# Bitwise AND: Compares each bit of both numbers. If both bits are 1, the result bit is 1; otherwise, it's 0.
# 5 (0101) & 3 (0011) = 1 (0001)
print(f"{a} & {b} = {a & b}")   # 5 & 3 = 1

# Bitwise OR: Compares each bit. If at least one bit is 1, the result bit is 1; otherwise, it's 0.
# 5 (0101) | 3 (0011) = 7 (0111)
print(f"{a} | {b} = {a | b}")   # 5 | 3 = 7

# Bitwise XOR: Compares each bit. If the bits are different, the result bit is 1; if they're the same, it's 0.
# 5 (0101) ^ 3 (0011) = 6 (0110)
print(f"{a} ^ {b} = {a ^ b}")   # 5 ^ 3 = 6

# Bitwise NOT: Inverts all the bits. In Python, this gives the two's complement of the number.
# ~5 = -6 (in 2's complement representation)
print(f"~{a} = {~a}")           # ~5 = -6

# Left Shift: Shifts the bits of the number to the left by the specified number of positions.
# 5 (0101) << 1 = 10 (1010) - Equivalent to multiplying by 2
print(f"{a} << 1 = {a << 1}")   # 5 << 1 = 10

# Right Shift: Shifts the bits of the number to the right by the specified number of positions.
# 5 (0101) >> 1 = 2 (0010) - Equivalent to integer division by 2
print(f"{a} >> 1 = {a >> 1}")   # 5 >> 1 = 2

print("\nMembership Operators:")
# Membership Operators (in, not in)
sample_list = [1, 2, 3, 4, 5]
print(f"3 in sample_list: {3 in sample_list}") # 3 in sample_list: True
print(f"6 not in sample_list: {6 not in sample_list}") # 6 not in sample_list: True

print("\nIdentity Operators:")
# Identity Operators (is, is not)
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is y: {x is y}")       # x is y: False
print(f"x is z: {x is z}")       # x is z: True
print(f"x is not y: {x is not y}") # x is not y: True
