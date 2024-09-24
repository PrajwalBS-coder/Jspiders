arr1 = [1,10,100]
arr2 = [1000]
arr3=set()


for v in arr1:
    while v not in arr3 and v>0:
        arr3.add(v)
        v//=10
lp=0   
for v in arr2:
    while v not in arr3 and v>0:
        v//10
    if(v>0):
        lp=max(lp,len(str(v)))

print(lp)