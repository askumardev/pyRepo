str = "Python is great"
# str = "P  y  t  h  o  n   i s   g  r  e  a  t"
#index:  0  1  2  3  4  5 6 7 8 9 10 11 12 13 14
print(str[0:3])  # Pyt
print(str[7:])   # is great
print(str[:6])   # Python
print(str[::2])  # Pto sgat
print(str[::-1]) # taerg si nohtyP 

print(str[0:4:1]) # Pyth
print(str[1:10:2]) # yhni
# python3 Basics/str/str_slicing.py


# Given String
# str = "Python is great"

# Index mapping:

# P  y  t  h  o  n     i  s     g  r  e  a  t
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# 🔹 Slicing Syntax
# str[start : end : step]
# start → where to begin (inclusive)
# end → where to stop (exclusive)
# step → how many steps to move
# ✅ Line-by-line Explanation
# 1. str[0:3]
# print(str[0:3])  # Pyt
# Start at index 0
# Stop before index 3

# 👉 Characters: 0,1,2 → P y t

# 2. str[7:]
# print(str[7:])   # is great
# Start at index 7
# Go till end

# 👉 i s g r e a t

# 3. str[:6]
# print(str[:6])   # Python
# Start from beginning
# Stop before index 6

# 👉 0–5 → Python

# 4. str[::2]
# print(str[::2])  # Pto sgat
# No start → begin at 0
# No end → go till end
# Step = 2 (skip every other character)

# 👉 Indexes: 0,2,4,6,8,10,12,14
# 👉 Result: P t o s g a t

# 5. str[::-1]
# print(str[::-1]) # taerg si nohtyP
# Step = -1 → reverse direction

# 👉 Entire string reversed

# 6. str[0:4:1]
# print(str[0:4:1]) # Pyth
# Start at 0, stop before 4
# Step = 1 (normal)

# 👉 Same as str[0:4]

# 7. str[1:10:2]
# print(str[1:10:2]) # yhni
# Start at index 1
# Stop before 10
# Step = 2

# 👉 Indexes: 1,3,5,7,9
# 👉 Characters: y h n i (space)

# ⚠️ Important:

# Index 9 is a space, so actual visible result looks like "yhni" (space at end may not be obvious)
# 🔥 Key Takeaways
# Start is inclusive, end is exclusive
# Step controls skipping
# Negative step reverses direction
# Missing values default to:
# start → beginning
# end → end of string