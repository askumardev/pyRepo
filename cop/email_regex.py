# python3 cop/email_regex.py

import re

def is_valid_email(email):
  # Simple regex for basic email validation
  pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("invalid-email"))     # False