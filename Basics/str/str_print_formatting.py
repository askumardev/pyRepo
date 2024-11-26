#Print Formatting
x = "Insert some thing here: {}".format("INSERT ME!")
print(x)
x = "Item one: {} Item two: {}".format("1","2")
print(x)

x = "Item one: {x} Item two: {y}".format(x="1",y="2")
print(x)

x = "Item one: {y} Item two: {y}".format(x="1",y="2")
print(x)

# python3 Basics/str/str_print_formatting.py