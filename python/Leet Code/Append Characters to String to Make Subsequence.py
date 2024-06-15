s = " "
t = "g"
l=list(t)
p=list(s)
k=[]
for i in range(len(l)):
    #print(i,l[i])
    if l[i] == p[i]:
        k.append(l[i]) 
    else:
        break
print(len(l)-len(k))