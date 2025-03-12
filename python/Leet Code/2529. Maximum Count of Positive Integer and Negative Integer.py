nums = [-2,-1,-1,1,2,3]
pos_count = sum(num > 0 for num in nums)
neg_count = sum(num < 0 for num in nums)

# Find the maximum count
maximum = max(pos_count, neg_count)
print(maximum)