from collections import Counter
nums = [11, 2,3,5,4,6,7,8,9,2,1,2, 3, 4, 5, 61, 7, 8, 9, 101,11]
# val=2
# k=0
# # 1 using for loop
# for i in nums:
#      if i==val:
#         k+=1

# print(k)    



res=Counter(nums)
print(res)
