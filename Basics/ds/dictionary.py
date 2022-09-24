# python3 Basics/ds/dictionary.py

# A dictionary is an unordered collection of data that stores data in key-value pairs.

data = {1:"satish", 2:13, 3:"kumar", 4:10.5}
print(data) #{1: 'satish', 2: 13, 3: 'kumar', 4: 10.5}

print(data[2]) #13
#print(data[5]) #KeyError: 5

print(data.keys()) #dict_keys([1, 2, 3, 4])
print(data.values()) #dict_values(['satish', 13, 'kumar', 10.5])

print(data.get(1)) #satish
print(data.get(5)) #None
print(data.get(5,'Not Found')) #Not Found

keys = ["ram","kumar","shyam"]
values = [1,2,3]
new = dict(zip(keys,values))
print(new) #{'ram': 1, 'kumar': 2, 'shyam': 3}
new['kumar'] = 4
print(new) #{'ram': 1, 'kumar': 4, 'shyam': 3}
new['kiran'] = 5
print(new) #{'ram': 1, 'kumar': 4, 'shyam': 3, 'kiran': 5}

del new['kumar']
print(new) #{'ram': 1, 'shyam': 3, 'kiran': 5}

dict1={"key1":"value1","key2":"value2"}
dict2={}   # empty dictionary
dict3=dict({1:"apple",2:"cherry",3:"strawberry"})
print(dict1)
print(dict2)
print(dict3)
