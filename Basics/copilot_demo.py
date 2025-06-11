# Write a python program to reverse a string without using any built-in functions.

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_str = "Hello, World!"
print("Original String:", input_str)
print("Reversed String:", reverse_string(input_str))