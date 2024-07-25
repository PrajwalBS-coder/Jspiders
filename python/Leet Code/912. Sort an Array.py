nums = [5,1,1,2,0,0]
for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[j]>nums[i]):
            nums[j],nums[i]=nums[i],nums[j]
print(nums)