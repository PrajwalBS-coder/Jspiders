nums = [4,3,6,16,8,2]
nums.sort()
l=[]
for i in range(len(nums)):
    l.append(nums[i])
    for j in range(i+1,len(nums)):
        if nums[i]==int(nums[j]**0.5):
            l.append(nums[j])
    # else:
    #     l.clear()
print(list(set(l)))
