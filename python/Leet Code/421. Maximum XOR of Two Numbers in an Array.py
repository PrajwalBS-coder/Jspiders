nums = [14,70,53,83,49,91,36,80,92,51,66,70]
l=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        # print(nums[i]^nums[j])
        l.append(nums[i]^nums[j])
l.sort()
print(l[-1])