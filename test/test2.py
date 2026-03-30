result  = []

try:
  result.append("try")
except TypeError:
  result.append("except")
else:
  result.append("else")
finally:
  result.append("finally")

print(result)