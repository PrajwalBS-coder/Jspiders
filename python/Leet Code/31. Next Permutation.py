from itertools import permutations as p
nums = [1,2,3]
nums2=nums[::]
nums.sort()
l=list(p(nums))
print(l)
p=[]
for ele in l:p.append(list(ele))
for i in range(len(p)):
    if(p[i]==nums2):
        if(i==len(p)-1):
            print(p[0])
            break
        print('2nd one',p[i+1])
        break
# print(nums2)