nums = [2,2,3,1]
nums=list(set(nums))
if(len(nums)>=3):
    print(nums[-3])
else:
    print(nums[-1])