l=[2,6,33,89,33,76,19,64,98,15]
for ind in range(len(l)-1,0,-1):
    for ind2 in range(ind):
        if l[ind]<l[ind2]:
            l[ind],l[ind2]=l[ind2],l[ind]
            print(l)
print(l)#ascending


for ind in range(len(l)-1,0,-1):
    for ind2 in range(ind):
        if l[ind]>l[ind2]:
            l[ind],l[ind2]=l[ind2],l[ind]
#print(l)#descding

for ind in range(len(l)-1,len(l)-2,-1):
    for ind2 in range(ind):
        if l[ind]<l[ind2]:
            l[ind],l[ind2]=l[ind2],l[ind]
#print(l[-1])#to find the largest in list


for ind in range(len(l)-1,len(l)-2,-1):
    for ind2 in range(ind):
        if l[ind]>l[ind2]:
            l[ind],l[ind2]=l[ind2],l[ind]
#print(l[-1])#to find the smallest in list

