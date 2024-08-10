import math as m
n = 7
f=1
c=0
for i in range(1,n+1):
    f *= i
s=str(f)
for i in range(len(s)-1,-1,-1):
    if (s[i])=='0':
        c+=1
    if(s[i])!= '0':
        break
print(c)