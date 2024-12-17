nums = [1,2,3,4,5,1,2,6,7,8,1,2,3]

duplicate=[]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            if(nums[j] not in duplicate):
                duplicate.append(nums[j])
print(duplicate)            



