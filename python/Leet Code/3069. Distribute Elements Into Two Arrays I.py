nums = [2,1,3]
arr1=[]
arr2=[]
arr1.append(nums[0])
arr2.append(nums[1])
for i in range(2,len(nums)):
    if arr2[-1]<arr1[-1]:
        arr1.append(nums[i])
    else:
        arr2.append(nums[i])
print(arr1+arr2)