import re

def convert_to_dashed_string(text: str) -> str:
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    dashed_string = re.sub(r'\s+', '-', cleaned_text.strip())
    return dashed_string.lower()

input_string = "Hello, World! This is a test."
result = convert_to_dashed_string(input_string)
print(result)

# Additional test cases
print(convert_to_dashed_string("  Leading and trailing spaces  "))
print(convert_to_dashed_string("Multiple   spaces in   between"))
print(convert_to_dashed_string("Special characters!@#$%^&*()"))


# python3 AI_ML/basic/str_function.py