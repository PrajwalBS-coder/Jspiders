arrays = [[1,2,3],[4,5],[1,2,3]]
sm=arrays[0][0]
big=arrays[-1][-1]
mxd=0
for i in range(1,len(arrays)):
    a=arrays[i]
    mxd=max(mxd,abs(a[-1]-sm),abs(big-a[0]))
    sm=min(sm,a[0])
    big=max(big,a[-1])
print(mxd)