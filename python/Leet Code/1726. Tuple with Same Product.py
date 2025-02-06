from itertools import permutations
nums = [1,2,4,5,10]
l=[]
for p in permutations(nums,4):
    a,b,c,d=p
    if (a*b)==(c*d):
        l.append(p)
print(len(l))
