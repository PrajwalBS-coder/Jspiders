nums = [1,3,1,2,2]
from itertools import combinations
c=0
for r in range(1, len(nums)+1):
    for combo in combinations(nums, r):
        print(combo)
        if len(set(nums))==len((combo)):
            c+=1
print(c)
