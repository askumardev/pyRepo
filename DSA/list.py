# python3 Basics/ds/list.py
# A list is a collection of ordered data.

"""
0  1  2  3  4  5  6
[2,34,54,65,76,21,'satish']
-7 -6 -5 -4 -3 -2 -1 
"""
nums = [2,34,54,65,76,21,'satish']
#print nums #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(nums)?
print(nums) #[2, 34, 54, 65, 76, 21, 'satish']
print(nums[2]) #54
#print(nums[10]) #IndexError: list index out of range
print(nums[2:]) #[54, 65, 76, 21, 'satish']
print(nums[-4]) #65

names = [10,'kiran',17.6]
print(names) #[10, 'kiran', 17.6]
names = [10.2,'kiran',17]
print(names) #[10.2, 'kiran', 17]

combine = nums + names
print(combine) #[2, 34, 54, 65, 76, 21, 'satish', 10.2, 'kiran', 17]
combine = [nums, names]
print(combine) #[[2, 34, 54, 65, 76, 21, 'satish'], [10.2, 'kiran', 17]]

list1=[1,4,"Gitam",6,"college"]
list2=[]  # creates an empty list
list3=list((1,2,3))
print(list1)
print(list2)
print(list3)
