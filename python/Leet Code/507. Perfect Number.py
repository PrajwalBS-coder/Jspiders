num = 28
l=[]
for i in range(1,num):
    if(num%i==0):
        l.append(i)
print(num==sum(l))
