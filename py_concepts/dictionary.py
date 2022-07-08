data = {1:"satish", 2:13, 3:"kumar", 4:10.5}
print(data) #{1: 'satish', 2: 13, 3: 'kumar', 4: 10.5}

print(data[2]) #13
#print(data[5]) #KeyError: 5

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