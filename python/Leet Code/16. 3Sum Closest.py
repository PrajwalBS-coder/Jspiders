nums = [-1,2,1,-4]
target = 1
nums.sort()
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
       if(sum((nums[i:j]))>=target):
           print(sum(nums[i:j]))
           break
       if(sum((nums[i:j]))<=target):
            print(sum(nums[i:j]))
            break
           