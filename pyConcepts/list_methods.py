ary = [1,2,2,3,1,4,1]
nums = [2,34,54,65,76,21,'satish']
nums.insert(2,77) 
print(nums) #[2, 34, 77, 54, 65, 76, 21, 'satish']
nums.remove(21)
print(nums) #[2, 34, 77, 54, 65, 76, 'satish']
nums.pop(3)
print(nums) #[2, 34, 77, 65, 76, 'satish']
nums.pop()
print(nums) #[2, 34, 77, 65, 76]
print(len(nums)) #length of list --> 5
print(ary.count(1)) #3
print(ary[::-1]) #[1, 4, 1, 3, 2, 2, 1]
print(ary.index(4)) #5

del nums[2:]
print(nums) #[2, 34]

nums.extend([32,41,53])
print(nums) #[2, 34, 32, 41, 53]

print(min(nums)) #2
print(max(nums)) #53
print(sum(nums)) #162

nums.sort()
print(nums) #[2, 32, 34, 41, 53]