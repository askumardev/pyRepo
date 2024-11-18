# python3 Basics/lists/iterator.py

arr = [2,3,4,5,6]

it = iter(arr)
print(it.__next__())
print(it.__next__())
print("*****")
print(next(it))
print("#####")
for i in arr:
  print(i)