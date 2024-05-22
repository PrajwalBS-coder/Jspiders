l=[1,9,99,67,34,667]
#print(l.sort())
#print(l)
for p in range(len(l)):
    lowvalueind=p
    for q in range(p+1,len(l)):
        if l[lowvalueind]>l[q]:
            lowvalueind=q
    l[p],l[lowvalueind]=l[lowvalueind],l[p]
print(l)
