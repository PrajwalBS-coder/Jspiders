def harshad(n,c,sum=0):
    while n!=0:
        ld=n%10
        sum+=ld
        n//=10
   # print(sum)
    return c%sum==0

num=12
#print(harshad(num,num))
print('Harshad Number' if(harshad(num,num)) else 'Not Harshad Number')