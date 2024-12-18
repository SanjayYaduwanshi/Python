nums1=[1,2,3,4]
nums2=[1,2,2,4]
flag=False
if(len(nums1)!=len(nums2)):
    print("not identical")
else:
    for i in range(len(nums1)):
        if(nums1[i]!=nums2[i]):
            flag=False
            break
        else:
            flag=True
print(flag)                
