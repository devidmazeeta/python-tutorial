class Google:
    def welcome(self):
        raise NotImplementedError("Implement a method in sub class")

# Base class - Inherits parent class - Google
class PythonTeam(Google):
    # Method Overriding
    def welcome(self):
        print("Welcome to Python Team")

# Base class - Inherits parent class - Google
class JavaTeam(Google):
    # Method Overriding
    def welcome(self):
        print("Welcome to Python Team")

pythonObj = PythonTeam()
pythonObj.welcome()

javaObj = JavaTeam()
javaObj.welcome()

GoogleObj = Google()
# GoogleObj.welcome() # NotImplementedError: Implement a method in sub class

print ( 'abc' * 20 )

# Method Overloading
# A definition accepts more than one datatype of argument
# and functionality is differed based on it
print(len("Google")) # 5
print(len([10,20,30,40])) # 4
