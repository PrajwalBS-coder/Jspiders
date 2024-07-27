n = 521
s=0
si=1
# for i in range(len(str(n))):
    # if(i%2==0):
    #     while(n!=0):
    #         ld=n%10
    #         s=ld*(+1)
# while(n!=0):
#     ld=n%10**(len(str(n))-1)
#     print(ld)
#     s+=ld*(si)
#     si=si*-1
#     n=n//10**(len(str(n))-1)
# print(s)

for digit in str(n):
    s+= (si * int(digit))
    si *= -1
print(s)
    
