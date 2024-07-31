nums = [1,1,2,2]
nums=list(set(nums))
nums.sort()
ev=nums[-1]
l=[]
if(len(nums)==1):
    for i in range(1,len(nums)+2):
        l.append(i)
else:
    for i in range(1,ev):
        l.append(i)
print(list(set(l)-set(nums)))