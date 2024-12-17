import copy
nums = [1, 2, 3, 4, 5, 61, 7, 8, 9, 101,11]

# 1 using for loop/ append method
# new_list=[]
# for i in nums:
#     new_list.append(i)
# print(new_list)    

# 2 using copy method
# new_list=nums.copy()

# 3 using list method
# new_list=list(nums)
# print(new_list)

# 4 using slicer operator
# new_list=nums[:]
# print(new_list)

# 5 using list comprehension
# new_list=[item for item in nums]
# print(new_list)


# using Deep Copy (to create deep copy, we have to use the copy.deepcopy() functio from the copy module.)

new_list=copy.deepcopy(nums)

nums[2]=55
print(nums)
print(new_list)



