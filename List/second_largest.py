
nums = [11, 2,3,-100,5,4,-200, 8, 9, 101,11,-1,-3,100]

#second smallest

# smallest=float('inf')
# sec_smallest=float('inf')

# for i in nums:
#     if (i<smallest):
#         sec_smallest=smallest
#         smallest=i
#     elif(i<sec_smallest and i!=smallest):
#         sec_smallest=i   

# if(sec_smallest==float('inf')):
#     print("no second smallest")       
# else:      
#     print(sec_smallest)            


# Second Largest

largest=-float('inf')
sec_largest=-float('inf')
for i in nums:
    if(i>largest):
        sec_largest=largest
        largest=i
    elif (i>sec_largest and i != largest):
        sec_largest=i
if(sec_largest==-float('inf')):
    print("no second largest")
else:
    print(sec_largest)                