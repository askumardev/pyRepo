# python3 cop/mobile_no_regex.py

import re

def is_valid_indian_mobile(number):
    # Indian mobile numbers: 10 digits, start with 6-9
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, number) is not None

# Example usage
print(is_valid_indian_mobile("9876543210"))  # True
print(is_valid_indian_mobile("1234567890"))  # False