import statistics
import numpy as np
nums = [11, 2,3,5,4,6,7,8,9,2,1,2, 3, 4, 5, 61, 7, 8, 9, 101,11]
# sum=0
# for i in nums:
#     sum+=i
# print(sum)


#Average
# avg=0
# sum=0
# for i in nums:
#     sum+=i
# avg=round(sum/len(nums),2)
# print(avg)


# using sum() method
# total=sum(nums)
# print("sum=",total)
# print("average= ",round(total/len(nums),2))


# # using statistics mean() method
# avg=statistics.mean(nums)
# print(round(avg,2))


# using numpy module sum() and average() functions
sum=np.sum(nums)
avg=np.average(nums)
print(sum)
print(avg)