import random
import string

def get_random_string(length):
  # choose from all lowercase letter
  letters = string.ascii_letters + string.digits + string.punctuation
  print(letters)
  result_str = ''.join(random.choice(letters) for i in range(length))
  print("Random string of length", length, "is:", result_str)

get_random_string(8)


# # get random password pf length 8 with letters, digits, and symbols
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for i in range(8))
# print("Random password is:", password)