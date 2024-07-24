# python3 Basics/str/great_count.py

str = "gggggggrrrrrrrreeeeeeeeeeaaaaaaaattttttttttttttt"
arr = list(str)
hsh = {x: arr.count(x) for x in set(arr)}
print(hsh)

