from itertools import permutations as p
nums = [1,1,2]
l=list(p(nums))
l=set(l)
p=[]
for ele in l:p.append(list(ele))
print(p)