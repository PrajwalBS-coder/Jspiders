arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
l=[]
for i in queries:
    xor=0
    for j in range(i[0],i[1]+1):
        xor=xor ^ arr[j]
    l.append(xor)
print(l)
