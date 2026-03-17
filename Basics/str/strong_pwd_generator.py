import random, string

def strong_password(length):
  # choose from all lowercase letter
  letters = string.ascii_letters + string.digits + string.punctuation
  # print(letters)
  result_str = ''.join(random.choice(letters) for i in range(length))
  print("Random string of length", length, "is:", result_str)

strong_password(8)
print("-----------------------------")
strong_password(10)


# # get random password pf length 8 with letters, digits, and symbols
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for i in range(8))
# print("Random password is:", password)

# python3 Basics/str/strong_pwd_generator.py