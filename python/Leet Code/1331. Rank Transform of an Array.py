arr = [37,12,28,9,100,56,80,5,12]
p=arr
arr=sorted(list(set(arr)))
print(arr)
l=[]

for i in p:
    l.append(arr.index(i)+1)
print(l)