nums = [-5]
k = 5
c=0
if(len(nums)==1):
    if(int(sum(nums)%k==0)):
            c+=1

for i in range(len(nums)+1):
    for j in range(i+1,len(nums)+1):
       # pass
       print(nums[i:j])
        #if(int(sum(nums[i:j+1])%k==0)):
            #c+=1
print(c)

#print(abs(sum([4, 5, 0, -2, -3])))