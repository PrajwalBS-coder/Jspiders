arr1 = [12]
arr2 = [4]
l=[]
for i in arr1:
    for j in arr2:
        l.append(i & j)

print(l)
op=0
if(len(l)>=2):
    op=l[0]^l[1]
    for m in range(2,len(l)):
        # print(l[m+1])
        op=op ^l[m]
        print(op)
else:
    op=l[0]
print(op)