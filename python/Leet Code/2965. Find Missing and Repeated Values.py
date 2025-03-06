grid = [[9,1,7],[8,9,2],[3,4,6]]
l=[]
l2=[]
for i in grid:
    l.extend(i)
for i in  range(1,len(l)+1):
    if l.count(i)>1:
        l2.append(i)
for i in  range(1,len(l)+1):
    if i not in l:
        l2.append(i)
    
print(l2)