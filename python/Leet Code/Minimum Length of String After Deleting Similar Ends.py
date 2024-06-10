s = "cabaabac"
l=list(s)
print(len(l))
print(l)
for i in range(len(l)):
    for i2 in range(i+1,len(l)):
        if(l[i]==l[i2]):
            l.remove(l[i])
            l.remove(l[i2])
print(len(l))