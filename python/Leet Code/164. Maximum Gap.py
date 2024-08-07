nums = [10]
nums.sort()
l=[]
if(len(nums)<2):
    print(0)
else:
    for i in range(len(nums)-1):
        l.append(abs(nums[i]-nums[i+1]))
print(max(l))