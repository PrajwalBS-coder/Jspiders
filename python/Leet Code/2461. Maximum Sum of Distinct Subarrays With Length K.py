nums = [1,2,2]
k = 2
l=[]
for i in range(len(nums)):
    if len((nums[i:i+3]))==k:
        # print(nums[i:i+3])
        if(len(nums[i:i+3]))==len(set((nums[i:i+3]))):
            l.append(sum((nums[i:i+3])))
print(max(l) if len(l)>0 else 0)
