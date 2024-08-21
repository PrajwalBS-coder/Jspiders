nums = [0,1,2]
target = 3
l=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
           if(len(nums[i:j])==3):
            print(nums[i:j])
            l.append(sum(nums[i:j]))
for i in l:
      if target-1==i or target+1==i:
            print(i)
            break
print(l)