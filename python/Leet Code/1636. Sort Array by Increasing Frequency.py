from collections import Counter
nums = [1,1,2,2,2,3]
fr=Counter(nums)
# print(fr)
print(sorted(nums, key=lambda x : (fr[x], -x)))