# Method 1 - Concatenation using + operator
company_name = "Google"
company_suffix = "Inc."
print(company_name + " " + company_suffix)

# string + string -> Concatenation (e.g., "Hello" + "World" = "HelloWorld")
# num + num -> Addition (e.g., 2 + 3 = 5)
# string + num or num + string -> TypeError (cannot concatenate str and int)


# Method 2 - '%' or C-style String Formatting
# %s for String
# %d for integer
# %f for float
person_name = "Arun" # String
person_age = 25 # Integer
person_score = 99.126456 # Float
print("%s age is %d. He has scored %.2f in HSC." % (person_name, person_age, person_score))


# Method 3 - .format() method
print("{} age is {}. He has scored {} in HSC.".format(
    person_name,
    person_age,
    person_score
))  # Arun age is 25. He has scored 99.126456 in HSC.

print("{0} age is {2}. He has scored {1} in HSC.".format(
    person_name,
    person_age,
    person_score
))  # Arun age is 25. He has scored 99.126456 in HSC.


# Method 4 - f'string
employee_name = "Alex"
employee_company = "Google"
print("{employee_name} works in {employee_company}") # {employee_name} works in {employee_company}
print(f"{employee_name} works in {employee_company}") # Alex works in Google

water_amount = 1.5
times_per_day = 4
total_water_amount = water_amount * times_per_day
print(f"{employee_name} works in {employee_company}. He drinks {total_water_amount} of water per day.")
print(f"{employee_name} works in {employee_company}. He drinks {water_amount * times_per_day} of water per day.")

fruits = {
    "apple": 10,
    "orange": 20,
}
print(f"Apple count are {fruits['apple']}")
