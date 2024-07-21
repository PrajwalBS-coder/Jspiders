nums = [[1,2,3],[4,5,6]]
res = set(nums[0])
for i in range(1,len(nums)-1):
    res &=(set(nums[i]).intersection (set(nums[i+1])))
    # res.append(nums[0][i])
print(res)