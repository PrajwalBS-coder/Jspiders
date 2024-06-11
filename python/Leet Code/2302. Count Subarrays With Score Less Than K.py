nums = [1,1,1]
k = 5
c=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        if((sum(nums[i:j]))*len(nums[i:j]))<k:
            #print(nums[i:j])
            c+=1
print(c)