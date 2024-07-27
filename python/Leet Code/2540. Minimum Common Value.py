nums1 = [1,2,3]
nums2 = [2,4]
n=list(set(nums1).intersection(set(nums2)))
n.sort()
print(n[0])