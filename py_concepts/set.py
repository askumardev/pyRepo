#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.

#* Note: Set items are unchangeable, but you can remove items and add new items.

s = {31,12,23,45,15}
print(s) #{12, 45, 15, 23, 31}

s = {31,12,23,45,15,1,16,15}
print(s) #{1, 12, 45, 15, 16, 23, 31}

#print(s[2]) #TypeError: 'set' object does not support indexing