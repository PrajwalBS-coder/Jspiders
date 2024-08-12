nums = [1,2]
k = 3
l=nums[(-k%(len(nums)))::]
for i in nums:
    if i not in l:
        l.append(i)
nums=l
print(nums)

