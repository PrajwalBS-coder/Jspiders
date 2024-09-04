nums = [2147483647,2147483646,2147483645,3,2,1,-1,0,-2147483648]
m=1 if min(nums)<0 else min(nums)
m2=max(nums)
for i in range(m,m2):
    if i not in nums:
        print(i)
        break
print(m,m2)