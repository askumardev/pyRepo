greeting = "Hi"
language = "Java"
status = "bad"

# Transform values
greeting = "Hello"
language = "Python"
status = "good" if status == "bad" else status

print(f"{greeting}, {language} Learner")
print(f'I am "{status}"')

# python3 Basics/str/str_transform.py