nums = [1,4,2,1]
k = 3
count = 0
max_num = max(nums)

# Generate all possible subarrays
for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        subarray = nums[i:j]
        if subarray.count(max_num) >= k:
            count += 1
print(count)  