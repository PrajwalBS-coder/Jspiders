nums = [555,901,482,1771]
c=0
for i in nums:
    if(len(str(i))%2==0):
        c+=1
print(c)