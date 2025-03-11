
from itertools import combinations
s = "aaacb"
l= [s[i:j] for i, j in combinations(range(len(s) + 1), 2)]
c=0
for i in l:
    if "a" in i and "b" in i and "c" in i:
        print(i)
        c+=1
print(c)
