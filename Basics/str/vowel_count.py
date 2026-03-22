str = "Hello, World!"
# str = input("Enter a string: ")
vowels = "aeiou"
count = 0
for char in str.lower():
    if char in vowels:
        count += 1  

print(f"The number of vowels in the string is: {count}")

# python3 Basics/str/vowel_count.py