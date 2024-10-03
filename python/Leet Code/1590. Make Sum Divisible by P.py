nums = [6,3,5,2]
p = 9
re=nums[::]
nums.sort()
print(nums)
re=nums
while(sum(nums)%p!=0):
    nums=nums[:len(nums)-1:]
    print(nums)
print(len(re)-len(nums))