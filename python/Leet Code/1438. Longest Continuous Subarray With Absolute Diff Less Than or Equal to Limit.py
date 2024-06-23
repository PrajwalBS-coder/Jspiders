import numpy as np
nums = [8,2,4,7]
limit = 4
l=[]
k=[]
for i in range(len(nums)+1):
    for j in range(len(nums)+1):
        if(len(nums[i:j])>=1):
            l.append(nums[i:j])
for t in range(len(l)):
    if(np.prod(l[t])%limit)==0:
        k.append(l[t])

    
print(k)
"""
if (sum(l[t])%limit==0):
        continue
    else :
        l.remove(l[t])
nums = [8,2,4,7]
limit = 4
l=[]
for i in range(len(nums)+1):
    for j in range(len(nums)+1):
        if(len(nums[i:j])>=1):
            for o in range(len(nums[i:j])):
                print(nums[i:j][o])
            l.append(nums[i:j])
#print(l)"""
