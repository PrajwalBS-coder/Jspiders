nums = [2,7,9,3,1]
c=0
for i in range(len(nums)):
    if(i%2==0):
        c+=nums[i]
print(c)