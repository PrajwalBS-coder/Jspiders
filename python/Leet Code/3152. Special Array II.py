def sp(l):
    for i in range(len(l)-1):
        if(l[i]%2==l[i+1]%2):
            return False
            
    return True

nums = [3,4,1,2,6] 
queries = [[0,4]]
l=[]
t=[]
#queries =[[0,2],[2,3]]
for i in range(len(queries)):
    l.append(nums[queries[i][0]:queries[i][1]+1])
for p in range(len(l)):
    t.append(sp(l[p]))
print(t,l)