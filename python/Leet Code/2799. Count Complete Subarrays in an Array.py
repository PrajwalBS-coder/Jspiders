nums = [1,3,1,2,2]
from itertools import combinations
distinct = len(set(nums))  # Calculate this once outside the loop
count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        subarray = nums[i:j]
        if len(set(subarray)) == distinct:
            count += 1

print(count)
