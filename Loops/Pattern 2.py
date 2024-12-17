
nums=[3,2,2,3]
val=3
newList=[x for x in nums if x!=val ]
print(newList)
# temp=nums.__len__()-1
# # print(nums.__len__())
# print(len(nums))
# for i in range(nums.__len__()):
#     if(i>=temp):
#         k=i+1
#         break
#     if(nums[temp]==val):
#         temp-=1
#     if(nums[i]==val):
#        x=nums[temp]
#        nums[temp]=nums[i]
#        nums[i]=x
#        temp-=1
# print(nums)
# print(k)       