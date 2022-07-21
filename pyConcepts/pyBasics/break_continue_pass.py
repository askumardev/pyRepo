for i in range(5):
  if i==3:
    break
  print("hello ",i)  

for i in range(1,20):
  if i%3==0 or i%5==0:
    continue
  print(i)
print("Bye")


#to run a empty function we can use pass
def fun():
  pass

print("testing pass keyword")

#python3 pyConcepts/pyBasics/break_continue_pass.py 