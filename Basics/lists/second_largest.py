# python3 Basics/lists/second_largest.py

list_val = []  
  
# user provides the number of elements to be added in the list  
num_list = int(input("Enter number of elements in list: "))  
  
  
for i in range(1, num_list + 1):  
  element = int(input("Enter the elements: "))  
  list_val.append(element)  
  
# sort the list  
list_val.sort()  
      
# print second largest element  
print("Second largest element is:", list_val[-2])  