nums = [0,0,0,0]
from itertools import combinations
combinations_of_three = list(set(combinations(nums, 3)))
c=0
for i in combinations_of_three:
    if i[0]+i[-1]==i[1]/2:
        c+=1
print(c)