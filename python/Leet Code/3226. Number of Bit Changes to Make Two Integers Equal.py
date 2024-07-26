n = 13
k = 4
n1=""
n2=""
if(n==k):
    print(0)
else:
    while(n!=0):
        ld=n%2
        n1=str(ld)+n1
        n//=2
    while(k!=0):
        ld=k%2
        n2=str(ld)+n2
        k//=2
if(n1.count('1')==n2.count('1')):
    print(-1)
print(n1.count('1')-n2.count('1'))
print(n1,n2)