nums = [2,3,1,2,4,3]
k = 5
l=[]
l.append(sum(nums[:len(nums)//k+1]))
l.append(sum(nums[len(nums)//k+1:]))
print(max(l))


# nums=[7,2,5,10,8]
# k=2
# l=[]
# for i in range(k):
#     print(i)
#     l.append(nums[i:i%k+1])
# print(l)
