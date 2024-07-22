nums = [3,2,3,2,2,2]
if(len(nums)%2!=0):
    print("False")
else:
    for i in nums:
        if(nums.count(i)%2!=0):
            print(False)
            break
    else:
        print(True)