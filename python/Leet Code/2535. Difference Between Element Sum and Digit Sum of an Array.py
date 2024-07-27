nums = [1,2,3,4]
s=sum(nums)
d=0
print(s)
for i in nums:
    if(i<=9):
        d+=i
    elif(i>9):
        while(i!=0):
            ld=i%10
            d+=ld
            i//=10
        
print(d)