nums = [5,4,-1,7,8]
s=0
nums.sort()
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        print((nums[i:j]))
        s=max(s,sum(nums[i:j]))
# print(s,nums)