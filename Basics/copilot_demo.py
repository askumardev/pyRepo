# python3 Basics/copilot_demo.py

# # Write a python program to reverse a string without using any built-in functions.

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# input_str = "Hello, World!"
# print("Original String:", input_str)
# print("Reversed String:", reverse_string(input_str))

# below is a ruby code snippet. provide a python code snippet that does the same thing.
# def adult?(dob)
#   age = (Time.now - dob) / (365 * 24 * 60 * 60)
#   age >= 18
# end
# from datetime import datetime, timedelta  
# def adult(dob):
#     age = (datetime.now() - dob).total_seconds() / (365 * 24 * 60 * 60)
#     return age >= 18

# #but this is not a complete code snippet. consider the following inputs
# Inaccurate age calculation:

# It approximates a year as 365 days — ignores leap years.

# It assumes Time.now is in the same time zone as dob.

# No type checking:

# If dob is nil or not a Date/Time object, it will raise an error.

# Not using python helpers:

# In Python, we can use age calculation methods that handle this better.
from datetime import datetime

def adult(dob):
    if not isinstance(dob, datetime):
        raise ValueError("dob must be a datetime object")
    
    today = datetime.now()
    age = (today - dob).days / 365.25  # Accounts for leap years
    return age >= 18

# Example usage
dob = datetime(1990, 5, 10)
print(adult(dob))

# Example usage with invalid input
dob = datetime(2010, 8, 15)  # Invalid input
print(adult(dob))
