from collections import Counter
nums = [2,2,3,2]
# nums.sort()

for i in range(len(nums)):
    if(nums.count(nums[i])==1):
        print(nums[i])
        break