nums = [-1,2,1,-4]
target = 1
nums.sort()
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
           l.append(sum(nums[i:j]))
for i in l:
      if i==target:
            print(i)
            break