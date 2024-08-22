from itertools import permutations as p
nums = [1,2,3]
l=list(p(nums))
p=[]
for ele in l:p.append(list(ele))
print(p)