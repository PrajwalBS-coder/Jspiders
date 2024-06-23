nums = [1,1,2,1,1]
k=3
l=[]
c=0
op=0
for i in range(len(nums)):
    for k in range(len(nums)+1):
        if(len(nums[i:k])>=3):
            for m in range(len(nums[i:k])):
                print(nums[i:k][m])
                c=0
                if(nums[i:k][m]==1):
                    print("yes")
                    c+=1
            if(c==k):
                print("op")
                op+=1
print(op)
"""for t in range(len(l)):
    for g in range(len(l[t])-1):
        if l[t][g]==1:
            c+=1
    if(c!=k):
        l.pop(l[t][g])
print(l)"""

#print(l)