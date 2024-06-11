# python3 Basics/str_concat.py

print("Enter Two Strings: ", end="")
strOne = input()
strTwo = input()

print("\nFirst String before Concatenation: ", strOne)
strOne = strOne + strTwo
print("\nFirst String after Concatenation: ", strOne)

print("***********using list*******")
print("Enter Two Strings: ", end="")
strOne = input()
strTwo = input()

print("\nFirst String before Concatenation:", strOne)

oneList = []
twoList = []
oneList[:0] = strOne
twoList[:0] = strTwo
oneLen = len(strOne)
twoLen = len(strTwo)

for i in range(twoLen):
  oneList.insert(oneLen, twoList[i])
  oneLen = oneLen+1

print("\nFirst String after Concatenation: ", end="")
for i in range(len(oneList)):
  print(end=oneList[i])
print()

print("************using join method**********")
print("Enter Two Strings: ", end="")
strOne = input()
strTwo = input()

print("\nBefore Concatenation: ", strOne)
strOne = "".join([strOne, strTwo])
print("\nAfter Concatenation: ", strOne)