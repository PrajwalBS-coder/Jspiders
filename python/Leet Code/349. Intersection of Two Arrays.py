nums1 = [1,2,2,1]
nums2 = [2,2]
n=[]
nums1=list(set(nums1))
nums2=list(set(nums2))
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if(nums1[i]==nums2[j]):
            n.append(nums1[i])
print(n)