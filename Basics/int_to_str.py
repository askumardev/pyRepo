# python3 Basics/int_to_str.py

num_len= len(input("Enter name :"))

#print("you entered" + num_len + "Characters.") #TypeError: can only concatenate str (not "int") to str

str_len = str(num_len)
print(str_len)
print("you entered " + str_len + " Characters.") 