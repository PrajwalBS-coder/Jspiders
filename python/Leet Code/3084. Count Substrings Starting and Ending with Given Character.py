s = "abada"
c = "a"
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if(s[i:j][0]==c and s[i:j][-1]==c):
            l.append(s[i:j])
print(l)