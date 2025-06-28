nums =[-35]
k = 3
from itertools import combinations
a=list(combinations(nums, k))
max=sum(a[0])
pair=[]
for i in a:
    if sum(i) > max:
        pair = i
        max=sum(i)
print(a)
print(pair)