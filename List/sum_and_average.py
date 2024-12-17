nums = [11, 2,3,5,4,6,7,8,9,2,1,2, 3, 4, 5, 61, 7, 8, 9, 101,11]
# sum=0
# for i in nums:
#     sum+=i
# print(sum)


#Average
avg=0
sum=0
for i in nums:
    sum+=i
avg=round(sum/len(nums),2)
print(avg)