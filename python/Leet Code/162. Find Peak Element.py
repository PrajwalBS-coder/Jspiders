nums = [1,2,1,3,5,6,4]
l=[]
for i in range(1,len(nums)-1):
    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        l.append(i)
print(max(l))