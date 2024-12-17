nums=[1,2,3,4,5,6,1,2,3,4,2,1,23]
new=[]
for i in nums:
    if( i not in new):
        new.append(i)
print(new)                 