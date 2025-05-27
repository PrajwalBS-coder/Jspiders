n = 5
m = 1
l=[]
l2=[]
for i in range(1,n+1):
    if i %m==0:
        l.append(i)
    else:
        l2.append(i)
print(sum(l2)-sum(l))