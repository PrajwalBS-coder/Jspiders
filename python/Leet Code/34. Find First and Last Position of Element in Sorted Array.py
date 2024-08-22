nums = [5,7,7,8,8,10]
target = 6
l=[]
if target in nums:
    l.append(nums.index(target))
    l.append(nums.index(target,nums.index(target)+1))
if target in nums:
    print(l)
else:
    print([-1,-1])