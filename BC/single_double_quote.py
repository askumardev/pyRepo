# In Python, you can use both single quotes (') and double quotes (") to define strings.
# The choice between the two is usually based on readability and convenience. Here are some examples:
#
# Using Single Quotes

string1 = 'Hello, World!'

#
# Using Double Quotes
string2 = "Hello, World!"
# Key Differences
# For Strings with Single Quotes: Use double quotes to avoid escaping single quotes.

# sentence = "It's a beautiful day!"
# For Strings with Double Quotes: Use single quotes to avoid escaping double quotes.

dialog = 'He said, "Python is amazing!"'
# Escaping Characters: When both types of quotes are present in a string, you must escape one of them or use triple quotes.


mixed_quotes = "He said, \"It's a beautiful day!\""
triple_quoted = """He said, "It's a beautiful day!"""
# Best Practices
# Use the type of quotes that make your string easier to read and maintain.
# Stick to a consistent style throughout your project (e.g., follow PEP 8 guidelines if working in a team).
# Triple Quotes
# Triple quotes (''' or """) are useful for multi-line strings:


multiline_string = '''This is
a multi-line
string.'''
# For simple single-line strings, it’s a matter of preference.


print("'WithQuotes'")
print("Hello 'Python'")

# print WithQuotes within single quotes
print('"WithQuotes"')
print('Hello "Python"')
print("Hello, \t World!")

# python3 BC/single_double_quote.py