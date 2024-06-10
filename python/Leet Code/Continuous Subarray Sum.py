nums=[23,2,4,6,6]
k=7
for fst in range(len(nums)-1):
    for sec in range(fst+1,len(nums)):
        if(sum(nums[fst:sec+1]))%k==0:
            print( True)
            break
print(False)