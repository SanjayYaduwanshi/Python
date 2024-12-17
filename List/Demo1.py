# Program to check if element exists in list

nums=[2,3,5,4,6,8,7,9,3,1]
val=3
for i in range(len(nums)):
    if(nums[i]==val):
        print("Element exist")
        break
else:
    print("Element doesn't exist")
