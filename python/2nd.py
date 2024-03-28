a=int(input())
b=a*a
print(b)
v=0
r=0

while(b!=0):
    r=b%10
    
    v=v+r
    b=b//10
    #print(v)
print((v))