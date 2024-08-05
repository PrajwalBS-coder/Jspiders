from collections import Counter
arr = ["d","b","c","b","c","a"]
k = 2
c=Counter(arr)
# print(c)
for v in arr:
    if c[v] == 1:
        k -= 1
        if k == 0:
            print(v)
    print('')
