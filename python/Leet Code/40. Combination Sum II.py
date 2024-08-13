from itertools import combinations as c
candidates = [10,1,2,7,6,1,5]
target = 8
l=[]
p=[]
for r in range(1,len(candidates)+1):
    l.extend(c(candidates,r))
for i in l:
       if(sum(list(i))==target):
           p.append(list(i))
for i in range(len(p)):
     p[i].sort()
unique_lists = list(set(tuple(x) for x in p))
print(unique_lists)