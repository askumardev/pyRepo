# python3 Basics/ds/even_odd_list_count.py

def count(lst):
  even = 0
  odd = 0
  for i in lst:
    if i%2 == 0:
      even+=1
    else:
      odd+=1
  
  return even,odd


lst = [2,3,4,5,6,7,8,9,23,25]
even,odd = count(lst)
print(even)
print(odd)
print("Even : {} and Odd : {}".format(even,odd))