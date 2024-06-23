#A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are used to store multiple items in a single variable.
# Set uses hash internally

#* Note: Set items are unchangeable, but you can remove items and add new items.

s = {31,12,23,45,15}
print(s) #{12, 45, 15, 23, 31}

s = {31,12,23,45,15,1,16,15}
print(s) #{1, 12, 45, 15, 16, 23, 31}

#print(s[2]) #TypeError: 'set' object does not support indexing

set1={1,2,2,3,4,5,"hello","tup"}
set2={(1,8,"python",7)}
print(set1) #{1, 2, 3, 4, 5, 'hello', 'tup'}
print(set2) #{(1, 8, 'python', 7)}

# python3 Basics/ds/set.py