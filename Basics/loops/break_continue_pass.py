x = 1
for i in range(5):
  if i == 3:
    break
  print("hello ",i)  
print("------------------------------")
for i in range(1, 10):
  if i%3==0 or i%5==0:
    continue
  print(i)
print("------------------------------")

#to run a empty function we can use pass
if x == 1:
  pass # this is used when we want to write code later but want to run the program without any error
print("testing pass keyword")

# python3 Basics/loops/break_continue_pass.py
