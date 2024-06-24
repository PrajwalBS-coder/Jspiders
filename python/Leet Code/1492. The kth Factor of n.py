n = 7
k = 2
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
if(k<=len(l)):
    print(l[k-1])
else:
    print("-1")