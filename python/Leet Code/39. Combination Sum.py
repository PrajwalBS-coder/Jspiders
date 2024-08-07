candidates = [2,3,5]
target = 8
l=[]
for i in candidates:
    if(target % i==0):
        l.append(int(str(i)*(target //i)))
    if(i==target):
        l.append(i)
sum=0
k=[]
for j in candidates:
    if(sum<=target):
        k.append(j)
        sum+=j
        if(sum==target):
            l.append(','.join(k))
            break

print(l)
print(k)