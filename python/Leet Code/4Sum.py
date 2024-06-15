import itertools
arr = [2,2,2,2,2]
arr.sort()
t=8
l=list(itertools.combinations(arr, 4))
l=set(l)
l=list(l)
#print(l)
for i in range(len(l)):
    if(sum(l[i])==t):
        print(l[i])
