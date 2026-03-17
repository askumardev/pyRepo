## python3 Basics/params_by_key_value_args.py

def person(name, **data):
  print(name)
  for i,j in data.items():
    print(i,j)

person("satish",age=30,city="Vizag",mobile=123456)