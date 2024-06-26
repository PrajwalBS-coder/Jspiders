"""nums = [-1,0,1,2,-1,-4]
l=[]
for i in range(len(nums)):
    for j in range()
"""
import itertools
nums = [10,-2,-12,3,-15,-12,2,-11,3,-12,9,12,0,-5,-4,-2,-7,-15,7,4,-5,-14,-15,-15,-4,10,9,-6,7,1,12,-6,14,-15,12,14,10,0,10,-10,3,4,-12,10,7,-9,-7,-15,-8,-15,-4,2,9,-4,3,-10,13,-3,-1,5,5,-4,-15,4,-11,4,-4,6,-11,-9,12,7,11,7,2,-5,13,10,-5,-10,3,7,0,-3,10,-12,2,9,-8,8,-9,13,12,13,-6,8,3,5,-9,7,12,10,-8,0,2,1,10,-7,-3,-10,-10,7,4,5,-11,-8,0,-2,-14,8,13,-8,-2,10,13]
l=list(sorted(itertools.combinations(nums,3)))
# # l=list(set(l))
# o=[]
# print(len(l))
# for k in range(len(l)):
#     if(sum(l[k])==0):
#         o.append(sorted(l[k]))
# for g in range(len(o)):
#     o.insert(g,sorted(o[g]))
# # op=set(tuple(o))
# # print(op)
# print(o)
l=[tuple(sorted(i)) for i in l if(sum(i))==0]
# k=[list(set(tuple(i))) for i in l]
# print(k)
print(l)
k=list(list(set(l)))
print(k)