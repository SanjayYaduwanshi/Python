# Program to revers a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
length=len(nums)
# print(int(length/2))
for i in range(int(length/2)):
    temp=nums[length-i-1]
    nums[length-i-1]=nums[i]
    nums[i]=temp
print(nums)    