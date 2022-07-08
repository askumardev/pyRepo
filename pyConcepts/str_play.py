# strings are immutable in python
name = "satishkumar"
print(name[0]) #s
# print(name[15]) #IndexError: string index out of range
print(name[-1]) #r
print(name[0:4]) #sati
print(name[0:]) #satishkumar
print(name[:5]) #satis
print(name[3:15]) #ishkumar
#name[1] = 'i' #TypeError: 'str' object does not support item assignment
#print(name)
print("si"+name[3:]) #siishkumar
print(len(name)) #11

str1 = "Satish".lower()
print(str1)

str2 = str1.count("s")
print(str2)
