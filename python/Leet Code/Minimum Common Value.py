nums1 = [1,2,3,6]
nums2 = [2,3,4,5]

nums2.sort()
nums1.sort()


for  i in range(len(nums1)):
   # print("1st")
    for j in range(len(nums2)):
       # print("2nd")
        #print(nums1[i],nums2[j])
        if nums1[i]in nums2:
            print(nums1[i])
            break
