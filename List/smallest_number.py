
nums = [11, 2,3,5,4,6,7,8,9,2,1,2, 3, 4, 5, 61, 7, 8, 9, 101,11,-1,-3,100]
small=0

for i in nums:
    if(i<small):
        small=i
print(small)


# using min() method
print(min(nums))
print(max(nums))
print(nums.sort())
print(nums)


