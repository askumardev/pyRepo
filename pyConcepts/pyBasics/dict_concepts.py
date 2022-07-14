data = {"JS":"Notepad","Python":['pycharm','sublime'],"Java":{'jse':'netbeans','jee':'eclipse'}}
print(data) #{'JS': 'Notepad', 'Python': ['pycharm','sublime'], 'Java': {'jse': 'netbeans', 'jee': 'eclipse'}}

#print(data['python']) #KeyError: 'python'

print(data['Python']) #['pycharm', 'sublime']
print(data['Python'][1]) #sublime

print(data['Java']) #{'jse': 'netbeans', 'jee': 'eclipse'}
print(data['Java']['jse']) #netbeans

# python3 pyConcepts/pyBasics/dict_concepts.py