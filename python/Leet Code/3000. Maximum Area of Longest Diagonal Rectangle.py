import math
dimensions = [[3,4],[4,3]]
max=0
a=[]
for i in dimensions:
    val=((i[0]**2+i[1]**2)**0.5)
    if val>max:
        max=val
        a=[i]
print(math.prod(a[0]))