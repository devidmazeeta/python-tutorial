# Syntax:
# from <packagename> import <module_name>

from datetime import datetime as dt
import math as ma

print("Today : ", end="")
print(dt.today())
print("Pi : ", end="")
print(ma.pi)
print("Square Root : ", end="")
print(ma.sqrt(16))
print("Power : ", end="")
print(ma.pow(2, 4))
print("Flooring Round : ", end="")
print(ma.floor(7.5))
print("Ceiling Round : ", end="")
print(ma.ceil(7.5))
