# nums = [9,6,4,2,3,5,7,0,1]
# nums.sort()
# l=[i for i in range(nums[0],nums[-1]+1)]
# op=(str(set(l)-set(nums)))
# print(op.strip("{}"))


nums = [0,1]
nums.sort()
l=[i for i in range(nums[0],nums[-1]+1)]
if(len(l)==2):
    print(l[-1]+1)
for i in l:
    if i not in nums:
        print(i,end=" ")
        break
# print(l)